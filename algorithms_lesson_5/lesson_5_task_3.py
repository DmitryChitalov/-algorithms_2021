
from collections import deque
from timeit import timeit


# ЗАПОЛНЕНИЕ МАССИВА
def fill_deque():
    NEW_DEQUE = deque(i for i in range(1000))
    return NEW_DEQUE


def fill_list():
    NEW_LIST = [i for i in range(1000)]
    return NEW_LIST


fill_deque()
fill_list()
print('ЗАПОЛНЕНИЕ МАССИВА')
print(f'Time for fill_deque() is {timeit("fill_deque()", globals=globals())} seconds')
print(f'Time for fill_list() is {timeit("fill_list()", globals=globals())} seconds')
print('#########################################################################')


# ВСТАВКА ЭЛЕМЕНТА В КОНЕЦ МАССИВА
def deque_append(NEW_DEQUE):
    NEW_DEQUE.append('end')
    return NEW_DEQUE


def list_append(NEW_LIST):
    NEW_LIST.append('end')
    return NEW_LIST


# deque_append()
# list_append()
print('ВСТАВКА ЭЛЕМЕНТА В КОНЕЦ МАССИВА')
print(f'Time for deque_append() is {timeit("deque_append", globals=globals())} seconds')
print(f'Time for list_append is {timeit("list_append", globals=globals())} seconds')
print('#########################################################################')


# ВСТАВКА ЭЛЕМЕНТА В НАЧАЛО МАССИВА
def deque_append_left(NEW_DEQUE):
    NEW_DEQUE.appendleft('start')
    return NEW_DEQUE


def list_append_left(NEW_LIST):
    NEW_LIST.insert(0, 'start')
    return NEW_LIST


# deque_append_left()
# list_append_left()
print('ВСТАВКА ЭЛЕМЕНТА В НАЧАЛО МАССИВА')
print(f'Time for deque_append_left is {timeit("deque_append_left", globals=globals())} seconds')
print(f'Time for list_append_left is {timeit("list_append_left", globals=globals())} seconds')
print('#########################################################################')


# ИЗМЕНЕНИЕ ЭЛЕМЕНТОВ МАССИВА
def deque_change(NEW_DEQUE):
    for i, val in enumerate(NEW_DEQUE):
        val *= 2
    return NEW_DEQUE


def list_change(NEW_LIST):
    for i, val in enumerate(NEW_LIST):
        val *= 2
    return NEW_LIST


# deque_change()
# list_change ()
print('ИЗМЕНЕНИЕ ЭЛЕМЕНТОВ МАССИВА')
print(f'Time for deque_change is {timeit("deque_change", globals=globals())} seconds')
print(f'Time for list_change is {timeit("list_change", globals=globals())} seconds')


'''
ЗАПОЛНЕНИЕ МАССИВА
Time for fill_deque() is 95.4233148 seconds
Time for fill_list() is 55.027056400000006 seconds
#########################################################################
ВСТАВКА ЭЛЕМЕНТА В КОНЕЦ МАССИВА
Time for deque_append() is 0.03897370000001388 seconds
Time for list_append is 0.0362615999999889 seconds
#########################################################################
ВСТАВКА ЭЛЕМЕНТА В НАЧАЛО МАССИВА
Time for deque_append_left is 0.04233189999999354 seconds
Time for list_append_left is 0.04234639999998535 seconds
#########################################################################
ИЗМЕНЕНИЕ ЭЛЕМЕНТОВ МАССИВА
Time for deque_change is 0.03628380000000675 seconds
Time for list_change is 0.043528600000001916 seconds
ВЫВОД: Оба инструмента работают практически одинаково. В некоторых случаях 
(н-р, операция заполнения массива) list работает даже быстрее. При длине массива
100 элементов разница полностью исчезает. 
'''
