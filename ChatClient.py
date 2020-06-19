import socket
import threading

class ChatClient(threading.Thread):

    def __init__(self):
        self.clients = None
        self.connected = None

        self.host = input("Enter the host ip: ")
        self.port = int(input("Enter port: "))
        self.setConnection(True)

    def addClients(self, newClient):
        count = 0
        for client in self.clients:
            count = client
            count += 1
        self.clients[count] = newClient

    def removeClients(self, leavingClient):
        for client in self.clients:
            if self.clients.get(client).getIp() == leavingClient.getIp():
                self.clients.get(client).setConnection(False)
                self.clients.pop(client)

    def setConnection(self, connectionStatus):
        self.connected = connectionStatus

    def getConnection(self):
        return self.connected

    def getPort(self):
        return self.port

    def getIp(self):
        return self.host

    def setIp(self, ip):
        self.host = ip

    def setPort(self, port):
        self.port = port
