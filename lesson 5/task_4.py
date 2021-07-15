"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
import collections
import timeit

test_dict = {}
def for_dict():
    for i in range(100):
        test_dict[i] = (i+2)
    return test_dict
#print(for_dict())

test_orderdict = collections.OrderedDict([])
def for_orderdict():
    for i in range(100):
        test_orderdict[i] = (i+2)
    return test_orderdict
#print(for_orderdict())

print('замеры по наполнению dict и OrderedDict')
print(
    timeit.timeit(
        "for_dict()",
        globals=globals(),
        number=100000))

print(
    timeit.timeit(
        "for_orderdict()",
        globals=globals(),
        number=100000))
new_dict = {}
def update_dict():
    for i in range(100):
        new_dict[i+100] = (i + 3)
        test_dict.update(new_dict)
    return test_dict
#print(update_dict())

new_orderdict = collections.OrderedDict([])
def update_orderdict():
    for i in range(100):
        new_orderdict[i+100] = (i + 3)
        test_orderdict.update(new_orderdict)
    return test_orderdict
#print(update_orderdict())
print(
    timeit.timeit(
        "update_dict()",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "update_orderdict()",
        globals=globals(),
        number=1000))
print('Повырезаем')

def popitem_dict():
    n = 0
    while n != 10:
        test_dict.popitem()
        n += 1
    return test_dict
#print(popitem_dict())

def popitem_orderdict():
    n = 0
    while n != 10:
        test_orderdict.popitem()
        n += 1
    return test_orderdict
# print(popitem_orderdict())
print(
    timeit.timeit(
        "update_dict()",
        globals=globals(),
        number=10))
print(
    timeit.timeit(
        "update_orderdict()",
        globals=globals(),
        number=10))
"""
На момент создания и до версии 3.6 OrderedDict имел право на существование.
На новых версиях он проигрывает словарям.
Смысла использовать OrderedDict в Python выше 3.6 нет
"""
