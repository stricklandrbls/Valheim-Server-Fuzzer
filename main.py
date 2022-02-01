import socket
import lib.constants as c
from lib.packet import Packet
from lib.History import History
from lib.comm.categories import *
from lib.comm.Socket import Socket

def run():

    s = Socket(target = "71.136.241.218")
    query = Query()
    # sequence = [Query().execute, Query.parse_server_response]
    history = History()


    s.send(query.execute())
    echo = query.parse_server_response(s.receive())
    history.append(Packet(echo))

    s.send(echo)
    history.append(Packet(s.receive()))
    history.print_last()

    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # packet = Packet()
    # history = History()
    
    # target = [('71.136.241.218', 2457), ('71.136.241.218', 2456)]
    
    # try:
    #     package = packet.get_ping_package()
    #     s.sendto(package, target[0])
    #     response = s.recvfrom(c.LPACKET_SIZE)
    #     history.append(Packet(response[0]))

    #     package = packet.get_echo_package(response[0])
    #     s.sendto(package, target[0])
    #     response = s.recvfrom(c.LPACKET_SIZE)
    #     history.append(Packet(response[0]))

    #     package = packet.get_connect_packet()
    #     s.sendto(package, target[1])
    #     response = s.recvfrom(c.LPACKET_SIZE)
    #     history.append(Packet(response[0]))
        
    #     for msg in history.list:
    #         print(msg)

    # except KeyboardInterrupt:
    #     for item in history.list:
    #         print(f"\n{item}")
    #     print("\nDone")

if __name__ == "__main__":
    run()