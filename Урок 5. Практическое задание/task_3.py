"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""
from collections import deque
import cProfile


def list_append_right(nums):
    need_list = []
    for num in nums:
        need_list.append(num)


def deque_append_right(nums):
    need_list = deque()
    for num in nums:
        need_list.append(num)


def list_append_left(nums):
    need_list = []
    for num in nums:
        need_list.insert(0, num)


def deque_append_left(nums):
    need_list = deque()
    for num in nums:
        need_list.appendleft(num)


def list_extend(nums):
    # так как у списка нет метода extendleft, просто меняем местами
    need_list = [num for num in range(100000)]
    nums.extend(need_list)


def deque_extend(nums):
    need_list = deque()
    need_list.extendleft(nums)


def list_pop_left(nums):
    need_list = []
    need_list.extend(nums)
    while need_list:
        need_list.pop(0)


def deque_pop_left(nums):
    need_list = deque()
    need_list.extend(nums)
    while need_list:
        need_list.popleft()


def main():
    numbers = [num for num in range(100000)]
    list_append_right(numbers)
    deque_append_right(numbers)
    list_append_left(numbers)
    deque_append_left(numbers)
    list_extend(numbers)
    deque_extend(numbers)
    list_pop_left(numbers)
    deque_pop_left(numbers)


cProfile.run('main()')

"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    4.536    4.536 <string>:1(<module>)
        1    0.010    0.010    0.015    0.015 task_3.py:18(list_append_right)
        1    0.010    0.010    0.015    0.015 task_3.py:24(deque_append_right)
        1    0.013    0.013    1.737    1.737 task_3.py:30(list_append_left)
        1    0.009    0.009    0.015    0.015 task_3.py:36(deque_append_left)
        1    0.000    0.000    0.003    0.003 task_3.py:42(list_extend)
        1    0.003    0.003    0.003    0.003 task_3.py:44(<listcomp>)
        1    0.000    0.000    0.001    0.001 task_3.py:48(deque_extend)
        1    0.030    0.030    2.715    2.715 task_3.py:53(list_pop_left)
        1    0.020    0.020    0.031    0.031 task_3.py:60(deque_pop_left)
        1    0.002    0.002    4.536    4.536 task_3.py:67(main)
        1    0.003    0.003    0.003    0.003 task_3.py:68(<listcomp>)
        1    0.000    0.000    4.536    4.536 {built-in method builtins.exec}
   100000    0.005    0.000    0.005    0.000 {method 'append' of 'collections.deque' objects}
   100000    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
   100000    0.005    0.000    0.005    0.000 {method 'appendleft' of 'collections.deque' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.001    0.001    0.001    0.001 {method 'extend' of 'collections.deque' objects}
        2    0.001    0.000    0.001    0.000 {method 'extend' of 'list' objects}
        1    0.001    0.001    0.001    0.001 {method 'extendleft' of 'collections.deque' objects}
   100000    1.724    0.000    1.724    0.000 {method 'insert' of 'list' objects}
   200000    2.684    0.000    2.684    0.000 {method 'pop' of 'list' objects}
   200000    0.010    0.000    0.010    0.000 {method 'popleft' of 'collections.deque' objects}
   
Из замеров можно сделать вывод что:
1) Если брать картину заполнения: если с конца - то одинаково, если с начала - дек значительно опережает список
2) По операции извлечения дек опять же обходит список в невероятное кол-во раз
"""