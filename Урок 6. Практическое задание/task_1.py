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

import memory_profiler
from timeit import default_timer
from pympler import asizeof


def memory_and_time(func):
    def wrapper(*args):
        mem_start = memory_profiler.memory_usage()
        start_time = default_timer()
        result = func(args[0])
        mem_stop = memory_profiler.memory_usage()
        mem_use = mem_stop[0] - mem_start[0]
        time_use = default_timer() - start_time
        print(f'Нагрузка на память: {mem_use}, потрачено времени: {time_use}')
        return result
    return wrapper


# Сравним классическую итерацию с "ленивым вычислением"
@memory_and_time
def min_value(lst):
    minimal_value = lst[0]
    for i in lst:
        if i < minimal_value:
            minimal_value = i
    return minimal_value


@memory_and_time
def min_value_two(lst):
    minimal_value = lst[0]
    for i in lst:
        if i < minimal_value:
            minimal_value = i
            yield minimal_value


need_list = [i for i in range(1000000)]
min_value(need_list)
min_value_two(need_list)

"""
Нагрузка на память: 0.0078125, потрачено времени: 0.1272548
Нагрузка на память: 0.0, потрачено времени: 0.1118133
По результатам видно что генератор выигрывает по памяти
"""


# Сделаем две ф-ции с переводом в числовой тип данных: классическую и через map
@memory_and_time
def app_list(lst):
    new_list = []
    for item in lst:
        new_list.append(int(item))
    return new_list


@memory_and_time
def mapped_list(lst):
    new_list = list(map(int, lst))
    return new_list


app_list(need_list)
mapped_list(need_list)

"""
Нагрузка на память: 6.76953125, потрачено времени: 0.17255720000000008
Нагрузка на память: 8.515625, потрачено времени: 0.14201830000000004
Как мы можем наблюдать, если нужно выиграть по времени - это метод через map, но если по памяти - классический for плюс
append
"""


# Теперь посмотрим на слоты и классику в ООП
class FullName:  # Полное имя человека

    def __init__(self, name, second_name, patronymic):
        self.name = name
        self.second_name = second_name
        self.patronymic = patronymic

    def show(self):
        return f'Мое ФИО: {self.second_name} {self.name} {self.patronymic}'


person_1 = FullName('Иван', 'Иванов', 'Иваныч')
print(asizeof.asizeof(person_1))  # Размер 600


class FullName2:

    __slots__ = ('name', 'second_name', 'patronymic')

    def __init__(self, name, second_name, patronymic):
        self.name = name
        self.second_name = second_name
        self.patronymic = patronymic

    def show(self):
        return f'Мое ФИО: {self.second_name} {self.name} {self.patronymic}'


person_2 = FullName2('Иван', 'Иванов', 'Иваныч')
print(asizeof.asizeof(person_2))  # Размер 320

"""
Как видим использование слотов в данном примере сокращает потребление памяти чуть ли не в два раза
"""
