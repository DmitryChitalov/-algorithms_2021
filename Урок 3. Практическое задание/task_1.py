"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
# import timeit
import time
import random


def measure_time():
    starts = time.time()
    # time.sleep(1)
    stop = time.time()
    return str((stop - starts)) + ' мсек'


# print(measure_time())
# a)
starts_l = time.time()
lst = [random.randint(0, 9999) for i in range(50000)]
stop_l = time.time()
print(stop_l - starts_l, 'мсек создания списка\n')
# print(lst)
print()
starts_d = time.time()
dct = {f'{i}': random.randint(0, 9999) for i in range(50000)}
stop_d = time.time()
print(stop_d - starts_d, 'мсек создания словаря\n')
# print(dct)
print()
print((stop_d - starts_d) - (stop_l - starts_l), 'разница во времени создания списка и словаря\n')

# read / in
starts_l = time.time()
print(564 in lst)
stop_l = time.time()
print(stop_l - starts_l, 'мсек')
starts_d = time.time()
print('564' in dct)
stop_d = time.time()
print(stop_d - starts_d, 'мсек')
print((stop_d - starts_d) - (stop_l - starts_l), 'разница во времени in\n')

# insert
starts_l = time.time()
lst.insert(123, '0123')
stop_l = time.time()
print(stop_l - starts_l, 'мсек')
starts_d = time.time()
dct.setdefault('0123', 123)
stop_d = time.time()
print(stop_d - starts_d, 'мсек')
print((stop_d - starts_d) - (stop_l - starts_l), 'разница во времени insert\n')

# pop
starts_l = time.time()
lst.pop(123)
stop_l = time.time()
print(stop_l - starts_l, 'мсек')
starts_d = time.time()
dct.pop('0123')
stop_d = time.time()
print(stop_d - starts_d, 'мсек')
print((stop_d - starts_d) - (stop_l - starts_l), 'разница во времени pop\n')

# remove
starts_l = time.time()
lst.remove(124)
stop_l = time.time()
print(stop_l - starts_l, 'мсек')
starts_d = time.time()
dct.popitem()
stop_d = time.time()
print(stop_d - starts_d, 'мсек')
print((stop_d - starts_d) - (stop_l - starts_l), 'разница во времени remove\n')

starts_l = time.time()
print(564 in lst)
lst.insert(123, '0123')
lst.pop(123)
lst.remove(124)
stop_l = time.time()
print(stop_l - starts_l, 'мсек')


starts_d = time.time()
print('564' in dct)
dct.setdefault('0123', 123)
dct.pop('0123')
dct.popitem()
stop_d = time.time()
print(stop_d - starts_d, 'мсек')

print((stop_d - starts_d) - (stop_l - starts_l), 'разница во времени')


# start = timeit.timeit()
# print("hello")
# time.sleep(10**-3)
# end = timeit.timeit()
# print(end - start)
