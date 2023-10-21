import threading

class Game:
    def __init__(self, client_list, all_clients):
        self.client_list = client_list
        self.all_clients = all_clients

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if data.decode() == "q":
                    print(f"{self.client_list[client_socket]} has left the server")
                    del self.client_list[client_socket]
                    del self.all_clients[client_socket]
                    client_socket.close()
                    return
                self.broadcast(data, self.client_list[client_socket])

            except Exception as e:
                del self.client_list[client_socket]
                client_socket.close()
                return

    def broadcast(self, message, client_name):
        for connection, _ in self.client_list.items():
            connection.sendall(f"{client_name}: {message.decode()}".encode())

    def start(self):
        for key, item in self.client_list.items():
            client = threading.Thread(target=self.handle_client, args=(key,))
            client.start()