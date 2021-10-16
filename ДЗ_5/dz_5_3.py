from collections import deque

# Заполнение списка
from timeit import timeit


def append_in_list():
    lst = []
    for el in range(1000):
        lst.append(el)
    return lst


# Заполнение deque
def append_in_deque():
    queue = deque()
    for el in range(1000):
        queue.append(el)
    return queue


# Вставка в начало списка
def insert_el2_list(lst: list):
    for el in range(1000, 2000):
        lst.insert(0, el)


# Вставка в начало deque
def insert_el2_deque(dequ: deque):
    for el in range(1000, 2000):
        dequ.appendleft(el)


# Удаление из начала списка
def pop_from_beg_list(lst: list):
    for _ in range(100):
        lst.pop(0)


# Удаление из начала deque
def pop_from_beg_deque(dequ: deque):
    for _ in range(100):
        dequ.popleft()


# Расширение списка слева
def left_extend_list(lst: list, new_lst: list):
    new_lst = new_lst + lst
    return new_lst


# Расширение deque слева
def left_extend_deque(dequ: deque, new_lst: list):
    for _ in range(1000):
        dequ.extendleft(reversed(new_lst))
    return dequ


TEST_COUNT = 100
ls = append_in_list()
deq = append_in_deque()
new_ls = list(range(10000, 20000))

print("Выполнение функции append_in_list занимает: ", timeit("append_in_list()", globals=globals(), number=TEST_COUNT),
      " сек.")
print("Выполнение функции append_in_deque занимает: ",
      timeit("append_in_deque()", globals=globals(), number=TEST_COUNT), " сек.")
print("Выполнение функции insert_el2_list занимает: ",
      timeit("insert_el2_list(ls)", globals=globals(), number=TEST_COUNT), " сек.")
print("Выполнение функции insert_el2_deque занимает: ",
      timeit("insert_el2_deque(deq)", globals=globals(), number=TEST_COUNT), " сек.")
print("Выполнение функции pop_from_beg_list занимает: ",
      timeit("pop_from_beg_list(ls)", globals=globals(), number=TEST_COUNT), " сек.")
print("Выполнение функции pop_from_beg_deque занимает: ",
      timeit("pop_from_beg_deque(deq)", globals=globals(), number=TEST_COUNT), " сек.")
print("Выполнение функции left_extend_list занимает: ",
      timeit("left_extend_list(ls, new_ls)", globals=globals(), number=TEST_COUNT), " сек.")
print("Выполнение функции left_extend_deque занимает: ",
      timeit("left_extend_deque(deq, new_ls)", globals=globals(), number=TEST_COUNT), " сек.")

"""
Выполнение функции append_in_list занимает:  0.003989199999999998  сек.
Выполнение функции append_in_deque занимает:  0.0038585999999999968  сек.
Выполнение функции insert_el2_list занимает:  1.9578316  сек.
Выполнение функции insert_el2_deque занимает:  0.00454510000000008  сек.
Выполнение функции pop_from_beg_list занимает:  0.1906005999999998  сек.
Выполнение функции pop_from_beg_deque занимает:  0.0003446000000000282  сек.
Выполнение функции left_extend_list занимает:  0.04657119999999981  сек.
Выполнение функции left_extend_deque занимает:  9.2345497  сек.

Добавление элементов конец списка и деки происходит быстро и на одном уровне.

Вставка элементов в начало последовательности для деки происходит также быстро как и 
вставка в конец, но заметно медленее вставка происходит для списка.

Такую же картину можно наблюдать и с удалением элементов из начала последовательности.

Расширение списка для деки не смотря на то, что она имеет встроенный метод, 
происходит очень медленно. А простое сложение списков (расширение списка слева)
происходит довольно быстро по сравнению с декой.
 """
