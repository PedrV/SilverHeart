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
