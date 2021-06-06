"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
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
import time
import memory_profiler
import json
from pympler import asizeof
from random import randint


def space_time(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start = time.time()
        res = func(args[0])
        end = time.time()
        m2 = memory_profiler.memory_usage()
        mem_difference = m2[0] - m1[0]
        time_difference = end - start
        return res, mem_difference, time_difference

    return wrapper


@space_time
def test1(arr):
    for i in range(len(arr)):
        arr[i] = str(arr[i])
    return arr


@space_time
def test_map(arr):
    return list(map(str, arr))


print('')
test_arr = [i * 2 for i in range(1000000)]

res_test1, mem_difference, time_difference = test1(test_arr)
print(f'Выполнение заняло {mem_difference} Mib, {"%.4f" % time_difference} секунд.')

res_test_map, mem_difference, time_difference = test_map(test_arr)
print(f'Выполнение заняло {mem_difference} Mib, {"%.4f" % time_difference} секунд.')
#  Выполнение заняло 31.0078125 Mib, 0.2962 секунд.
#  Выполнение заняло 6.54296875 Mib, 0.1196 секунд.
#  функция test_map оптимизирована при помощи встроенной функции 'map' и требует меньше памяти и меньше времени


@space_time
def get_list(n):
    return [i for i in range(n)]


@space_time
def get_dict(n):
    return {key: key for key in range(n)}


res_list, mem_difference, time_difference = get_list(1000000)
print(f'Выполнение заняло {mem_difference} Mib, {"%.4f" % time_difference} секунд.')

res_dict, mem_difference, time_difference = get_dict(1000000)
print(f'Выполнение заняло {mem_difference} Mib, {"%.4f" % time_difference} секунд.')

# Выполнение заняло 38.63671875 Mib, 0.0515 секунд.
# Выполнение заняло 71.0546875 Mib, 0.0918 секунд.
# Создание списка и словаря. Тут на создание словаря расходуется больше памяти и времени.


def fill_dict():
    dict = {12: 13}
    i = 10000
    while i != 0:
        dict[randint(10, 100)] = randint(10, 100)
        i -= 1
    return dict


dumped_dict = json.dumps(fill_dict())

print('Размер dict: ', asizeof.asizeof(fill_dict()))
print('Размер json: ', asizeof.asizeof(dumped_dict))

# Размер dict:  7608
# Размер json:  960
# Использовав сериализацию, сокращаем размер словаря в несколько раз


@space_time
def func_1(n):
    new_arr = []
    for i in range(len(n)):
        if n[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# меняем цикл на list comprehension:
@space_time
def func_2(n):
    return [i for i, n in enumerate(n) if n % 2 == 0]


res_func_1, mem_difference, time_difference = func_1(list(range(9999999)))
print(f'Выполнение заняло {mem_difference} Mib, {"%.4f" % time_difference} секунд.')

res_func_2, mem_difference, time_difference = func_2(list(range(9999999)))
print(f'Выполнение заняло {mem_difference} Mib, {"%.4f" % time_difference} секунд.')

# Выполнение заняло 193.54296875 Mib, 1.1236 секунд.
# Выполнение заняло 193.09375 Mib, 1.0186 секунд.
# Время выполнения через list comprehension меньше
