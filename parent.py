import win32con
import win32api
import win32gui
import sys
import time
#
# def log_info(msg):
#     """ Prints """
#     print (msg)
#     f = open("C:\\Users\Pedro Vieira-PC\PycharmProjects\KeyLogger\\venv\Include\Key.txt", "a")
#     f.write(msg + "\n")
#     f.close()
#
# def wndproc(hwnd, msg, wparam, lparam):
#     log_info("wndproc: %s" % msg)
#
# if __name__ == "__main__":
#     log_info("*** STARTING ***")
#     hinst = win32api.GetModuleHandle(None)
#     wndclass = win32gui.WNDCLASS()
#     wndclass.hInstance = hinst
#     wndclass.lpszClassName = "testWindowClass"
#     messageMap = { win32con.WM_QUERYENDSESSION : wndproc,
#                    win32con.WM_ENDSESSION : wndproc,
#                    win32con.WM_QUIT : wndproc,
#                    win32con.WM_DESTROY : wndproc,
#                    win32con.WM_CLOSE : wndproc }
#
#     wndclass.lpfnWndProc = messageMap
#
#
#     try:
#         myWindowClass = win32gui.RegisterClass(wndclass)
#         hwnd = win32gui.CreateWindowEx(win32con.WS_EX_LEFT,
#                                      myWindowClass,
#                                      "testMsgWindow",
#                                      0,
#                                      0,
#                                      0,
#                                      win32con.CW_USEDEFAULT,
#                                      win32con.CW_USEDEFAULT,
#                                      win32con.HWND_MESSAGE,
#                                      0,
#                                      hinst,
#                                      None)
#     except Exception:
#         print("Exception")
#
#     if hwnd is None:
#         log_info( "hwnd is none!" )
#     else:
#         log_info( "hwnd: %s" % hwnd )
#
#     while True:
#         win32gui.PumpWaitingMessages()
#         time.sleep( 1 )

def log_info(msg):
     """ Prints """
     print (msg)
     f = open("C:\\Users\User\Key.txt", "a")
     f.write(msg + "\n")
     f.close()

def wndproc(hwnd, msg, wparam, lparam):
    log_info("wndproc: %s" % msg)


class MyWindow:
    log_info("***STARTING***")
    def __init__(self):
        win32gui.InitCommonControls()
        self.hinst = win32api.GetModuleHandle(None)
        className = 'MyWndClass'
        message_map = { win32con.WM_QUERYENDSESSION : wndproc,
                        win32con.WM_ENDSESSION : wndproc,
                        win32con.WM_QUIT : wndproc,
                        win32con.WM_DESTROY : wndproc,
                        win32con.WM_CLOSE : wndproc,
                        win32con.CTRL_C_EVENT : wndproc,
        }
        wc = win32gui.WNDCLASS()
        wc.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        wc.lpfnWndProc = message_map
        wc.lpszClassName = className
        win32gui.RegisterClass(wc)
        style = win32con.WS_OVERLAPPEDWINDOW
        self.hwnd = win32gui.CreateWindow(
            className,
            'My win32api app',
            style,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            300,
            300,
            300,
            0,
            self.hinst,
            None
        )
        win32gui.UpdateWindow(self.hwnd)
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOW)


w = MyWindow()
win32gui.PumpMessages()