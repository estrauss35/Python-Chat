import threading
import ChatSender
import ChatListener


class ChatClient(threading.Thread):

    def __init__(self, config_file):
        threading.Thread.__init__(self)
        self.config_file = open(config_file)
        self.client_dict = {}

        self.port = None
        self.host = None
        self.is_connected = False

        try:
            self.host = self.config_file.readline(0).split(" ")[1].split(":")[0]
            self.port = int(self.config_file.readline(0).split(" ")[1].split(":")[1])

        except:
            print(Exception)
            print("Could not access file.")

    def add_client(self, new_client):
        count = 0
        for client in self.client_dict:
            count = client[0]
            count += 1
        new_client[count] = new_client

    def remove_client(self, target_client):
        for client in self.client_dict:
            count = client[0]
            if self.client_dict[count] == target_client:
                self.client_dict.pop(count)
                break

    def set_connection(self, is_connected):
        self.is_connected = is_connected

    def get_connection(self):
        return self.is_connected

    def get_port(self):
        return self.port

    def get_ip(self):
        return self.host

    def set_ip(self, ip):
        self.host = ip

    def set_port(self, port):
        self.port = port

    def run(self):
        sender = ChatSender.ChatSender(self)
        listener = ChatListener.ChatListener(self)
        try:
            sender.start()
            listener.start()
        except:
            print("Something went wrong, could not start client")
            print(Exception)

