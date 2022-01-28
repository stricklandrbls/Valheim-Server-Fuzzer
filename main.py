import socket
import lib.constants as c
from lib.packet import Packet


def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = Packet()
    target = [('45.24.126.6', 2457), ('45.24.126.6', 2456)]
    history = []
    try:
        package = packet.get_ping_package()
        s.sendto(package, target[0])
        response = s.recvfrom(c.LPACKET_SIZE)
        history.append(response[0])

        package = packet.get_echo_package(response[0])
        s.sendto(package, target[0])
        response = s.recvfrom(c.LPACKET_SIZE)
        history.append(response[0])

        package = packet.get_connect_packet()
        Packet.print(package)
        s.sendto(package, target[1])
        response = s.recvfrom(c.LPACKET_SIZE)

        history.append(response[0])

    except KeyboardInterrupt:
        for item in history:
            print(f"\n{item}")
        print("\nDone")

if __name__ == "__main__":
    run()