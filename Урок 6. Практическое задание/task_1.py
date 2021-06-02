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

from memory_profiler import memory_usage, profile
from timeit import default_timer
from collections import namedtuple

def memory_time_profiler(func):
    def wraper(*args):
        memory = memory_usage()
        timer = default_timer()
        result = func(*args)
        memory = memory_usage()[0] - memory[0]
        timer = default_timer() - timer
        print(f'Время выполнения: {timer}\nИспользуемая память: {memory}')
        return result
    return wraper

@profile
def add_firm(count_firm):
    all_company = []
    for el in range(count_firm):
        name = input('Введите название фирмы')
        profits_srt = input('Введите через пробел прибыль данного предприятия за каждый квартал: ')
        profits = profits_srt.split()
        if len(profits) != 4:
                print('Вы ввели либо мало, либо много значений')
                continue
        try:
            average_profit = (int(profits[0]) + int(profits[1]) + int(profits[2]) + int(profits[3])) / 4
            firm_tuple = Firm_template(name_firm=name,
                                       average_profit_firm=average_profit)
            all_company.append(firm_tuple)
        except ValueError:
            print('Вы ввели не правильное значение прибыли!!!')
            continue
    return all_company

@profile
def aver_profit(all_company):
    average_profit_all_firm = 0
    average_profit_less = []
    average_profit_more = []
    for el in all_company:
        average_profit_all_firm = average_profit_all_firm + el.average_profit_firm
    average_profit_all_firm = average_profit_all_firm / len(all_company)
    print(f'Средняя годовая прибыль всех предприятий: {average_profit_all_firm}')
    for el in all_company:
        if el.average_profit_firm >= average_profit_all_firm:
            average_profit_more.append(el.name_firm)
        else:
            average_profit_less.append(el.name_firm)
    print(f'Предприятия, с прибылью выше среднего значения: {average_profit_more}')
    print(f'Предприятия, с прибылью ниже среднего значения: {average_profit_less}')


Firm_template = namedtuple('Firm_Profit', 'name_firm average_profit_firm')
try:
    count_firm = int(input('Введите количество предприятий для расчета прибыли: '))
    aver_profit(add_firm(count_firm))
except ValueError:
    print('Вы ввели не число!!!')

