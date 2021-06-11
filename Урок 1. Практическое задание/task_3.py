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

company_margin = {
    'Berkshire Hathaway': 81417,
    'Apple': 55256,
    'Industrial & Commercial Bank of China': 45195,
    'Microsoft': 39240,
    'China Construction Bank': 38610,
    'JPMorgan Chase & Co.': 36431,
    'Alphabet': 34343,
    'Saudi Aramco': 88211,
    'Agricultural Bank of China': 30701,
    'Bank of America Corp.': 27430
}

"""
solution1
Самый удачный по производительности код, основная 'стоимость' которого - это сортировка списка.
выборка в цикле всегда имеет постоянную сложность (3 элемента)
Общая сложность O(n log n)
"""


def tree_company_max_margin(dict):
    if len(dict) == 0:                          #O(1)
        return None                             #O(1)
    company = list(dict.keys())                 #O(n)+O(1)
    if len(dict) <= 3:                          #O(1)
        return '; '.join(company)               #O(1) элементов всегда будет не больше 3
    margin = list(dict.values())                #O(n)+O(1)
    sort_margin = sorted(margin, reverse=True)  #O(1)присваивание + O(n log n) сортировка
    result = []                                 #O(1)
    for i in sort_margin[:3]:                   #O(1) всегда 3 значения
        ind = margin.index(i)                   #O(1)
        result.append(company[ind])             #O(1)
    return '; '.join(result)                    #O(1)


print(tree_company_max_margin(company_margin))


"""
solution2
самое малоэффективное решение(длинный код, много ресурсов задействуется при решении, а при увеличении
исходного словаря, растет количество иттераций)
Общая сложность n**2 квадратичная
1+1+1+n*(1+1 1+n +1+1 +n*(1+1))=3+2n+n+n**2+n**2
"""


def tree_company_max_margin2(dict):
    if len(dict) == 0:                                  #O(1)
        return None                                     #O(1)
    result = {}                                         #O(1)
    for key, val in dict.items():                       #O(n)
        if len(result) < 3:                             #O(1)
            result[key] = val                           #O(1)
        else:
            min_val = min(result.values())              #O(1)
            if val > min_val:                           #O(1)
                result[key] = val                       #O(1)
                for key_res, val_res in result.items(): #O(n)
                    if val_res == min_val:              #O(1)
                        del result[key_res]             #O(1)
                        break
    return '; '.join(list(result.keys()))               #O(1)


print(tree_company_max_margin2(company_margin))


"""
solution3
Самый короткий и, на мой взгляд, читаемый код. Квадратичная сложность получилась из-за манипуляций в присваивании:
слиянии двух списков, а затем их сортировка.
(очень надеюсь, что я не неверно поняла, как определять сложность по О нотации и на самом деле у данного
решения линейная сложность O(N) и оно самое лучшее из представленного!)
Общая сложность n**2
1+1+n+1+1+n+1*(n log n)*n+1
"""


def tree_company_max_margin3(dict):
    if len(dict) == 0:                                                  #O(1)
        return None                                                     #O(1)
    company = list(dict.keys())                                         #O(n)
    if len(dict) <= 3:                                                  #O(1)
        return '; '.join(company)                                       #O(1)
    margin = list(dict.values())                                        #O(n)
    new_list_company = sorted(zip(margin, company), reverse=True)       #O(n log n)сортировка*O(n)слияние+присваиваниеO(1)
    return '; '.join([x[1] for x in new_list_company[:3]])              #O(1)


print(tree_company_max_margin3(company_margin))
