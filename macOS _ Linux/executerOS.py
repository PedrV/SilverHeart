import multiprocessing as mp

import keeperOS
import logger

if __name__ == '__main__':
    p1 = mp.Process( target=keeperOS.keeperOS )
    p2 = mp.Process( target=loggerOS.loggerOS )
    p1.start()
    p2.start()
    p1.join()
    p2.join()
