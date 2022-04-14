"""
Реализация программы подсчёта средней прибыли предприятий

1. Замена namedtuple на recordclass

Размер с использованием getsizeof(namedtuple) 56 байт.
Размер с использованием getsizeof(recordclass) 40 байт.
Размер с использованием asizeof(namedtuple) 144 байт.
Размер с использованием asizeof(recordclass) 672 байт.

Не смотря на то, что getsizeof показывает небольшое
преимущество по памяти у recordclass относительно namedtuple,
измерение размера полной структуры объектов с помощью asizeof
в связи с тем, что объект recordclass более сложный,
namedtuple занимает меньший объём памяти. Таким образом,
в данном случае использование recordclass не эффективно.
Recordclass остаётся хорошим вариантом в случае,
если необходимо изменять атрибуты класса в процессе
выполнения программы.

2. Удаление лишних ссылок на объекты

Удаляем ссылки на временную переменную firm
после заполнения данных о всех фирмах и
сиходный список firms после разделения его на
списки фирм с доходом больше и меньше среднего.
Результатом служит освобождение некоторого объёма
памяти до завершения выполнения функции.
Однако, в данном случае разница будет минимальна.

ункция average_firm_profit_1:
Использованная память: 0.01171875 Mib.

Функция average_firm_profit_2:
Использованная память: 0.0 Mib.
"""

from collections import namedtuple
from sys import getsizeof
from recordclass import recordclass
from pympler.asizeof import asizeof
from memory_profiler import profile
from task_1 import time_memo_prof

FIRM1 = namedtuple('Firm1', 'name year_income')
FIRM2 = recordclass('Firm2', 'name year_income')


@time_memo_prof
def average_firm_profit_1(count=2):

    average_profit = 0
    firms = []
    i = 1
    while i <= count:
        name = input(f'Введите название фирмы {i}: ')
        income = input('Введите прибыль предприятия за 4 квартала, через пробел: ').split()
        if len(income) != 4:
            print('Неверный ввод. Нужно ввести прибыль за 4 квартала.')
            continue

        try:
            income = sum(map(float, income))
        except ValueError:
            print('Неверные данные о доходе. Повторите попытку.')
            continue
        average_profit += income
        firm = FIRM1(
            name=name,
            year_income=income
        )
        firms.append(firm)
        i += 1

    average_profit = round(average_profit / count, 2)

    more = [f.name for f in firms if f.year_income > average_profit]
    less = [f.name for f in firms if f.year_income < average_profit]
    print(f'Средняя годовая прибыль предприятий {average_profit}\n'
          f'Фирмы с прибылью выше среднего: {", ".join(more)}\n'
          f'Фирмы с прибылью ниже среднего: {", ".join(less)}')


@time_memo_prof
def average_firm_profit_2(count=2):

    average_profit = 0
    firms = []
    i = 1
    while i <= count:
        name = input(f'Введите название фирмы {i}: ')
        income = input('Введите прибыль предприятия за 4 квартала, через пробел: ').split()
        if len(income) != 4:
            print('Неверный ввод. Нужно ввести прибыль за 4 квартала.')
            continue

        try:
            income = sum(map(float, income))
        except ValueError:
            print('Неверные данные о доходе. Повторите попытку.')
            continue
        average_profit += income
        firm = FIRM1(
            name=name,
            year_income=income
        )
        firms.append(firm)
        i += 1

    del firm

    average_profit = round(average_profit / count, 2)

    more = [f.name for f in firms if f.year_income > average_profit]
    less = [f.name for f in firms if f.year_income < average_profit]

    del firms

    print(f'Средняя годовая прибыль предприятий {average_profit}\n'
          f'Фирмы с прибылью выше среднего: {", ".join(more)}\n'
          f'Фирмы с прибылью ниже среднего: {", ".join(less)}')


if __name__ == '__main__':

    f1 = FIRM1(name='f1', year_income=12345)
    f2 = FIRM2(name='f2', year_income=12345)
    print(f'Размер с использованием getsizeof(namedtuple) {getsizeof(f1)} байт.')
    print(f'Размер с использованием getsizeof(recordclass) {getsizeof(f2)} байт.')
    print(f'Размер с использованием asizeof(namedtuple) {asizeof(f1)} байт.')
    print(f'Размер с использованием asizeof(recordclass) {asizeof(f2)} байт.')

    average_firm_profit_1()
    average_firm_profit_2()


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    50     31.2 MiB     31.2 MiB           1   @profile
    51                                         def average_firm_profit_1(count=2):
    52                                         
    53     31.2 MiB      0.0 MiB           1       average_profit = 0
    54     31.2 MiB      0.0 MiB           1       firms = []
    55     31.2 MiB      0.0 MiB           1       i = 1
    56     31.2 MiB      0.0 MiB           3       while i <= count:
    57     31.2 MiB      0.0 MiB           2           name = input(f'Введите название фирмы {i}: ')
    58     31.2 MiB      0.0 MiB           2           income = input('Введите прибыль предприятия за 4 квартала, через пробел: ').split()
    59     31.2 MiB      0.0 MiB           2           if len(income) != 4:
    60                                                     print('Неверный ввод. Нужно ввести прибыль за 4 квартала.')
    61                                                     continue
    62                                         
    63     31.2 MiB      0.0 MiB           2           try:
    64     31.2 MiB      0.0 MiB           2               income = sum(map(float, income))
    65                                                 except ValueError:
    66                                                     print('Неверные данные о доходе. Повторите попытку.')
    67                                                     continue
    68     31.2 MiB      0.0 MiB           2           average_profit += income
    69     31.2 MiB      0.0 MiB           4           firm = FIRM1(
    70     31.2 MiB      0.0 MiB           2               name=name,
    71     31.2 MiB      0.0 MiB           2               year_income=income
    72                                                 )
    73     31.2 MiB      0.0 MiB           2           firms.append(firm)
    74     31.2 MiB      0.0 MiB           2           i += 1
    75                                         
    76     31.2 MiB      0.0 MiB           1       average_profit = round(average_profit / count, 2)
    77                                         
    78     31.2 MiB      0.0 MiB           5       more = [f.name for f in firms if f.year_income > average_profit]
    79     31.2 MiB      0.0 MiB           5       less = [f.name for f in firms if f.year_income < average_profit]
    80     31.2 MiB      0.0 MiB           3       print(f'Средняя годовая прибыль предприятий {average_profit}\n'
    81     31.2 MiB      0.0 MiB           1             f'Фирмы с прибылью выше среднего: {", ".join(more)}\n'
    82     31.2 MiB      0.0 MiB           1             f'Фирмы с прибылью ниже среднего: {", ".join(less)}')


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    85     31.2 MiB     31.2 MiB           1   @profile
    86                                         def average_firm_profit_2(count=2):
    87                                         
    88     31.2 MiB      0.0 MiB           1       average_profit = 0
    89     31.2 MiB      0.0 MiB           1       firms = []
    90     31.2 MiB      0.0 MiB           1       i = 1
    91     31.2 MiB      0.0 MiB           3       while i <= count:
    92     31.2 MiB      0.0 MiB           2           name = input(f'Введите название фирмы {i}: ')
    93     31.2 MiB      0.0 MiB           2           income = input('Введите прибыль предприятия за 4 квартала, через пробел: ').split()
    94     31.2 MiB      0.0 MiB           2           if len(income) != 4:
    95                                                     print('Неверный ввод. Нужно ввести прибыль за 4 квартала.')
    96                                                     continue
    97                                         
    98     31.2 MiB      0.0 MiB           2           try:
    99     31.2 MiB      0.0 MiB           2               income = sum(map(float, income))
   100                                                 except ValueError:
   101                                                     print('Неверные данные о доходе. Повторите попытку.')
   102                                                     continue
   103     31.2 MiB      0.0 MiB           2           average_profit += income
   104     31.2 MiB      0.0 MiB           4           firm = FIRM1(
   105     31.2 MiB      0.0 MiB           2               name=name,
   106     31.2 MiB      0.0 MiB           2               year_income=income
   107                                                 )
   108     31.2 MiB      0.0 MiB           2           firms.append(firm)
   109     31.2 MiB      0.0 MiB           2           i += 1
   110                                         
   111     31.2 MiB      0.0 MiB           1       del firm
   112                                         
   113     31.2 MiB      0.0 MiB           1       average_profit = round(average_profit / count, 2)
   114                                         
   115     31.2 MiB      0.0 MiB           5       more = [f.name for f in firms if f.year_income > average_profit]
   116     31.2 MiB      0.0 MiB           5       less = [f.name for f in firms if f.year_income < average_profit]
   117                                         
   118     31.2 MiB      0.0 MiB           1       del firms
   119                                         
   120     31.2 MiB      0.0 MiB           3       print(f'Средняя годовая прибыль предприятий {average_profit}\n'
   121     31.2 MiB      0.0 MiB           1             f'Фирмы с прибылью выше среднего: {", ".join(more)}\n'
   122     31.2 MiB      0.0 MiB           1             f'Фирмы с прибылью ниже среднего: {", ".join(less)}')
"""
