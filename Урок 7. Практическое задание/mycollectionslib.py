from collections import deque
from itertools import islice

class sdeque(deque):
    def __getitem__(self, index):
        if isinstance(index, slice):
            return type(self)(islice(self, index.start,
                                               index.stop, index.step))
        return super().__getitem__(self, index)

if __name__ == '__main__':
    print('Custom type "sdeque" realized...')
    print('Usage: from mycollectionslib import sdeque')
    exit(0)
