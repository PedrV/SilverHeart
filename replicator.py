from winreg import *

path = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
filePath = 'C:\\Users\\User\\FilePath\\pgrm.exe'

# Try stock access rights with 64bits program to 64bit registry
try:
    key = OpenKey( HKEY_CURRENT_USER, path, 0, access=KEY_SET_VALUE )
    SetValue( key, 'Registry', REG_SZ, filePath )  # Registry = name of the sub_key to open
    CloseKey( key )
except FileNotFoundError:
    import platform

    bits = platform.architecture()[0]

    # detects the bitness of the computer and gives the proper additional right access
    # https://docs.microsoft.com/en-us/windows/desktop/WinProg64/accessing-an-alternate-registry-view
    if bits == '32bits':
        bits_access_right = KEY_WOW64_64KEY
    elif bits == '64bits':
        bits_access_right = KEY_WOW64_32KEY

    try:
        key = OpenKey( HKEY_CURRENT_USER, path, 0, access=KEY_SET_VALUE | bits_access_right )
        SetValue( key, 'registry', REG_SZ, filePath )
        CloseKey( key )
    except Exception as e:
        print( 'Excpetion: %s' % str( e ) )