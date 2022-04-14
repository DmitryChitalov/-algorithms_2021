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
from timeit import default_timer
from random import choice
from functools import reduce
from memory_profiler import memory_usage
from pympler.asizeof import asizeof
from collections import defaultdict

# Наш декоратор для замеров памяти и времени
def measurer(func):
    def wrapper(*args, **kwargs):
        start_mem, start_time = memory_usage()[0], default_timer()
        r = func(*args, **kwargs)
        mem, time = (memory_usage()[0] - start_mem), (default_timer() - start_time)
        return r, f'Использовано памяти: {mem}', f'Затрачено времени{time}'
    return wrapper


# Задача 1:
# Для начала возьмем задачу с рекурсией. Урок 2 задача 2: нам нужно найти количество четных и нечетных цифр в числе.
# Профилируем сначала рекурсивное решение, а потом перепишем задачу через цикл и опять же проведем замеры.
@measurer
def wrapper_odd_even_count1(num: int):
    def odd_even_count1(d=num, o=0, e=0):
        mod = d % 10
        if mod % 2 == 0:
            o += 1
        else:
            e += 1
        d_temp = d // 10
        if d_temp == 0:
            return f'Количество четных и нечетных цифр в числе равно: ({o}, {e})'
        return odd_even_count1(d=d_temp, o=o, e=e)
    return odd_even_count1()


@measurer
def odd_even_count2(d, o=0, e=0):
    while d > 0:
        if d % 2 == 0:
            o += 1
        else:
            e += 1
        d = d // 10
    return f'Количество четных и нечетных цифр в числе равно: ({o}, {e})'


num_1 = 1472583690547893342534363469896859688938673439770564568756795696724697469769746798705836587536
num_2 = 1472583690547893342534363469896859688938673439770564568756795696724697469769746798705836587536
print(wrapper_odd_even_count1(num_1))
print(odd_even_count2(num_2))

# Результаты:
# ('Количество четных и нечетных цифр в числе равно: (44, 50)', 'Использовано памяти: 0.125', 'Затрачено времени0.10925969999999999')
# ('Количество четных и нечетных цифр в числе равно: (44, 50)', 'Использовано памяти: 0.0', 'Затрачено времени0.10865599999999997')
# Вывод: как видно из замеров, по скорости цикл в данном случае не дал
# каких-то значительных приростов, но вот по памяти, циклы значительно выигрывают, и чем больше будет рекурсивных
# вызовов, тем больший прирост по памяти мы увидим.

# Задача 2:
# Задача с курса основ программирования: на вход подается список имен сотрудников,
# на выходе программа должна отдаль словарь, в котором ключом, будут первые буквы имени сотрудников,
# а значением список соответствующих сотрудников.
@measurer
def thesaurus1(*args) -> dict:
    names_dict = {}
    for name in args:
        if name[0] in names_dict:
            names_dict[name[0]].append(name)
        else:
            names_dict.setdefault(name[0], [name])
    return names_dict


# Второй вариант решения с использования defaultdict
@measurer
def thesaurus2(*args) -> dict:
    names_dict = defaultdict(list)
    for name in args:
        names_dict[name[0]].append(name)
    return names_dict


print(thesaurus1("Иван", "Мария", "Петр", "Илья"))
print(thesaurus2("Иван", "Мария", "Петр", "Илья"))
# Результаты
# ({'И': ['Иван', 'Илья'], 'М': ['Мария'], 'П': ['Петр']}, 'Использовано памяти: 0.01171875', 'Затрачено времени0.10980569999999998')
# (defaultdict(<class 'list'>, {'И': ['Иван', 'Илья'], 'М': ['Мария'], 'П': ['Петр']}), 'Использовано памяти: 0.00390625', 'Затрачено времени0.10909730000000001')
# Как мы видим, при использовании defaultdict мы не получаем значительного прироста по скорости исполнения кода,
# но немного выигрывает по использованию памяти. Да и код получается лаконичнее :)

# Задача 3:
# Задача с курса основ программирования: реализовать класс, который позволит валидировать вводимую дату
# и конвертировать ее в нужный формат.


class Data1:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def converter(cls, date: str):
        try:
            day, month, year = date.split('-')
            cls.validator(cls(day, month, year))
            return cls(day, month, year)
        except ValueError as e:
            print(e)

    @staticmethod
    def validator(obj):
        if 13 > int(obj.month) > 0 and len(obj.year) == 4 and 32 > int(obj.day) > 0:
            return True
        raise ValueError("Дата указана не верно!")


class Data2:
    __slots__ = ['day', 'month', 'year']
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def converter(cls, date: str):
        try:
            day, month, year = date.split('-')
            cls.validator(cls(day, month, year))
            return cls(day, month, year)
        except ValueError as e:
            print(e)

    @staticmethod
    def validator(obj):
        if 13 > int(obj.month) > 0 and len(obj.year) == 4 and 32 > int(obj.day) > 0:
            return True
        raise ValueError("Дата указана не верно!")


date1 = Data1.converter('12-12-2020')
date2 = Data2.converter('12-12-2020')
print(asizeof(date1))
print(asizeof(date2))

# Результаты:
# 488
# 224
# Для оптимизации по памяти использовал __slots__, что дало значительное улучшение в этом направлении