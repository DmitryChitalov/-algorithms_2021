from collections import deque
from timeit import timeit


my_lst = [i for i in range(100000)]
my_deque = deque(my_lst)
element = 5
a = [1, 2]


def append_left_deque(check_deque, el):
    check_deque.appendleft(el)


def pop_left_list(check_list):
    check_list.pop(0)


def pop_left_deque(check_deque):
    check_deque.popleft()


def append_left_list(check_list, el):
    check_list.insert(0, el)


def extend_left_list(check_list, el):
    for i in el:
        check_list.insert(0, i)


def extend_left_deque(check_deque, el):
    check_deque.extendleft(el)


def pop_list(check_list):
    check_list.pop()


def pop_deque(check_deque):
    check_deque.pop()


print('appendleft list')
print(timeit('append_left_list(my_lst, element)', globals=globals(), number=1000))

print('appendleft deque')
print(timeit('append_left_deque(my_deque, element)', globals=globals(), number=1000))

print('popleft list')
print(timeit('pop_left_list(my_lst)', globals=globals(), number=1000))

print('popleft deque')
print(timeit('pop_left_deque(my_deque)', globals=globals(), number=1000))

print('extendleft list')
print(timeit('extend_left_list(my_lst, a)', globals=globals(), number=100))

print('extendleft deque')
print(timeit('extend_left_deque(my_deque, a)', globals=globals(), number=100))

print('pop list')
print(timeit('pop_list(my_lst)', globals=globals(), number=100))

print('pop deque')
print(timeit('pop_deque(my_deque)', globals=globals(), number=100))

'''
Вывод
В ходе проведевения различныч операций с каждым из объектов, можно сказать, что встроенные в deque операции
работают в несколько раз быстрее, чем аналогичные в list, но при этом одинковые операции выполняются
с равными затратами времени
'''