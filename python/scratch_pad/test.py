import socket
import sock_func as sf

addr = ('192.168.1.253', 2456)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, True)

try:
    server.connect(addr)

    server.sendall(sf.build_connect_package())
    header = sf.capture_header(server.recv(512))

    server.sendall(sf.build_steamid_package(header[0], header[1]))
    data = server.recv(512)
    print(data.hex())

except KeyboardInterrupt:
    print("Quitting")
    server.close()
    print("Done")

# 0000   20 10 00 0d 23 2d 87 90 19 01 e0 96 7f ba 02 00
# 0010   00 20 0b 00 00 00 00 00 00 00 00 00 00 00 00 00
# 0020   ...
# 01f0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
