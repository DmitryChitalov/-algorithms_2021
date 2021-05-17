"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

# Здесь код из 4 примера домашнего задания к 4 уроку. Необходимо определить число,
# которое встречается в массиве чаще всего


from random import randint
from collections import Counter
import memory_profiler
import timeit


def decor(func):
    def wrapper(*args):
        start_time = timeit.default_timer()
        m1 = memory_profiler.memory_usage()
        res1, res2 = func(args[0])
        m2 = memory_profiler.memory_usage()
        end_time = timeit.default_timer()

        return res1, res2, m2[0] - m1[0], end_time - start_time
    return wrapper


@decor
def func_1(array):

    arr_value = []
    arr_count = []
    for el in array:
        if el not in arr_value:
            count2 = array.count(el)
            arr_value.append(el)
            arr_count.append(count2)

    max_2 = max(arr_count)
    elem = arr_value[arr_count.index(max_2)]

    return elem, max_2


@decor
def func_2(array):
    arr_value = []
    arr_count = []
    for el in array:
        if el not in arr_value:
            count2 = array.count(el)
            arr_value.append(el)
            arr_count.append(count2)

    max_2 = max(arr_count)
    elem = arr_value[arr_count.index(max_2)]

    del arr_value
    del arr_count
    del count2

    return elem, max_2


@decor
def func_3(array):
    arr_value = Counter(array)

    return arr_value.most_common(1)[0][0], arr_value.most_common(1)[0][1]


lst = [randint(1, 20) for i in range(1000)]

# func_1 - это исходный вариант функции
el, el_count, mem_diff, exec_time = func_1(lst)
print(f'Чаще всего встречается число {el}, оно появилось в массиве {el_count} раз(а)')
print(f'func_1. Использовано {mem_diff} Mib памяти')
print('func_1', exec_time)

# func_2 - в конце функции перед return добавил удаление созданных объектов
el, el_count, mem_diff, exec_time = func_2(lst)
print(f'Чаще всего встречается число {el}, оно появилось в массиве {el_count} раз(а)')
print(f'func_2. Использовано {mem_diff} Mib памяти')
print('func_2', exec_time)

# func_3 - подключил Counter из collections
el, el_count, mem_diff, exec_time = func_3(lst)
print(f'Чаще всего встречается число {el}, оно появилось в массиве {el_count} раз(а)')
print(f'func_3. Использовано {mem_diff} Mib памяти')
print('func_3', exec_time)

# Признаться, не понимаю, почему в третьем варианте использование памяти = 0?? Ведь
# созданный объект Counter имеет объем и при завершении функции я его не удаляю
# Ну и, кстати, Counter существенного выигрыша в скорости не дает, только лаконичность кода

# Чаще всего встречается число 12, оно появилось в массиве 65 раз(а)
# func_1. Использовано 0.0078125 Mib памяти
# func_1 0.22022609999999998

# Чаще всего встречается число 12, оно появилось в массиве 65 раз(а)
# func_2. Использовано 0.0 Mib памяти
# func_2 0.22209540000000005

# Чаще всего встречается число 12, оно появилось в массиве 65 раз(а)
# func_3. Использовано 0.0 Mib памяти
# func_3 0.22236290000000003
