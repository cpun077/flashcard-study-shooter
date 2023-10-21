import socket
import threading
import sys
import os
import signal
import atexit

class Client:
    def __init__(self, name):
        self.event = threading.Event()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 8003
        self.addr = (self.host, self.port)
        self.name = name


    def send(self, data):
        try:
            self.sock.sendall(data.encode())
        except Exception as e:
            print(e)
            self.sock.close()
            return

    def recv(self):
        try:
            data = self.sock.recv(8096).decode()
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
        self.sock.close()
        self.event.set()
        os._exit(-1)

    def start(self):
        self.sock.connect(self.addr)
        self.sock.sendall(self.name.encode())
        signal.signal(signal.SIGINT, self.kill_client)
        signal.signal(signal.SIGHUP, self.kill_client)
