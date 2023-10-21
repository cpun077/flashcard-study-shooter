import socket
import threading
import sys
import os
import signal
import atexit

class Client:
    def __init__(self):
        self.event = threading.Event()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 8002
        self.addr = (self.host, self.port)

    def send(self, data):
        try:
            sys.stdout.write("\x1b[1A\x1b[2K")
            self.sock.sendall(data.encode())
        except:
            self.sock.close()
            return

    def recv(self):
        try:
            data = self.sock.recv(1024).decode()
            print(data)
            if data == "Server shutting down!":
                self.sock.close()
                os._exit(1)
                return
        except:
            self.sock.close()
            os._exit(1)
            return
        return data

    def kill_client(self, sig, frame):
        self.sock.sendall("q".encode())
        print("hi")
        self.sock.close()
        self.event.set()
        os._exit(-1)

    def start(self):
        name = sys.argv[1]
        self.sock.connect(self.addr)
        self.sock.sendall(name.encode())
        signal.signal(signal.SIGINT, self.kill_client)
        signal.signal(signal.SIGHUP, self.kill_client)


if __name__ == "__main__":
    client = Client()
    client.start()
    while True:
        pass