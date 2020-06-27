import socket
import threading
import sys


class ChatSender(threading.Thread):

    def __init__(self, chat_client):
        threading.Thread.__init__(self)
        self.client = chat_client
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):

        input_message = input(self.client.get_port() + ":")

