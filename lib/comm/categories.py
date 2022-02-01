
from lib.packet import Packet
import lib.constants as c
import struct

class Connect():

    def initiate_connection():
        packet = Packet()
        header = [0x20, 0x10, 0x00, 0x0d, 0x9e, 0x70, 0xe0, 0x15, 0x19, 0x24, 0x66, 0x1c, 0x82, 0xba, 0x02, 0x0, 0x0, 0x20, 0x0b]
        packet.append(header)
        while len(packet.bytes) < 512:
            packet.append(0x00)
        
        return packet.bytes

class Query():
    def __init__(self, socket = None):
        self.echo = ""
        self.init_msg = "TSource Engine Query"
        self.init_header = [255, 255, 255, 255]
        self.msg = Packet()
        self.socket = socket

    def execute(self):
        self.reset()
        self.msg.append(self.init_header)
        self.msg.append(self.init_msg)
        self.msg.append(0x00)
        return self.msg.bytes

    def echo_response(self, data):
        echo = struct.unpack(c.STRUCT_ECHO, data[5:])
        for char in echo:
            self.msg.append(char)
        return self.msg.bytes

    def parse_server_response(self, data):
        return self.echo_response(data)

    def reset(self):
        self.msg.bytes = []
        self.msg.package = []