"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict as od
from timeit import timeit


class DictVSOderedDict:

    def __init__(self, size):
        self.dct = {}
        self.odct = od()
        self.size = size

    def fill_dict(self):
        for i in range(self.size):
            self.dct[i] = i

    def fill_odict(self):
        for i in range(self.size):
            self.odct[i] = i

    def show_dict_items(self):
        for key, val in self.dct.items():
            if int(key) % 10 == 0:
                print()
            print(f"{key:>5}:{val:>5}", end='\t')

    def show_odict_items(self):
        for key, val in self.odct.items():
            if int(key) % 10 == 0:
                print()
            print(f"{key:>5}:{val:>5}", end='\t')

    def write_dict_items_to_file(self, filename: str):
        with open(filename, mode='w', encoding='utf-8') as f:
            for key, val in self.dct.items():
                if int(key) % 10 == 0:
                    f.write('\n')
                f.write(f"{key:>5}:{val:>5}\t")

    def write_odict_items_to_file(self, filename: str):
        with open(filename, mode='w', encoding='utf-8') as f:
            for key, val in self.odct.items():
                if int(key) % 10 == 0:
                    f.write('\n')
                f.write(f"{key:>5}:{val:>5}\t")

    def pop_dict(self, keys: list):
        for key in keys:
            self.dct.pop(key)

    def pop_odict(self, keys: list):
        for key in keys:
            self.odct.pop(key)


if __name__ == '__main__':
    battle = DictVSOderedDict(10000)
    dict_file = 'dct.txt'
    odict_file = 'odct.txt'

    print(f"Fill dict time: "
          f"{timeit('battle.fill_dict()', number=1000, globals=globals())}")

    print(f"Fill ordered dict time: "
          f"{timeit('battle.fill_odict()', number=1000, globals=globals())}")

    print(f"Show elements of the dict time: "
          f"{timeit('battle.write_dict_items_to_file(dict_file)', number=1000, globals=globals())}")

    print(f"Show elements of the ordered dict time: "
          f"{timeit('battle.write_odict_items_to_file(odict_file)', number=1000, globals=globals())}")

    keys_dct = list(battle.dct.keys())
    print(f"Pop elements of the dict time: "
          f"{timeit('battle.pop_dict(keys_dct)', number=1, globals=globals())}")

    keys_odct = list(battle.odct.keys())
    print(f"Pop elements of the ordered dict time: "
          f"{timeit('battle.pop_odict(keys_odct)', number=1, globals=globals())}")

"""
Fill dict time: 0.5122118
Fill ordered dict time: 0.9826965000000001
Show elements of the dict time: 7.6706311000000005
Show elements of the ordered dict time: 8.084804899999998
Pop elements of the dict time: 0.0007030999999990684
Pop elements of the ordered dict time: 0.001321900000000653

Fill dict time: 0.508626
Fill ordered dict time: 0.9801002999999999
Show elements of the dict time: 7.703318
Show elements of the ordered dict time: 8.1342484
Pop elements of the dict time: 0.0007145999999984554
Pop elements of the ordered dict time: 0.0013319999999978904

Fill dict time: 0.5139958
Fill ordered dict time: 0.9917861
Show elements of the dict time: 7.7828919
Show elements of the ordered dict time: 8.1589096
Pop elements of the dict time: 0.0007260000000002265
Pop elements of the ordered dict time: 0.0013684000000004914

Во всех проведённых операциях OrderedDict оказался медленнее, при этом dict в полной мере выполняет тот же функционал.
Таким образом, нет особого смысла использовать OrderedDict в современных версиях python. Более того, по полученным 
данным получается, что стоит даже избегать использования OrderedDict.
"""
