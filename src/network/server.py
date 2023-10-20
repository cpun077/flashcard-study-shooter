import socket
import threading
import signal
import os


class Server:
    def __init__(self):
        self.event = threading.Event()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 8002
        self.addr = (self.host, self.port)
        self.sock.bind(self.addr)
        self.sock.listen(10)
        self.client_list = {}
        self.games = {}

    def queue_handler(self):
        while True:
            if len(self.client_list) >= 3:
                print("hi")


    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if data.decode() == "q":
                    print(f"{self.client_list[client_socket]} has left the server")
                    del self.client_list[client_socket]
                    client_socket.close()
                    return
                self.broadcast(data, self.client_list[client_socket])

            except Exception as e:
                del self.client_list[client_socket]
                client_socket.close()
                return

    def shut_down_server(self, sig, frame):
        for connection in list(self.client_list):
            connection.sendall("Server shutting down!".encode())
            connection.close()
        self.event.set()
        os._exit(1)

    def broadcast(self, message, client_name):
        for connection, _ in self.client_list.items():
            connection.sendall(f"{client_name}: {message.decode()}".encode())

    def start(self):
        signal.signal(signal.SIGINT, self.shut_down_server)
        signal.signal(signal.SIGHUP, self.shut_down_server)
        handler = threading.Thread(target=self.queue_handler)
        handler.start()
        while True:
            client_socket, addr = self.sock.accept()
            name = client_socket.recv(128).decode()
            self.client_list[client_socket] = name
            print(f"{name}({addr[0]}) has joined the Server.")
            client = threading.Thread(target=self.handle_client, args=(client_socket,))
            client.start()


if __name__ == "__main__":
    server = Server()
    server.start()