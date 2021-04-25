"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import random
from timeit import default_timer as t


# 1) сложность O(N log N)
def find_top_three(dct):
    dct_sort = sorted(dct.items(), key=lambda el: el[1])[:-4:-1]
    return [el[0] for el in dct_sort]


# 2) сложность O(n)
def find_top_three1(dct):
    lst_company = [el for el in dct.keys()]
    lst_proceed = [el for el in dct.values()]
    rez = []
    for i in range(3):
        max_proceed = max(lst_proceed)
        idx = lst_proceed.index(max_proceed)
        rez.append(lst_company[idx])
        lst_company.pop(idx)
        lst_proceed.pop(idx)
    return rez


data_proceeds = {'Intel': 33, 'AMD': 10, 'IBM': 13, 'Apple': 31, 'Microsoft': 21, 'Google': 41, 'Yandex': 44}

print(find_top_three(data_proceeds))
print(find_top_three1(data_proceeds))
'''Не смотря на более объемный код второе решение эффективнее за счет меньшей сложности алгоритма, что подтверждается 
тестами ниже'''

if __name__ == '__main__':
    lst = random.sample(range(10**7), 10**5)
    lst1 = random.sample(range(10**7), 10**5)
    test_data = dict(zip(lst, lst1))

    start = t()
    find_top_three(test_data)
    end = t()
    print(end - start)

    start = t()
    find_top_three1(test_data)
    end = t()
    print(end - start)
