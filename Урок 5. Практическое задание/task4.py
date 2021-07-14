from collections import OrderedDict
from random import randint
from timeit import timeit

def fill_dict(n):
    d = dict()
    for i in range(n):
        d.update({randint(0,100):randint(1,5)})
    return d

def fill_od(n):
    d = OrderedDict()
    for i in range(n):
        d.update({randint(0,100):randint(1,5)})
    return d

print("Наполнение словаря: ")
print(timeit('fill_dict(100)', globals=globals(), number=1000))
print("Наполнение OD: ")
print(timeit('fill_dict(100)', globals=globals(), number=1000))

def popitem_d(d,item):
    del d[item]
    return d

def popitem_od(od, item):
    od.popitem(item)
    return od

d = fill_dict(100)
od = fill_od(100)

d.update({100:100})
od.update({100:100})
d.update({200:200})
od.update({200:200})

d = fill_dict(500)
od = fill_od(500)


print("Удаление элемента словаря: ")
print(timeit(f'popitem_d({d},100)', globals=globals(), number=1000))
print("Удаление элемента OD: ")
print(timeit(f'popitem_od({od},(100,100))', globals=globals(), number=1000))

def move_to_end_d(d, item):
    t_value = d[item]
    t_key = item
    del d[item]
    d.update({t_key: t_value})
    return d

def move_to_end_od(od, item):
    return od.move_to_end(item)

print("Перемещение элемента словаря в конец: ")
print(timeit(f'move_to_end_d({d}, 100)', globals=globals(), number=1000))
print("Перемещение элемента OD в конец: ")
print(timeit(f'move_to_end_od({od},100)', globals=globals(), number=1000))

print("Все операции описанные выше работают быстрее для обучного словаря")
print("Однако смысл использования OD есть, поскольку он \nболее эфетивен при работе с сортировкой элементов")
