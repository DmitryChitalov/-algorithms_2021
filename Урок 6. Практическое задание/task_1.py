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
import random, string, json
from memory_profiler import profile, memory_usage
from timeit import default_timer
from numpy import array


def decor(func):
    """Функция декортатор для замеров времени и памяти"""

    def wrapper(*args, **kwargs):
        t1 = default_timer()
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        t2 = default_timer()
        mem_diff = m2[0] - m1[0]
        time_dif = t2 - t1
        print(f'Функция - {func.__name__}\n Время заняло: {time_dif}\n Памяти заняло:{mem_diff}\n\n')
        return res

    return wrapper


def generate_random_string(length):
    """Генератор рандомной строки"""
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def key_gen():
    """Генератор инжекса элемента"""
    yield random.randint(1, 10000)


# @profile
@decor
def filling_list_cycle(num_of_el):
    my_list = []
    for i in range(num_of_el):
        my_list.append(i)
    return my_list


@decor
def filling_list(num_of_el):
    return [i for i in range(num_of_el)]


@decor
def search_in_list(my_list):
    arr = []
    for i in range(10000):
        key = random.randint(1, 10000)
        arr.append(my_list.index(key))
    return arr


@decor
def search_in_list_with_key_gen(my_list):
    arr = []
    for i in range(10000):
        for key in key_gen():
            arr.append(my_list.index(key))
    return arr


@decor
def hash_substrings(s):
    return [hash(s[i:j]) for i in range(len(s)) for j in range(i + 1, len(s) + 1)]


@decor
def hash_substrings_json(s):
    return json.dumps([hash(s[i:j]) for i in range(len(s)) for j in range(i + 1, len(s) + 1)])


@decor
def eratosthenes_numpy(n):
    sieve_list = n * 100  # Для создания достаточно большого листа для сита
    sieve = array([num for num in range(sieve_list + 1)])
    i = 2  # Начинем перебор с индекса 2
    while i <= sieve_list:  # O(logN)
        if sieve[i] != 0:
            s = i + i
            while s <= sieve_list:
                sieve[s] = 0
                s += i
        i += 1

    result = sorted(list(set(sieve)))
    result.remove(0)
    return result[n]


@decor
def eratosthenes(n):
    sieve_list = n * 100  # Для создания достаточно большого листа для сита
    sieve = [num for num in range(sieve_list + 1)]
    i = 2  # Начинем перебор с индекса 2
    while i <= sieve_list:  # O(logN)
        if sieve[i] != 0:
            s = i + i
            while s <= sieve_list:
                sieve[s] = 0
                s += i
        i += 1

    result = sorted(list(set(sieve)))
    result.remove(0)
    return result[n]


"""функции наполнения и поиска из 3-го урока"""
num_of_el = 1000000
my_list = filling_list_cycle(num_of_el)
my_list = filling_list(num_of_el)
search_in_list(my_list)
search_in_list_with_key_gen(my_list)

"""функции хэш из 3-го урока"""
s = generate_random_string(1000)
# print(f'Рандомная строка: {s}')

hash_substrings(s)
hash_substrings_json(s)


"""решето эратосфена"""

eratosthenes(100000)
eratosthenes_numpy(100000)

"""
1. Функции наполнения листа через цикл:
Функция - filling_list_cycle
 Время заняло: 0.32463429999999993
 Памяти заняло:19.21875

Функция реализованная с помощью спискового фключения выполняется быстрее и занимаеет немного меньше памяти:
Функция - filling_list
 Время заняло: 0.2653430000000001
 Памяти заняло:19.17578125

*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

2 .функции поиска элемента в листе:
Функция - search_in_list
 Время заняло: 0.9183887
 Памяти заняло:0.171875

Функция с использованием генератора (функция с yield) занимает меньше времени и использует меньше памяти:
Функция - search_in_list_with_key_gen
 Время заняло: 0.8612773
 Памяти заняло:0.0
 
 */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
 
3.Функции с хэш:
 Функция - hash_substrings
 Время заняло: 0.7208751000000002
 Памяти заняло:12.265625

Функция использующая для хранения json использует немного дольше по времени, но значительно меньше занимает памяти:
Функция - hash_substrings_json
 Время заняло: 0.7964286999999999
 Памяти заняло:4.9375
 
 */*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/ 
 
4.Функции решето Эратосфена:
Функция - eratosthenes
 Время заняло: 6.7860336000000006
 Памяти заняло:1.125


Функция решета с использованием массива из библиотеки numpy занимает гораздо меньше памяти, но продолжителнее по времени
Функция - eratosthenes_numpy
 Время заняло: 11.0538552
 Памяти заняло:0.25390625
"""
