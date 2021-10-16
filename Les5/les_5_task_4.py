from collections import OrderedDict
from timeit import timeit
od = OrderedDict([])
my_dict = {}


def dict_test_1():
    for i in range(1000):
        my_dict[i] = i + 1


def od_test_1():
    for i in range(1000):
        od[i] = i + 1


def dict_test_2():
    for i in range(1000):
        a = my_dict[i]


def od_test_2():
    for i in range(1000):
        a = od[i]


print("=====================")
print(f"Dict result: {timeit('dict_test_1()', setup='from __main__ import dict_test_1, my_dict', number=10000)}")
print(f"OrderedDict result: {timeit('od_test_1()', setup='from __main__ import od_test_1, od', number=10000)}")
print("#########")
print(f"Dict result: {timeit('dict_test_2()', setup='from __main__ import dict_test_2, my_dict', number=10000)}")
print(f"OrderedDict result: {timeit('od_test_2()', setup='from __main__ import od_test_2, od', number=10000)}")
print("=====================")

"""Мои тесты показали, что эти словари почти не отличаются(0.8234461000000001 vs 1.0738919999999998) в выполнении самых распространённых задач, а именно добавление элементов и взятие элементов по ключу, но в OrderedDict есть полезные методы, которые пригодятся для выполнения специфических заданий."""
