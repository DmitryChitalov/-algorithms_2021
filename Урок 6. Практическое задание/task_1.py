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
from memory_profiler import memory_usage
from timeit import default_timer
from random import randint


def memory_time_profiler(func):
    def wrapper(*args, **kwargs):
        t1 = default_timer()
        mem1 = memory_usage()
        res = func(*args, **kwargs)
        mem2 = memory_usage()
        t2 = default_timer()
        print(f'Время выполнения {func.__name__}: {t2 - t1}\nИспользуемая память: {mem2[0] - mem1[0]} MiB')
        return res

    return wrapper


@memory_time_profiler
def loop_func(num):
    num_lst = list(range(num))
    for i in num_lst:
        return i


@memory_time_profiler
def gen_func(num):
    num_lst = list(range(num))
    for i in num_lst:
        yield i


loop_func(100000000)
gen_func(100000000)

"""
Генератор не расходует память и значительно превосходит итератор по скорости.
Время выполнения loop_func: 2.7369407
Используемая память: 1.4765625 MiB
Время выполнения gen_func: 0.2158857000000003
Используемая память: 0.0 MiB
"""

my_list = [randint(0, 1000) for i in range(30000)]


@memory_time_profiler
def check_clones(any_lst):
    return [el for el in any_lst if any_lst.count(el) == 1]


@memory_time_profiler
def check_clones2(any_lst):
    return filter(lambda x: any_lst.count(x) == 1, any_lst)


check_clones(my_list)
check_clones2(my_list)

"""
list comprehension в первом случае значительно проигрывает итератору во втором по времени и расходует немного меньше
памяти

Время выполнения check_clones: 4.5859068999999995
Используемая память: 0.0078125 MiB
Время выполнения check_clones2: 0.23011990000000004
Используемая память: 0.00390625 MiB
"""


class Worker:

    def __init__(self, name, surname, position, salary, bonus):
        self.__salary_dict = {'Зарплата': salary, 'Премия': bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = sum(self.__salary_dict.values())

    def get_total_income(self):
        print(f'Доход: {self._income}')


class WorkerOpt:
    __slots__ = ('name', 'surname', 'position', 'salary', 'bonus')

    def __init__(self, name, surname, position, salary, bonus):
        self.salary = salary
        self.bonus = bonus
        self.name = name
        self.surname = surname
        self.position = position


    def get_total_income(self):
        print(f'Доход: {self.salary + self.bonus}')


@memory_time_profiler
def worker_test():
    print('до оптимизации')
    worker1 = Worker('Roman', 'Kurdyukov', 'student', 100, 100)
    return worker1.get_total_income()


@memory_time_profiler
def worker_opt_test():
    print('после оптимизации')
    worker2 = WorkerOpt('Roman', 'Kurdyukov', 'student', 100, 100)
    return worker2.get_total_income()


if __name__ == '__main__':
    worker_test()
    worker_opt_test()

"""
до оптимизации
Доход: 200
Время выполнения worker_test: 0.2013568
Используемая память: 0.0078125 MiB

после оптимизации
Доход: 200
Время выполнения worker_opt_test: 0.2199354
Используемая память: 0.0 MiB

Время выполнения изначального кода и оптимизированного практически не отличаются,однако, инкремент памяти у 
оптимизированного равен 0 за счет использования slots 
"""
