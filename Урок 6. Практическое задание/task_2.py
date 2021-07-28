"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""
from collections import defaultdict
from prof import my_profile
from memory_profiler import profile
import pandas as pd

# По непонятной причине, вообще ничего не было сказано о pandas dataframe. А ведь если что-то нужно считать по многим
# записям с идентичными полями - ничего лучше просто не найти. Да, есть named tuples, но они хороши для единичных
# все же записей

"""
1.	Имеются данные предприятий, их наименования, страна и прибыль
Программа должна определить и вывести среднюю прибыль, 
вывести три страныс наибольшим кол-вом компаний в списке и отдельно
вывести наименования 10 самых крупных предприятий
"""


# для начала сделаем наивную реализацию
@my_profile
def best_of_list(_list):
    incomes = []
    countries = defaultdict(int)
    companies = defaultdict(float)
    for sublist in _list:
        incomes.append(float(sublist[2].replace(',', '.')))
        countries[sublist[1]] += float(sublist[2].replace(',', '.'))
        companies[sublist[0]] = float(sublist[2].replace(',', '.'))
    return f'Средняя прибыль равна: {sum(incomes) / len(incomes):.02f}', \
           f'Страны с наибольшим кол-вом компаний в списке: {", ".join([x for x in countries.keys() if countries[x] in sorted(list(countries.values()), reverse=True)[:3]])}', \
           f'Топ-10 предприятий: {", ".join([x for x in companies.keys() if companies[x] in sorted(companies.values(), reverse=True)[:10]])}'


# Profiling:       <best_of_list>  RSS:  20.48kB | VMS:       0B | time:   0.53ms ('Средняя прибыль равна: 21.00',
# 'Страны с наибольшим кол-вом компаний в списке: United States, Japan, Taiwan', 'Топ-10 предприятий: Samsung
# Electronics, Apple, Hewlett-Packard, Hitachi, IBM, Panasonic, Hon Hai Precision, Sony, Toshiba, Microsoft')
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    24     55.7 MiB     55.7 MiB           1   @profile
    25                                         def best_of_list(_list):
    26     55.7 MiB      0.0 MiB           1       incomes = []
    27     55.7 MiB      0.0 MiB           1       countries = defaultdict(int)
    28     55.7 MiB      0.0 MiB           1       companies = defaultdict(float)
    29     55.7 MiB      0.0 MiB         133       for sublist in _list:
    30     55.7 MiB      0.0 MiB         132           incomes.append(float(sublist[2].replace(',', '.')))
    31     55.7 MiB      0.0 MiB         132           countries[sublist[1]] += float(sublist[2].replace(',', '.'))
    32     55.7 MiB      0.0 MiB         132           companies[sublist[0]] = float(sublist[2].replace(',', '.'))
    33     55.7 MiB      0.0 MiB           2       return f'Средняя прибыль равна: {sum(incomes) / len(incomes):.02f}', \
    34     55.7 MiB      0.0 MiB          25              f'Страны с наибольшим кол-вом компаний в списке: {", ".join([x for x in countries.keys() if countries[x] in sorted(list(countries.values()), reverse=True)[:3]])}', \
    35     55.7 MiB      0.0 MiB         135              f'Топ-10 предприятий: {", ".join([x for x in companies.keys() if companies[x] in sorted(companies.values(), reverse=True)[:10]])}'
"""


# из-за небольшого размера файла в формате csv, предусмотренных в коде оптимизаций результат и так неплох. Попробуем
# Pandas
@my_profile
def best_of_list_pd(_csv):
    df = pd.read_csv(_csv, names=('comp', 'country', 'revenue'), decimal=',', delimiter=';')
    return f'Средняя прибыль равна: {df["revenue"].mean():.02f}', f'Страны с наибольшим кол-вом компаний в списке: ' \
                                                                  f'{", ".join(df["country"].value_counts()[:3].index.to_list())}', \
           f"Топ-10 предприятий: {', '.join(df.sort_values(by='revenue', ascending=False)['comp'][:10].values.tolist())}"


# Profiling:    <best_of_list_pd>  RSS:   10.16KB | VMS: 1.62B | time:   0.14ms
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    62     85.9 MiB     85.9 MiB           1   @profile
    63                                         def best_of_list_pd(_csv):
    64     86.3 MiB      0.4 MiB           1       df = pd.read_csv(_csv, names=('comp', 'country', 'revenue'), decimal=',', delimiter=';')
    65     86.5 MiB      0.1 MiB           3       return f'Средняя прибыль равна: {df["revenue"].mean():.02f}', f'Страны с наибольшим кол-вом компаний в списке: ' \
    66     86.5 MiB      0.1 MiB           1              f'{", ".join(df["country"].value_counts()[:3].index.to_list())}', \
    67     86.5 MiB      0.1 MiB           1              f"Топ-10 предприятий: {', '.join(df.sort_values(by='revenue', ascending=False)['comp'][:10].values.tolist())}"
('Средняя прибыль равна: 21.00', 'Страны с наибольшим кол-вом компаний в списке: United States, Japan, Taiwan', 'Топ-10 предприятий: Samsung Electronics, Apple, Hewlett-Packard, Hitachi, IBM, Panasonic, Hon Hai Precision, Sony, Toshiba, Microsoft')
"""

# Существенного прироста в производительности и памяти мы не получили за счет малого массива данных. Но если бы
# массив был большим, были бы другие цифры. Хотя и так видно. Кроме того, код отличается легкостью и простотой Я
# использую pandas на всех крупных таблицах, где кол-во элементов превышает 1000 - 10000000 шт и прирост скорости
# просто фантастический
#######################################################################################################################
"""Говоря об общих принципах(механизмах), ДОБАВИЛ бы следующие(то, чего не услышал на уроке)
 - При чтении файла лучше читать только то что реально нужно, а не все подряд(ленивое чтение)
 - Вызов функции - это долго, всякую мелочь нужно писать inline
 - создание объектов занимает время
 - использовать ссылки на объекты быстрее, чем копировать их содержимое
 Ну и есть более продвинутые технологии, вроде асинхрона и многопоточности для нагруженных проектов
 Также есть проекты автоматической оптимизации кода, но все они ограничены ОП и пока далеки от свободного применения"""

if __name__ == '__main__':
    with open('Книга2.csv', encoding='utf-8-sig') as f:
        comp = []
        for m in f:
            comp.append([m.split(';')[0].strip(), m.split(';')[1].strip(), m.split(';')[2].strip()])
    print(best_of_list(comp))
    print(best_of_list_pd('Книга2.csv'))
