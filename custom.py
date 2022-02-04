
import socket
import lib.constants as c
from lib.packet import Packet
from lib.History import History
from lib.comm.categories import *
from lib.comm.Socket import Socket

s = Socket(target = "71.136.241.218")
query = Query()
history = History()

try:
    while True:
        data = Packet(str(input("Enter hex data to send: ")))
        s.send(data.bytes, 1)
        history.append(Packet(s.receive()))
except KeyboardInterrupt:
    for packet in history.list:
        print(packet)
        print("\n")