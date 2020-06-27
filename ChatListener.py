import socket
import threading


class ChatListener(threading.Thread):

    def __init__(self, chat_client):
        threading.Thread.__init__(self)

        self.host = chat_client.get_ip()

        try:
            self.receiving_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.receiving_socket.bind((self.host, chat_client.get_ip()))
            self.port = self.receiving_socket.getsockname()[1]
        except:
            print("Something went wrong, unable to connect with client")

        self.client = chat_client
        self.client.set_connection(True)

    def run(self):

        print("Started receiver on " + self.host + ":" + self.client.get_port)

        while self.client.get_connection():

            try:
                print("Placeholder")
                # spawn a receiver worker here

            except:
                print("Something went wrong, unable to spawn receiver worker")
                print(Exception)



