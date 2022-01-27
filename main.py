import socket
import struct
from lib.packet import Packet

def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = Packet()
    target = ('72.177.3.63', 2456)
    history = []
    try:
        package = packet.get_ping_package()
        s.sendto(package, target)
        response = s.recvfrom(2048)
        history.append(response[0])

        package = packet.get_echo_package(response[0])
        s.sendto(package, target)
        response = s.recvfrom(2048)
        history.append(response[0])

        package = packet.get_test_packet()
        s.sendto(package, target)
        response = s.recvfrom(2048)
        history.append(response[0])

    except KeyboardInterrupt:
        for item in history:
            print(f"\n{item}")
        print("\nDone")

if __name__ == "__main__":
    run()