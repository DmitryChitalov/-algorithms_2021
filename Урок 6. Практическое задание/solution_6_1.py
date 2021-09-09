import json
from memory_profiler import profile
from numpy import array
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

# Задача №1


@profile
def create_list_1(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst


@profile
def create_list_2(n):
    """
    Оптимизировали при помощи LC
    :param n:
    :return:
    """
    return [i for i in range(n)]


@profile
def create_list_3(n):
    """
    Оптимизация с помощью сериализации
    :param n:
    :return:
    """
    return json.dumps([i for i in range(n)])


# Задача №2


@profile
def func_1(value):
    return list(range(value))


@profile
def func_2(value):
    """
    Если требования к скрипту подразумевают последование обращение к
    элементам, то можно воспользоваться генератором
    :param value:
    :return:
    """
    return (i for i in range(value))


@profile
def func_3(value):
    """
    Через numpy наблюдаем экономию памяти более чем в два раза
    :param value:
    :return:
    """
    return array(range(value))


# Задача №3

@profile
def sum_digits(num, tmp=1.0, summ=0.0):
    return num < 0 and sum or sum_digits(num - 1, (tmp / 2) * -1, summ + tmp)


@profile
def sum_digits_1(num, tmp=1.0, summ=1.0):
    """
    Ушли от рекурсии к циклу, тем самым провели оптимизацию
    :param num:
    :param tmp:
    :param summ:
    :return:
    """
    for i in range(num):
        tmp = (tmp / 2) * -1
        summ += tmp
    return summ


class SumDigits:
    __slots__ = ['num', 'tmp', 'summ']

    def __init__(self, num, tmp, summ):
        self.num = num
        self.tmp = tmp
        self.summ = summ

    @profile
    def summary(self):
        """
        Оптимизация через слоты
        :return:
        """
        for i in range(self.num):
            self.tmp = (self.tmp / 2) * -1
            self.summ += self.tmp
        return self.summ


val = 10000
create_list_1(val)
create_list_2(val)
create_list_3(val)


func_1(val)
func_2(val)
func_3(val)


number = 3
sum_digits(number-1)

SD_OBJ = SumDigits(number-1, 1, 1)
SD_OBJ.summary()
