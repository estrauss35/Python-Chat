import socket
import threading

localhost = "192.168.1.74"
bufferSize = 1024


class ChatListener(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.port = None

    def run(self):
        listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listenSocket.bind((localhost, self.port))
        listenSocket.listen(1)

        while True:
            connection, address = listenSocket.accept()

            print("Established connection with ", address)

            message = connection.recv(bufferSize)

            print("Them: ", message)


class ChatSender(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.address = None
        self.port = None

    def run(self):
        sendSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sendSocket.connect((self.address, self.port))

        while True:
            message = input("You: ")

            if message.lower() == "quit":
                break
            else:
                try:
                    sendSocket.sendall(message)
                except:
                    Exception


def main():
    ip = input("Enter the address to connect to: ")
    port = int(input("Enter the port you would like to connect on: "))

    listener = ChatListener()
    listener.port = port
    listener.start()

    sender = ChatSender()
    sender.address = ip
    sender.port = port
    sender.start()

if __name__ == "__main__":
    main()


