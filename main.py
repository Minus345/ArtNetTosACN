import sys
import time

import sacn
from stupidArtnet import StupidArtnetServer

if __name__ == '__main__':

    print(sys.argv)
    senderIp = sys.argv.__getitem__(1)
    print("Sender Ip:", senderIp)
    maxUniverse = 1 + int(sys.argv.__getitem__(2))  # Universe Count -1 because I´m starting with universe 1 and not 0
    print("Universes:", maxUniverse - 1, "From: 1 -", maxUniverse - 1)
    debug = False
    if len(sys.argv) > 3:
        if sys.argv.__getitem__(3) is not None:
            debug = True

    sender = sacn.sACNsender(source_name='sAcn Converter', fps=30, bind_address=senderIp)
    sender.start()

    for x in range(1, maxUniverse):
        sender.activate_output(x)
        sender[x].multicast = True
        sender[x].priority = 50
        print("created Universe: ", x)

    # ArtNet input
    ArtNetServer = StupidArtnetServer()
    artNetListeners = []

    for x in range(1, maxUniverse):
        print(x)
        artNetListeners.append(ArtNetServer.register_listener(x, is_simplified=True))
        print(ArtNetServer)

    print(artNetListeners)

    print("Start Sending sAcn")
    while True:
        for x in range(1, maxUniverse):
            sender[x].dmx_data = ArtNetServer.get_buffer(artNetListeners[x - 1])
            if debug:
                print("U:", x - 1, "Data:", ArtNetServer.get_buffer(artNetListeners[x - 1]))
        sender.flush()
