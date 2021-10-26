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
import os
import django
from collections import defaultdict
import sys
import timeit
import numpy
import random
from pympler import asizeof
import json


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        tm1 = timeit.default_timer()
        res = func(*args)
        m2 = memory_profiler.memory_usage()
        tm2 = timeit.default_timer()
        res_diff = m2[0] - m1[0]
        res_time = tm2 - tm1
        return res, str(res_diff) + ' Mib ', str(res_time) + ' time ', \
               str(sys.getsizeof(res)) + ' bytes', asizeof.asizeof(res)
    return wrapper


@decor
def static_info():
    """ Выполнение заняло 0.00390625 Mib, генератор освободил память на два порядка
    до генератора с обычным return было 0.10546875 Mib, а время уменьшилось в 16 раз
    """
    root_dir = django.__path__[0]
    result_dict = defaultdict(int)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            result_dict[size] += 1
    # return result_dict
    for i in result_dict.items():
        yield i


# if __name__ == '__main__':
#     print(static_info())


# 11.1
class Data:
    """
    К сожалению после использования слотов заняло 0.25454 Mib, но до использования
    слотов было 0.21818 Mib, я не понимаю почему
    """
    __slots__ = ['day', 'month', 'year']

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def parsing_info(cls, data):
        d, m, y = (int(el) for el in data.split('-'))
        return cls(d, m, y)

    @staticmethod
    def chek_info(obj):
        if obj.month == 2:
            if obj.day > 28:
                raise ValueError(f'The day in February is incorrectly entered: {obj.day}')
        if (31 < obj.day or obj.day < 0) or (12 < obj.month or obj.month < 0) or (6666 < obj.year):
            raise ValueError(f'Date entered incorrectly: {obj.day}-{obj.month}-{obj.year}')


work_str = '02-02-2021'
if __name__ == '__main__':
    one = Data.parsing_info(work_str)
    print(sys.getsizeof(one))
    print(asizeof.asizeof(one))
    """ 
    без слотов: 
    sys.getsizeof(one) - 48
    asizeof.asizeof(one) - 384
    с использованием слотов:
    sys.getsizeof(one) - 56
    asizeof.asizeof(one) - 120
    Вопрос чемотличается getsizeof от asizeof? они оба возвращают размер обекта в байтах 
    написанно что asizeof возвращает комбинированный размер но если ему верить то слоты 
    дают значительный прирост в свободной памяти
    """
    try:
        Data.chek_info(one)
    except ValueError as err:
        print(err)
    else:
        print(f'This good date: {work_str}')


# 5.4
""" в данном примере я сипользовал модуль numpy, получившееся рзультат таков что дли list_generation
модуль освобождает 20% памяти, для list_comprehension в 4 раза меньше места занимает, сериалтзация 
не многим лучше numpy разница в 2 байта в моём пимере
"""

src = [random.randint(0, 100) for _ in range(10000)]
list_generation_1 = (el for i, el in enumerate(src) if el > src[i - 1] and i > 0)
list_comprehension_1 = [el for i, el in enumerate(src) if el > src[i - 1] and i > 0]
# print(sys.getsizeof(list_generation_1))
# print(sys.getsizeof(list_comprehension_1))
# print()
list_generation_2 = numpy.array((el for i, el in enumerate(src) if el > src[i - 1] and i > 0))
list_comprehension_2 = numpy.array([el for i, el in enumerate(src) if el > src[i - 1] and i > 0])
list_json_1 = json.dumps(list_comprehension_1)
# print(sys.getsizeof(list_generation_2))
# print(sys.getsizeof(list_comprehension_2))
# print(sys.getsizeof(list_json_1))


@decor
def wrap_revers(el):
    """ Использование среза, вместо рекурсии дало уменьшеие используемой памяти
            в данном примере где el = 12045350 рекурсия =  0.0078125 Mib срез = 0.00390625 Mib
    """
    if not isinstance(el, str):
        el = str(el)
    return el[::-1]
    # def reverse_number(el, result=''):
    #     param = el % 10
    #     result += str(param)
    #     el //= 10
    #     if el == 0:
    #         return result
    #     return reverse_number(el, result)
    # return reverse_number(el)


# if __name__ == '__main__':
#     print(wrap_revers(12045350))

@decor
def wrap_arithmetic(n):
    def arithmetic_progression(count, term=0):
        """
        рекурсия = (382375, '0.83203125 Mib ', '0.10935564900000005 time ', '28 bytes'), заменил на
        цикл = (382375, '0.0078125 Mib ', '0.10950047499999993 time ', '28 bytes')
        результат не впечетляет но теперь можно считать любую прогрессию, раньшетолько до 1000
        :param count:
        :param res_sum:
        :param term:
        :return: sum arithmetic progression
        """
        for i in range(count+1):
            term += i
        return term
    #     term += 1
    #     if term == count:
    #         return term
    #     else:
    #         return term + arithmetic_progression(count, term)
    return arithmetic_progression(n)


# if __name__ == '__main__':
#     n = 874
#     print(wrap_arithmetic(n))
#     if wrap_arithmetic(n)[0] == n*(n+1)/2:
#         print('The formula is correctly')
#     else:
#         print('The formula is wrong')

""" Вывод: самый эффективный способ использование генератора занимает мало места
и скорость очень хорошая из минусов он одноразовый, хорошо показала себя сериализация и модуль numpy
дает хороший прирост в памяти, слоты показали обратное - но скорее всего это я накосячил,
не использовал модуль recordclass, map 
"""