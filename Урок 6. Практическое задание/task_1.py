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
from memory_profiler import profile
from random import randint
from logparselib import log_parse
import json

LOG = 'nginx_logs'
PARSED_LOG = 'nginx_logs_parsed'


def measure(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = func(*args, **kwargs)
        print(f'Результат работы {func.__name__} составил {default_timer() - start:10.5f}')
        return result

    return wrapper


class Class1_nonoptimized:
    def __init__(self, x=randint(0, 100), y=randint(0, 100)):
        self.X = x
        self.Y = y


class Class1_optimized:
    __slots__ = ('x', 'y')

    def __init__(self, x=randint(0, 100), y=randint(0, 100)):
        X = x
        Y = y


@measure
@profile
def func1_nonoptimized(cnt=1000):
    d = {x: Class1_nonoptimized() for x in range(cnt)}
    return d


@measure
@profile
def func1_optimized(cnt=1000):
    d = {x: Class1_optimized() for x in range(cnt)}
    return d


@measure
@profile
def func1_optimized2(cnt=1000):
    l = [Class1_optimized() for x in range(cnt)]
    return l


@measure
@profile
def func1_optimized3(cnt=1000):
    g = (Class1_optimized() for x in range(cnt))
    return g


@measure
@profile
def func2_nonoptimized():
    with open(LOG) as i, open(PARSED_LOG, 'w') as o:
        l = i.readlines()
        for line in l:
            pck = json.dumps(log_parse(line))
            o.write(pck)
    print(f'Парсинг завершен {func2_nonoptimized.__name__}')


@measure
@profile
def func2_optimized():
    with open(LOG) as i, open(PARSED_LOG, 'w') as o:
        line = i.readline()
        while line:
            pck = json.dumps(log_parse(line))
            o.write(pck)
            line = i.readline()
    print(f'Парсинг завершен {func2_optimized.__name__}')



if __name__ == '__main__':
    func1_nonoptimized(50000)  # не оптимизированный Increment = 11,9 MiB, время 12.7
    func1_optimized(50000)  # __slots__ = set(). Increment = 7.7 MiB, время 14.65
    func1_optimized2(50000)  # тоже + list вместо dict. Increment = 1.5 MiB, время 15.03
    func1_optimized3(50000)  # тоже + generator. Increment = 0, время 0.0025
    '''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^             
    По вышеприведенным примерам:
    - оптимизация по памяти существенна для ресурсоемких методов и функций.
    - по моему примеру лучший результат имеют более ресурсоемкие функции (генератор не учитываем)
    - но такой результат - частный случай. возможны и иные варианты
    - вариант с генератором даёт наилучшие результаты по времени и памяти, за счет "отложенного вычисления",
     но много где может быть применим
    '''

    func2_nonoptimized()    # без оптимизации:    Время 60, память 10МиБ
    func2_optimized()       # после оптимизации:  Время 72, память 0Миб
    '''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    По вышеприведенным примерам:
    - хороший результат по оптимизации памяти путем использования обработки лога построчным чтением.
    - в данном случае без сильной потери по скорости мы выиграли память.
    
    
    таким образом произведена оптимизация памяти по следующим методам:
    - применение атрибута __slots__
    - замена типа dict() на tuple() в качестве основного объекта обработки
    - замена циклов на генераторное выражение
    - сериализация json применена, но она требуется по смыслу алгоритма.
    - применение файла для последовательной обработки больших массивов
    - приведено всего 2 исходных алгоритма, однако 4 варианта оптимизации.
    
    главный вывод: при оптимизации следует соотнести выигрыш ресурса (память) с возможным 
    получением худших показателей по ресурсу (скорость). Прогноз следует проверять тестами'''

