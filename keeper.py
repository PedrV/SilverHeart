import time
import win32api
import win32gui

import win32con


# ------------------------------------ #
def log_info(msg):
    print( msg )
    f = open( 'C:\\Users\\User\\Documents\\Filename.log', "a" )
    f.write( msg + "\n" )
    f.close()

# ----------------------------------- #


# Reads the messages from the message map and prints
def wndproc(hwnd, msg, wparam, lparam):
    log_info( '%s' % msg )
    ctrl = msg
    #Sends email on End of Session
    if ctrl == 17:
        pass
    else:
        pass

# ---------------------------------- #

#   Test class
#   Used to create and test how to grab windows messages
#   Test "virtually posted" and "real queue" messages
#   https://devblogs.microsoft.com/oldnewthing/?p=33453

# ----------------------------------- #

# Creates invisible console (window) that detects commands

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

try:
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

except Exception as e:
    log_info( "Exception: %s" % str( e ) )

if hwnd is None:
    log_info( "No hwnd detected!" )
else:
    log_info( "hwnd: %s" % hwnd )

    while True:
        win32gui.PumpWaitingMessages()
        time.sleep( 1 )
