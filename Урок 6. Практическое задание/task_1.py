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

from random import randint, choice
from memory_profiler import memory_usage
from timeit import default_timer
import json
from recordclass import recordclass

print('Выделение памяти до выполнения первого примера', memory_usage())


def my_dec(func):
    def wrapper(*args, **kwargs):
        memory = memory_usage()
        time = default_timer()
        a = func(*args, **kwargs)
        print(f'Время выполнения{default_timer() - time} и было выделено памяти {memory_usage()[0] - memory[0]} MiB')
        return a

    return wrapper


@my_dec
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr  # Время выполнения 0.0037 памяти выделено 0.76 MiB


@my_dec
def func_2(nums):
    return (i for i in range(len(nums)) if nums[i] % 2 == 0)  # меньшее время выполнения и выделение памяти 0.0 MiB


c = func_1([randint(0, 1000) for _ in range(50000)])
f = func_2([randint(1000, 99999) for _ in range(50000)])
print('Выделение памяти после выполнения первого примера', memory_usage())

"""
Использование генератора сильно экономит память при использовании больших масивов данных 
"""

print('Выделение памяти до выполнения второго примера', memory_usage())


@my_dec
def test_dict():
    return {i: i for i in range(50000)}  # Выполнение 0.0056 выделяет памяти 2.8MiB


@my_dec
def dict_json():
    a = {i: i for i in range(50000)}
    a = json.dumps(a)
    return a  # Выполнение 0.0215 выделяет памяти 1.007 MiB


a = test_dict()
b = dict_json()

print('Выделение памяти после выполнения второго примера', memory_usage())
"""
Если приходится хранить в памяти  допустим словари то после их использований
можно перевести в json и тем самым освободив большее количиство памяти но на это надо больше времени так как 
перевод в json занимает мощности 
"""

print('Выделение памяти до выполнения третьего  примера', memory_usage())


@my_dec
def test_1():
    literals = ('abcdefghjklmnopuqwertzxv')
    st = ''.join([literals[randint(0, 23)] if i % 10 != 0 else ' ' for i in range(100000)])
    result = [i for i in st.split() if i.endswith('q')]
    return result  # Время выполлнения 0.063 выделено памяти 1.11 MiB но данные меняются генерируется случайная строка


@my_dec
def test_2():
    literals = ('abcdefghjklmnopuqwertzxv')
    st = ''.join([literals[randint(0, 23)] if i % 10 != 0 else ' ' for i in range(100000)])
    result = [i for i in st.split() if i.endswith('q')]
    del literals
    del st
    return result  # Время выполлнения 0.062 выделено памяти 0.0 MiB


test_1()
test_2()
print('Выделение памяти после выполнения третьего примера', memory_usage())

"""
Стоит всегда удалять не нужные ссылки для более оптимального использования памяти и не хранения в ней
уже не нужной информации 
"""
