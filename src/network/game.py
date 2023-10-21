import threading
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from GameState import GameState

class Game:
    def __init__(self, client_list, all_clients):
        self.client_list = client_list
        self.all_clients = all_clients
        self.game = GameState()
        self.game.initialize_random(500)

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(8096)
                if data.decode() == "q":
                    print(f"{self.client_list[client_socket]} has left the server")
                    del self.client_list[client_socket]
                    del self.all_clients[client_socket]
                    client_socket.close()
                    return
                self.broadcast(data, client_socket)

            except Exception as e:
                del self.client_list[client_socket]
                client_socket.close()
                return

    def broadcast(self, message, send_sock):
        for connection, _ in self.client_list.items():
            if connection == send_sock:
                continue
            connection.sendall(message)

    def start(self):
        for client, _ in self.client_list.items():
            client.sendall(self.game.encode_initial_data().encode())
            client = threading.Thread(target=self.handle_client, args=(client,))
            client.start()