import signal

# log = open ('log.txt', 'w')

stop = False


#When SIGTERM ( terminate the process in a soft way ) is detected activates the handler and sends the email
def signal_catcher(signal,frame):
    global stop
    stop = True
    # log.write("Signal Incoming...")
    # log.write("Signal Caught: %s" %str(signal))
    # log.flush()


signal.signal(signal.SIGTERM, signal_catcher)

# while stop != True:
#     log.write("Running\n")
#     log.flush()
#     time.sleep(10)
