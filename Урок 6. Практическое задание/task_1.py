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

from memory_profiler import profile
import memory_profiler
from numpy import array
from pympler import asizeof
from timeit import timeit
from timeit import default_timer
from collections import OrderedDict


def decor(func):    # что-то мне тут не нравится
    def wrapper(*args, **kwargs):
        memory_start = memory_profiler.memory_usage()    # начало замера памяти
        time_start = default_timer()    # начало замера времени
        func(*args, **kwargs)    # начало замера функции (к которым декоратор стоит)
        time_diff = default_timer() - time_start    # окончание замера времени
        memory_end = memory_profiler.memory_usage()    # окончание замера памяти
        mem_diff = memory_end[0] - memory_start[0]
        return f'Выполнение заняло памяти: {mem_diff} MiB \n' \
               f'И времени: {time_diff} \n'

    return wrapper

# скрипт 1
# ДЗ-4, задание 3 (из имеющегося числа сформировать обратное число)
# взят свой вариант (по ТЗ), не преподавателя


number_cycles = 1000000
enter_number_1 = 159753
enter_number_2 = 159753    # вторая переменная, для отдельного вычсиления, чтобы функции не зависели друг от друга


@decor
def revers_1():    # вариант без изменений
    new_list = []
    num_position = 1
    for i in str(enter_number_2):
        new_list.insert(-num_position, i)
        num_position = num_position + 1
    # print(asizeof.asizeof(new_list))
    return new_list    # 400 байт


@decor
def revers_2():    # изменённый вариант
    new_list = [i for i in str(enter_number_1)]    # сипользование LC вместо цикла (ибо быстрее)
    new_list = reversed(new_list)    # размер 448 байт
    # new_list = array(new_list)    # для уменьшения размера списка - тогда порядка 112 байт,
    # но (!) сильно упадёт скорость работы по времени!
    # print(*[i for i in new_list])   # если использвать/распаковать список, то размер - 48 байт
    # print(asizeof.asizeof(new_list))
    return new_list    # 448 байт


# print(f'Заполнение: '
#       f'{timeit("revers_1()", globals=globals(), number=number_cycles)}')
# print(f'Заполнение: '
#       f'{timeit("revers_2()", globals=globals(), number=number_cycles)}')
print(revers_1())
print(revers_2())

"""при изменении памяти ивремени получаются в основном одинаковые результаты, 
однако, при вызове функций через timeit (без декоратора) выяснняется, что вторая функция на 20-30% быстрее.
так же во второй функции имеется недостаток - размер new_list - 448 байт (в первой он 400 байт),
при использовании array для "сжатия" существенно (!) упадёт время работы функции (но размер станет 112 байт). 
но, если во втором варианте выводить (print(*new_list) или производить иные действия 
(например [i for i in new_list] или цикл) с new_list, 
то размер составит 48 байт.
закоментированные строки кода не убирал, чтобы посмотреть/запустить с другими параметрами можно было"""

# скрипт 2
# ДЗ-3, задание 1. (заполнение списка и словаря программно, выполниние набора операций и со списком, и со словарем)
# порядок следования: сначала пример, затем его улучшенная часть

first_list = []
first_list_1 = []
first_dictionary = {}
first_dictionary_1 = {}
second_list = []
second_list_1 = []
second_dictionary = {}
second_dictionary_1 = {}
number_operations = 1000000


@decor    # начальный пример (создание списка)
def append_list(lst, x):    # Выполнение заняло памяти: 38.32421875 MiB, И времени: 0.12531329999910668
    for i in range(x):
        lst.append(i)
    # print(asizeof.asizeof(lst))
    # print('время заполнения списка - ')
    return lst    # размер 40448720 байт


@decor    # изменённая версия (создание списка)
def append_list_1(lst_1, x):    # Выполнение заняло памяти: 0.63671875 MiB, И времени: 0.10525219999544788
    lst_1 = lst_1 + ([i for i in range(x)])    # использование генератора помогает ускорить создание массива
    # print(asizeof.asizeof(lst_1))
    # print('время заполнения списка - ')
    return lst_1    # размер 40000048 байт


print(append_list(first_list, number_operations))    # начальный пример
print(append_list_1(first_list_1, number_operations))    # изменённая версия

"""append_list_1 использован генератор, вместо append сложение (в большинстве тестов оно работает быстрее)
по итогам размер массива стал меньше (40000048 против 40448720), 
использование памяти редко превышает допустимое значение,
выполнение по времени примерно на 10% быстрее"""


@decor    # начальный пример (создание словаря)
def append_dictionary(dictionary, x):    # Выполнение заняло памяти: 70.65234375 MiB, И времени: 0.14390649998676963
    for i in range(x):
        dictionary[i] = i
    # print('время заполнения словаря - ')
    # print(asizeof.asizeof(dictionary))
    return dictionary    # размер 73943128


@decor    # изменённая версия (создание словаря)
def append_dictionary_1(dictionary_1, x):    # Выполнение заняло памяти: 62.640625 MiB, И времени: 0.08110670000314713
    dictionary_1[(i for i in range(x))] = ({i for i in range(x)})
    # print('время заполнения словаря - ')
    # print(asizeof.asizeof(dictionary_1))
    return dictionary_1    # размер 65555296


print(append_dictionary(first_dictionary, number_operations))    # начальный пример
print(append_dictionary_1(first_dictionary_1, number_operations))    # изменённая версия

"""аналогичная ситуация со словарями в append_dictionary_1 - при применении LC
значительно выросла скорость заполнения (примерно вдвое), памяти требуется примерно на 10-16% меньше,
размер словаря стал 65555296 против 73943128"""


@decor    # начальный пример (копирование списка)
def operations_list(lst):    # Выполнение заняло памяти: 7.6484375 MiB, И времени: 0.11844799999380484
    for i in lst:
        second_list.append(i)
    # print('время копирования списка - ')
    # print(asizeof.asizeof(second_list))
    return second_list    # размер 40448720 байт


@decor    # изменённая версия (копирование списка)
def operations_list_1(lst, s_list):    # Выполнение заняло памяти: 0.00390625 MiB, И времени: 0.07205769998836331
    s_list = s_list + ([i for i in lst])
    # print('время копирования списка - ')
    # print(asizeof.asizeof(s_list))
    return s_list    # размер 40000048 байт


print(operations_list(first_list))    # начальный пример
print(operations_list_1(first_list, second_list_1))    # изменённая версия

"""как и в примерах выше, LC вновь выдаёт высокие результаты скорости - примерно в полтора раза,
и пониженное потребление памяти ()практичеки не выходит за пределы, 
размер списка уменьшился 40000048 против 40448720"""


@decor    # начальный пример (копирование словаря)
def operations_dictionary(dictionary):    # Выполнение заняло памяти: 40.34375 MiB, И времени: 0.2272960999980569
    for i in dictionary:
        second_dictionary[i] = dictionary[i]
    # print('время копирования словаря - ')
    # print(asizeof.asizeof(second_dictionary))
    return second_dictionary    # размер 73943128


@decor    # изменённая версия (копирование словаря)
def operations_dictionary_1(dictionary, s_dict):    # Выполнение заняло памяти: 31.7265625 MiB,
                                                    # И времени: 0.0817148000060115
    s_dict[(i for i in dictionary)] = ({i for i in dictionary})
    # print('время копирования словаря - ')
    # print(asizeof.asizeof(s_dict))
    # s_dict = array(s_dict)
    return s_dict    # размер 107498472


print(operations_dictionary(first_dictionary))    # начальный пример
print(operations_dictionary_1(first_dictionary, second_dictionary_1))    # изменённая версия

"""каки  в предыдущих примерах LC показал высокую скорость работы (примерно в три раза),
меньшее потребление памяти (в данном случае примерно на 20%).
единственный минус (может неправильно измерял) размер словаря гораздо больше, 
почти в полтора раза 107498472 против 73943128 (модуль array не помощет, проверил)"""

# скрипт 3
# ДЗ-5, задание 4
# Поработайте с обычным словарем и OrderedDict.
# Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры

dictionary_list = {}
dictionary_list_1 = {}
ordered_dict_list = OrderedDict({})
ordered_dict_list_1 = OrderedDict({})
number_fill = 1000


# неизменённый вариант
@decor
def fill_dictionary():    # заполнение словаря - заняло памяти: 0.11328125 MiB, времени 0.00037719999090768397
    dictionary_list = {i: i * i for i in range(number_fill)}
    return dictionary_list


@decor
def fill_ordered_dict():    # заполнение OrderedDict - заняло памяти: 0.08984375 MiB, времени: 0.0003403000009711832
    ordered_dict_list = {i: i * i for i in range(number_fill)}
    return ordered_dict_list


@decor
def search_key_1():    # ищем значение по ключу в словаре - заняло времени: 1.170000177808106e-05
    dictionary_list.get(1)
    return dictionary_list


@decor
def search_key_2():    # ищем значение по ключу в словаре (OrderedDict) - заняло времени: 1.200000406242907e-05
    ordered_dict_list.get(1)
    return ordered_dict_list


print(fill_dictionary(), '\n', fill_ordered_dict(), '\n',
      search_key_1(), '\n', search_key_2())


# изменённый вариант

@decor
def fill_dictionary_1():    # заполнение словаря Выполнение заняло памяти: 0.109375 MiB
                            # И времени: 0.00031010000384412706
                            # 0.1015625 MiB после array
    dictionary_list_1 = array({i: i * i for i in range(number_fill)})
    return dictionary_list_1    # 100408, осле array 112


@decor
def fill_ordered_dict_1():    # заполнение словаря OrderedDict Выполнение заняло памяти: 0.09765625 MiB
                              # И времени: 0.0003563000063877553
                              # 0.078125 MiB  после array
    ordered_dict_list_1 = array({i: i * i for i in range(number_fill)})
    return ordered_dict_list_1    # 100408, после array 112


@decor
def search_key_3():    # ищем значение по ключу в словаре И времени: 8.100003469735384e-06
                       # 1.0500021744519472e-05  после array
    dictionary_list_1.get(1)
    return dictionary_list_1


@decor
def search_key_4():    # ищем значение по ключу в словаре (OrderedDict) И времени: 1.179997343569994e-05
    ordered_dict_list_1.get(1)
    return ordered_dict_list_1


print(fill_dictionary_1(), '\n', fill_ordered_dict_1(), '\n',
      search_key_3(), '\n', search_key_4())

"""при использовании модуля array существенно уменьшился размер словаря - стал порядка 112, вместо 100480,
на время работы практически не повлияло (в пределах погрешности после нескольких измерений),
на дальнейшие вычисления (поиск по ключу) практически не влияет, кроме search_key_3,
там вероятно увеличение работы по времени порядка 10-20 процентов (бывает уменьшение,
поэтому, как вариант, это погрешность выполнения кода)"""
