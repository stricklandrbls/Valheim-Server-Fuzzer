import struct
from typing import List
import lib.constants as c

class Packet():
    def __init__(self, packet=[]):
        self.bytes = []
        self.package = []
        self.length = len(self.bytes)
        self.bytes_format = ""
        
        if type(packet) == bytes:
            self.bytes = packet
            self.length = len(self.bytes)
            self.bytes_format = "B" * self.length
            self.package = struct.unpack(self.bytes_format, self.bytes)
        elif type(packet) == Packet:
            self.bytes = bytes(packet)
            self.length = len(self.bytes)
            self.bytes_format = "B" * self.length

    def __str__(self):
        
        _hex = []
        ascii = ""
        output = ""
        for char in self.package:
            output += chr(char)
            output += "  "
        output += "\n"
        for char in self.package:
            _hex.append(hex(char))
        ascii = str(ascii).replace("\\x", "")
        return output

    def get_ping_package(self):
        self.build_ping_package()
        self.bytes = bytes(self.package)
        return self.bytes

    def build_ping_header(self):
        self.package = [255,255,255,255]
    
    def build_ping_package(self):
        self.build_ping_header()
        for char in "TSource Engine Query":
            self.package.append(ord(char))
        self.package.append(0x0)

    def append(self, contents):
        if type(contents) == list or type(contents) == str:
            for char in contents:
                if type(char) == str:
                    self.package.append(ord(char))
                else:
                    self.package.append(char)
            self.bytes = bytes(self.package)
        elif type(contents) == int:
            self.package.append(contents)
            self.bytes = bytes(self.package)

    def build_echo_package(self, _echo):
        self.build_ping_package()
        echo = struct.unpack(c.STRUCT_ECHO, _echo[5:])
        for char in echo:
            self.package.append(char)

    def get_echo_package(self, _echo):
        self.build_echo_package(_echo)
        self.bytes = bytes(self.package)
        return self.bytes

    def build_connect_package(self):
        self.package = [0x20, 0x10, 0x00, 0x0d, 0x9e, 0x70, 0xe0, 0x15, 0x19, 0x24, 0x66, 0x1c, 0x82, 0xba, 0x02, 0x0, 0x0, 0x20, 0x0b]
        while len(self.package) < 512:
            self.package.append(0x0)

    def get_connect_packet(self):
        self.build_connect_package()
        self.bytes = bytes(self.package)
        return self.bytes

