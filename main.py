import time

import sacn
import stupidArtnet
from stupidArtnet import StupidArtnetServer

if __name__ == '__main__':
    def test_callback(data):
        # the received data is an array
        # of the channels value (no headers)
        print('Received new data \n', data)

    # a Server object initializes with the following data
    # universe 			= DEFAULT 0
    # subnet   			= DEFAULT 0
    # net      			= DEFAULT 0
    # setSimplified     = DEFAULT True
    # callback_function = DEFAULT None

    universe = 1
    a = StupidArtnetServer()

    # For every universe we would like to receive,
    # add a new listener with a optional callback
    # the return is an id for the listener
    u1_listener = a.register_listener(
        universe, callback_function=test_callback)

    print(a)

    time.sleep(100)


