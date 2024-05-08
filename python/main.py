import socket
import lib.constants as c
from lib.packet import Packet
from lib.History import History
from lib.comm.categories import *
from lib.comm.Socket import Socket

def run():

    s = Socket(target = "71.136.241.218")
    query = Query()
    history = History()

    try:
        s.send(query.execute())
        history.append(Packet(s.receive()))
        echo = query.parse_server_response(history.last().bytes)

        s.send(echo)
        history.append(Packet(s.receive()))

        s.send(Connect.initiate_connection(), 1)
        history.append(Packet(s.receive()))

        echo = Connect.parse_connect_response(history.last().bytes)

        history.print_all()
    except KeyboardInterrupt:
        history.print_all()

if __name__ == "__main__":
    run()