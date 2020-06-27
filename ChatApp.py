import socket
import threading
import sys
import ChatClient


class ChatApp(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.config_path = sys.argv[1]

    def app_main(self):
        while True:
            choice = input("Type /start to start a chat, or /join to join a chat: ")

            if choice == "/start":
                config_file = open(self.config_path)
                new_client = ChatClient.ChatClient(config_file)
                new_client.start()
                new_client.add_client(new_client)
                config_file.close()
                break

            elif choice[0:5] == "/join":
                config_file = open(self.config_path)
                new_client = ChatClient.ChatClient(config_file)
                new_client.start()

                ip = choice.split(" ")[1].split(":")[0]
                port = int(choice.split(" ")[1].split(":")[1])

                print(ip, port)

                try:
                    init_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    init_socket.bind((ip, port))

                    init_message = "User has joined."

                    init_socket.send(init_message.encode())
                    init_socket.close()
                    break

                except:
                    print(Exception)

            else:
                print("Invalid Input")


def main():
    my_chat = ChatApp()
    my_chat.app_main()


if __name__ == "__main__":
    main()
