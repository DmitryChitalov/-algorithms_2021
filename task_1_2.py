from sys import getsizeof
from random import randint
from collections import namedtuple
from recordclass import recordclass
import memory_profiler
from timeit import default_timer

with open('task_1_2.txt', 'w+', encoding='utf-8') as file:
    for i in range(1000):
        file.write(f'{i}, {randint(0, 100)} {randint(0, 100)} {randint(0, 100)} {randint(0, 100)}\n')


def decor(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        result = func(*args)
        m2 = memory_profiler.memory_usage()
        mem_usage = m2[0] - m1[0]
        run_time = default_timer() - start_time
        return result, mem_usage, run_time
    return wrapper


@decor
def main_tuple_file():
    company = namedtuple('Company', ('name', 'profit'))
    company_ls = []
    with open('task_1_2.txt', encoding='utf-8', errors='ignore') as inf:
        for line in inf:
            row = line.split(',')
            name = row[0]
            profit_sum = sum(map(int, row[1].split()))
            company_ls.append(company(name=name, profit=profit_sum))
        inf.seek(0)
        counter = len(inf.readlines())
    print(f'Объём занимаемой одним объектом namedtuple: {getsizeof(company)}')
    print(f'Объём занимаемой объектом namedtuple: {getsizeof(company_ls)}')
    average = sum(c.profit for c in company_ls) / counter
    # print(f'Средняя годовая прибыль всех предприятий: {average}')
    # print(
    #     f'Предприятия, с прибылью выше среднего значения: '
    #     f'{" | ".join([company.name for company in company_ls if company.profit > average])}')
    # print(
    #     f'Предприятия, с прибылью ниже среднего значения: '
    #     f'{" | ".join([company.name for company in company_ls if company.profit < average])}')


@decor
def main_record_file():
    company = recordclass('Company', ('name', 'profit'))
    company_ls = []
    with open('task_1_2.txt', encoding='utf-8', errors='ignore') as inf:
        for line in inf:
            row = line.split(',')
            name = row[0]
            profit_sum = sum(map(int, row[1].split()))
            company_ls.append(company(name=name, profit=profit_sum))
        inf.seek(0)
        counter = len(inf.readlines())
    print(f'Объём занимаемой одним объектом recordclass: {getsizeof(company)}')
    print(f'Объём занимаемой объектом recordclass: {getsizeof(company_ls)}')
    average = sum(c.profit for c in company_ls) / counter
    # print(f'Средняя годовая прибыль всех предприятий: {average}')
    # print(
    #     f'Предприятия, с прибылью выше среднего значения: '
    #     f'{" | ".join([company.name for company in company_ls if company.profit > average])}')
    # print(
    #     f'Предприятия, с прибылью ниже среднего значения: '
    #     f'{" | ".join([company.name for company in company_ls if company.profit < average])}')


@decor
def main_dict_file():
    company = dict()
    with open('task_1_2.txt', encoding='utf-8', errors='ignore') as inf:
        for line in inf:
            row = line.split(',')
            company[row[0]] = sum(map(int, row[1].split()))
    counter = len(company)
    print(f'Объём занимаемой объектом dict: {getsizeof(company)}')
    average = sum(company.values()) / counter
    # print(f'Средняя годовая прибыль всех предприятий: {average}')
    # print(
    #     f'Предприятия, с прибылью выше среднего значения: '
    #     f'{" | ".join([company.name for company in company_ls if company.profit > average])}')
    # print(
    #     f'Предприятия, с прибылью ниже среднего значения: '
    #     f'{" | ".join([company.name for company in company_ls if company.profit < average])}')


if __name__ == '__main__':
    res_1, mem_diff_1, runtime_1 = main_tuple_file()
    res_2, mem_diff_2, runtime_2 = main_record_file()
    res_3, mem_diff_3, runtime_3 = main_dict_file()

    print(f"Выполнение через namedtuple заняло {mem_diff_1} Mib и {runtime_1} секунд")
    print(f"Выполнение через recordclass заняло {mem_diff_2} Mib и {runtime_2} секунд")
    print(f"Выполнение через dict заняло {mem_diff_3} Mib и {runtime_3} секунд")


"""
Немного переработал код по namedtuple и для увеличения объёма информации реализовал чтение
из файла. На выходе получил: 
- для 100 записей
    Выполнение через namedtuple заняло 0.02734375 Mib и 0.1007574 секунд
    Выполнение через recordclass заняло 0.02734375 Mib и 0.10051779999999999 секунд
    Выполнение через dict заняло 0.0078125 Mib и 0.10161640000000005 секунд

При этом метод getsizeof() на 1000 записей показал вот такую цифру:
    Объём занимаемой объектом namedtuple: 920
    Объём занимаемой объектом recordclass: 920
    Объём занимаемой объектом dict: 4696

- для 1000 записей
    Выполнение через namedtuple заняло 0.27734375 Mib и 0.10876629999999998 секунд
    Выполнение через recordclass заняло 0.0390625 Mib и 0.10532409999999992 секунд
    Выполнение через dict заняло 0.046875 Mib и 0.10196260000000001 секунд

При этом метод getsizeof() на 1000 записей показал вот такую цифру:
    Объём занимаемой объектом namedtuple: 8856
    Объём занимаемой объектом recordclass: 8856
    Объём занимаемой объектом dict: 36960

Получается, что переменные namedtuple recordclass занимают одинаковое количество памяти.
Объём занимаемой одним объектом namedtuple: 896 байт
Объём занимаемой одним объектом recordclass: 896 байт

И при этом и namedtuple, и recordclass, экономнее dict.
"""