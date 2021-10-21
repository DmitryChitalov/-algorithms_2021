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
from memory_profiler import memory_usage, profile
from pympler import asizeof


def my_profile(function):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        start_memory = memory_usage()
        res = function(*args, **kwargs)
        end_time = default_timer()
        end_memory = memory_usage()
        return end_time - start_time, end_memory[0] - start_memory[0], res

    return wrapper


class Worker:
    def __init__(self, name, surname, work, wage):
        self.name = name
        self.surname = surname
        self.work = work
        self.wage = wage


class WorkerSlots:
    __slots__ = ('name', 'surname', 'work', 'wage')

    def __init__(self, name, surname, work, wage):
        self.name = name
        self.surname = surname
        self.work = work
        self.wage = wage


worker_1 = Worker('Name_1', 'Surname_1', 'Work_1', 10000)
worker_slots_1 = WorkerSlots('Name_2', 'Surname_2', 'Work_2', 10000)
print(f'Worker: {asizeof.asizeof(worker_1)}')
print(f'WorkerSlots: {asizeof.asizeof(worker_slots_1)}')
print('При использовании вместо словаря кортежа для хранения атрибутов класса память значительно экономится\n')


@my_profile
def list_pow(start_list):
    return [el * el for el in start_list]


@my_profile
def list_pow_map(start_list):
    return map(lambda x: x * x, start_list)


print(f'list_pow = {list_pow(list(range(10000)))[0]} сек.\n'
      f'memory = {list_pow(list(range(10000)))[1]}')
print(f'list_pow_map = {list_pow_map(list(range(10000)))[0]} сек.\n'
      f'memory = {list_pow_map(list(range(10000)))[1]}')
print('map() экономит память т.к. возвращает итератор\n')


@profile
def func_1(my_list):
    original_list = [item * 2 for item in my_list]
    new_list = original_list
    del original_list
    return new_list


@profile
def func_2(my_list):
    original_list = [item * 2 for item in my_list]
    new_list = original_list
    del original_list
    del new_list
    new_list = []
    return new_list


test_list = list(range(100000))
func_1(test_list)
func_2(test_list)
print('Удаление всех ссылок на один и тот же объект освобождает память')
