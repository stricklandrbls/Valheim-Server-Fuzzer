from email.errors import BoundaryError
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
        ascii = []
        output = ""
        for char in self.package:
            if char > 17:
                ascii.append(chr(char))
            else:
                ascii.append(".")

        for char in self.package:
            value = hex(char)[2:]
            if len(value) == 1:
                _hex.append("0" + value)
            else:
                _hex.append(value)
            


        index = 0
        hex_index = 0
        for char in ascii:
            # if len(str(char)) > 2:
            #     output += char[3] + ' '
            # else:
            output += str(char) + " "

            index += 1
            if index == 5:
                output += "\t"
                for i in range(hex_index, hex_index + 5):
                    try:
                        output += _hex[i] + " "
                    except BoundaryError:
                        pass
                output += "\n"
                hex_index += 5
                index = 0
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

