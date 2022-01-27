import struct
from typing import List
import lib.constants as c

class Packet():
    def __init__(self):
        self.header = [255, 255, 255, 255]
        self.bytes_msg = []
        self.package = []

    def get_ping_package(self):
        self.build_ping()
        self.bytes_msg = bytes(self.package)
        return self.bytes_msg

    def build_ping_header(self):
        self.package = [255,255,255,255]
    
    def build_ping(self):
        self.build_ping_header()
        for char in "TSource Engine Query":
            self.package.append(ord(char))
        self.package.append(0x0)

    def append(self, contents = List):
        for char in contents:
            if type(char) == str:
                self.package.append(ord(char))
            else:
                self.package.append(char)

    def build_echo(self, _echo):
        self.build_ping()
        echo = struct.unpack(c.STRUCT_ECHO, _echo[5:])
        for char in echo:
            self.package.append(char)

    def get_echo_package(self, _echo):
        self.build_echo(_echo)
        self.bytes_msg = bytes(self.package)
        return self.bytes_msg

    def build_test_packet(self):
        self.package = [0x20, 0x10, 0x00, 0x0d, 0x9e, 0x70, 0xe0, 0x15, 0x19, 0x24, 0x66, 0x1c, 0x82, 0xba, 0x02, 0x00, 0x00, 0x20, 0x0b]
        while len(self.package) < 512:
            self.package.append(0x0)

    def get_test_packet(self):
        self.build_test_packet()
        self.bytes_msg = bytes(self.package)
        return self.bytes_msg