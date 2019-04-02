import signal
import time

stop = False


def keeperOS():
    # When SIGTERM ( terminate the process in a soft way ) is detected activates the handler and sends the email
    def signal_catcher(signal, frame):
        global stop
        stop = True
        import senderOS
        # Never gets printed
        print( "Signal Incoming..." )
        print( "Signal Caught: %s" % str( signal ) )

import replicatorOS

    # Never gets printed
    while stop != True:
        print( "Running\n" )
        time.sleep( 10 )
        signal.signal( signal.SIGTERM, signal_catcher )
