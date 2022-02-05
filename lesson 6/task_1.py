"""
Задание 1.
Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

print('Задание 1: создать список элементов из нечетных чисел')
from memory_profiler import profile
from collections import deque

@profile
def fun_1():
    nums = 100000
    lst = []
    for num in range(nums):
        if num % 2 != 0:
            lst.append(num)
    return lst

fun_1()

@profile
def fun_2():
    nums = 100000
    lst2 = []
    my_gen = (num for num in range(1, nums + 1, 2))
    for i in my_gen:
        lst2.append(i)
    return lst2

fun_2()
"""
nums = 10
fun_1: 0 MiB
fun_2: 0 MiB

nums = 100000
fun_1: 2,2 MiB
fun_2: 1,7 MiB

Генератор на больших числах позволит нам использовать меньше памяти
"""


print('Поработаем с коллекциями, оценим их затраты на память\n'
      'Задание 2: оценить методы списка и методы коллекций')

@profile
def insert_lst():
    test_list = []
    nums = 100000
    for i in range(1, nums):
        test_list.insert(0, i)
    return test_list

insert_lst()

@profile
def appendleft_deque():
    test_deque = deque()
    nums = 100000
    for i in range(1, nums):
        test_deque.appendleft(i)
    return test_deque

appendleft_deque()
"""
nums = 10
insert_lst: 0 MiB
appendleft_deque: 0 MiB

nums = 100000
insert_lst: 4,5 MiB
appendleft_deque: 3,6 MiB

По моим замерам коллекция deque выигрывает по памяти у стандартных методов списка
"""

print('Задание 3: Необходимо реверсировать список')
@profile
def def_reversed():
    my_lst = []
    nums = 100000
    for i in range(nums):
        my_lst.append(i)
    #print(my_lst)
    lst_obj = list(reversed(my_lst))
    return lst_obj

def_reversed()


@profile
def def_reverse():
    my_lst = []
    nums = 100000
    for i in range(nums):
        my_lst.append(i)
    my_lst.reverse()
    return my_lst

def_reverse()

"""
nums = 10
def_reversed: 0 MiB
def_reverse: 0 MiB

nums = 100000
insert_lst: 5,3 MiB
def_reverse: 3,9 MiB

reverse экономит память, но надо помнить, что он не подойдет, 
если надо сохранить исходные данные"""
