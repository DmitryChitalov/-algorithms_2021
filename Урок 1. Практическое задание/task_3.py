"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

import operator
import time
from collections import OrderedDict

# Хранилище с информацией о компаниях: название и годовая прибль.
top_companies_by_profit = {
    'Alphabet': 34343,
    'JPMorgan Chase & Co.': 36431,
    'Saudi Aramco': 88211,
    'Agricultural Bank of China': 30701,
    'Industrial & Commercial Bank of China': 45195,
    'Microsoft': 39240,
    'Berkshire Hathaway': 81417,
    'Apple': 55256,
    'Bank of America Corp.': 27430,
    'China Construction Bank': 38610
} # значения указаны в миллионах долларов США по состоянию за 2019 год

# Решение № 1
def find_top3_1(dictobj: dict[str, int]) -> dict[str, int]:
    """Function sorts the dictionary by values.

    The complication of function is O(N^2).
    """

    sorted_values = sorted(dictobj.values(), reverse=True)
    sorted_dict = {}

    for i in sorted_values:
        for k in dictobj.keys():
            if dictobj[k] == i and len(sorted_dict) < 3:
                sorted_dict[k] = dictobj[k]
                break
    return sorted_dict


# Решение № 2
def find_top3_2(dictobj: dict[str, int]) -> dict[str, int]:
    """Function sorts the dictionary by values.

    The complication of function is O(N).
    """

    sorted_tuples = sorted(dictobj.items(), key=operator.itemgetter(1), reverse=True)
    top_3 = sorted_tuples[:3]
    sorted_dict = {k: v for k, v in top_3}
    return sorted_dict


# Решение № 3
def find_top3_3(dictobj: dict[str, int]) -> dict[str, int]:
    """Function sorts the dictionary by values.

    The complication of function is O(N*logN).
    """
    sorted_dict = {}
    sorted_keys = sorted(dictobj, key=dictobj.get, reverse=True)
    top_3 = sorted_keys[:3]
    for w in top_3:
        sorted_dict[w] = dictobj[w]
    return sorted_dict


if __name__ == '__main__':
    # Тестируем Решение № 1
    start_time = time.time()
    print(find_top3_1(top_companies_by_profit))
    end_time = time.time()
    print(f'Duration of function № 1 is - {end_time - start_time}')

    # Тестируем Решение № 2
    start_time = time.time()
    print(find_top3_2(top_companies_by_profit))
    end_time = time.time()
    print(f'Duration of function № 2 is - {end_time - start_time}')

    # Тестируем Решение № 3
    start_time = time.time()
    print(find_top3_3(top_companies_by_profit))
    end_time = time.time()
    print(f'Duration of function № 3 is - {end_time - start_time}')


# Наиболеее эффективное решение - Решение № 2, так как оно имеет меньшую вычислительную сложность

