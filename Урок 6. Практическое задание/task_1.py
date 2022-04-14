from numpy import array
import memory_profiler
from pympler import asizeof
from random import choice

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
"""
2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000

"""

print("Задание 1")


def decorator(func):
    def wrapper(*args, **kwargs):
        mem_1 = memory_profiler.memory_usage()
        res = func(*args, **kwargs)
        mem_2 = memory_profiler.memory_usage()
        mem_diff = mem_2[0] - mem_1[0]
        print("Результат", mem_diff)
        return res

    return wrapper


@decorator
def problem_1_1():
    cubes_of_numbers = []
    num = 1
    while num <= 100000:
        cubes_of_numbers.append(num ** 3)
        num += 1
    print(asizeof.asizeof(cubes_of_numbers))


@decorator
def problem_1_2():
    list_of_cubes = (num ** 3 for num in range(100000))
    print(asizeof.asizeof(list_of_cubes))


@decorator
def problem_1_3():
    list_of_cubes = array([num ** 3 for num in range(100000)])
    print(asizeof.asizeof(list_of_cubes))


problem_1_1()
problem_1_2()
problem_1_3()
# Результат 0.13671875
# Результат 0.02734375
# Результат 1.30078125
# Результат 0.02734375
"""
В данном задании нам необходимо создать список на 1000 элементов, 
я решила 1000000. Результаты оказались ожидаемыми: непрофилированное задание
занимает больше места, чем профилированное. Связано это конечно же
с методами управления памятью, такими как использование генераторов и модуля 
numpy
"""

"""
Задание 2 
Реализовать функцию get_jokes(),
возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
"""
print("\nЗадание 2")
nouns = ["программирование", "функциональный анализ", "комбинаторика", "линейная алгебра", "теория вероятности"]
verbs = ["заставляет", "обязует", "вынуждает", "любит", "ненавидит"]
infs = ["плакать", "любить", "жить", "грустить", "пить чай"]
"""
nouns: 680
verbs: 584
infs: 576

"""
print(asizeof.asizeof(nouns))
print(asizeof.asizeof(verbs))
print(asizeof.asizeof(infs))


def get_jokes(n):
    jokes = []
    for counter in range(n):
        noun, verb, inf = choice(nouns), choice(verbs), choice(infs)
        nouns.remove(noun)
        verbs.remove(verb)
        infs.remove(inf)
        jokes.append(noun + ' ' + verb + ' ' + inf)
    print(jokes)


get_jokes(3)
nouns_2 = array(
    ["программирование", "функциональный анализ", "комбинаторика", "линейная алгебра", "теория вероятности"])
verbs_2 = array(["заставляет", "обязует", "вынуждает", "любит", "ненавидит"])
infs_2 = array(["плакать", "любить", "жить", "грустить", "пить чай"])
print(asizeof.asizeof(nouns))
print(asizeof.asizeof(verbs))
print(asizeof.asizeof(infs))
"""
nouns_2: 344
verbs_2: 312
infs_2: 304

"""

"""
В этом задании нужно было использовать 3 списка. Аналогично с предыдущим
заданием я использовала numpy, и размер списков изменился в 2 раза в меньшую сторону

"""

"""
Задание 3

Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки.
Сформировать и вывести на экран фразы вида: 
'Привет, Игорь!' Подумать, как получить имена сотрудников 
из элементов списка, как привести их к корректному виду. 
Можно ли при этом не создавать новый список?

"""

print('\nЗадание 3')
list_1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for element in list_1:
    element = element.title()
    list_tmp = element.split()
    # print('Привет, {}!'.format(list_tmp[-1]))
print(asizeof.asizeof(list_1))
print(asizeof.asizeof(array(list_1)))
"""
Задание 3
616
600
"""
"""
метод array замечательно оптимизирует использование памяти
"""
