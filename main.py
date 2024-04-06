import time

import sacn
from stupidArtnet import StupidArtnetServer

if __name__ == '__main__':
    sender = sacn.sACNsender(source_name='sAcn Converter',
                             fps=30,
                             bind_address='192.168.178.131')
    sender.start()

    sender.activate_output(1)
    sender[1].multicast = True
    sender[1].priority = 50


    def test_callback(data):
        print('Received new data \n', data[0])
        sender[1].dmx_data = data
        sender.flush()


    # a Server object initializes with the following data
    # universe 			= DEFAULT 0
    # subnet   			= DEFAULT 0
    # net      			= DEFAULT 0
    # setSimplified     = DEFAULT True
    # callback_function = DEFAULT None

    universe = 1
    a = StupidArtnetServer()

    # ArtNet input
    u1_listener = a.register_listener(
        universe,  is_simplified=True) #callback_function=test_callback,
    print(a)

    while True:
        sender[1].dmx_data = a.get_buffer(u1_listener)
        #print(a.get_buffer(u1_listener))
        sender.flush()
