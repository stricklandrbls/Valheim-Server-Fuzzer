import socket

class Socket():
    def __init__(self, name = "", target = ""):
        self.target = target
        self.name = name
        self.ports = [2457, 2456]
        self.destination = [(target, self.ports[0]), (target, self.ports[1])]
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def send(self, data):
        self.socket.sendto(data, self.destination[0])

    def receive(self):
        try:
            response = self.socket.recvfrom(1024)
            return response[0]
        except KeyboardInterrupt:
            print("Receiver disconnnected")