import socket
import threading
import signal
import os
from game import Game
import atexit

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
        self.all_clients = {}

    def queue_handler(self):
        while True:
            if len(self.client_list) >= 3:
                game = Game(dict(self.client_list), self.all_clients)
                game.start()
                self.client_list.clear()

    def shut_down_server(self, sig, frame):
        for connection in list(self.all_clients):
            connection.sendall("Server shutting down!".encode())
            connection.close()
        self.event.set()
        os._exit(1)

    def start(self):
        signal.signal(signal.SIGINT, self.shut_down_server)
        signal.signal(signal.SIGHUP, self.shut_down_server)
        handler = threading.Thread(target=self.queue_handler)
        handler.start()
        while True:
            client_socket, addr = self.sock.accept()
            name = client_socket.recv(128).decode()
            self.client_list[client_socket] = name
            self.all_clients[client_socket] = name
            print(f"{name}({addr[0]}) has joined the Server.")


if __name__ == "__main__":
    server = Server()
    server.start()