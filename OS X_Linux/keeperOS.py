import signal
import time

log = open ('log.txt', 'w')

stop = False


#When SIGTERM ( terminate the process in a soft way ) is detected activates the handler and sends the email
def signal_catcher(signal,frame):
    global stop
    stop = True
    import sender
    log.write("Signal Incoming...")
    log.write("Signal Caught: %s" %str(signal))
    log.flush()

#If SIGHUP ( terminate a connection, or reload the configuration for daemons ) is ignored
def signal_ignore(signal, frs):
    log.write('Ignoring signal %d\n' % sig)
    log.flush()

signal.signal(signal.SIGTERM, signal_catcher)
signal.signal(signal.SIGHUP, signal_ignore)

while stop != True:
    log.write("Running\n")
    log.flush()
    time.sleep(10)
