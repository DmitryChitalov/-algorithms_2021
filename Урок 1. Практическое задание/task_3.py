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

# import random             #### O(n) - хороший вариант. Линейная сложность
# from collections import OrderedDict
#
# company_profit = dict(Apple=0, Xiaomi=0, Rostech=0, Microsoft=0, ChinaMObile=0, Huawei=0, Verizon=0, Beeline=0) ##O(1)
#
# for d in company_profit:   ########### O(n)
#     company_profit[d] = random.randint(-100, 1000)  ###### O(1)
#
# print(company_profit)
#
# b = OrderedDict(sorted(company_profit.items(), key=lambda t: t[1])) #### O(n)
# b = list(b)   #### O(1)
# top_3 = b[-3:] ### O(1)
# print(b)
# print(top_3)




# import random         ##############O(n2) квадратичная потому что много циколв for - не самый лучший вариант
#
#
# company_profit = dict(Apple=0, Xiaomi=0, Rostech=0, Microsoft=0, ChinaMobile=0, Huawei=0, Verizon=0, Beeline=0)
#
# for d in company_profit:  ##### O(n)
#     company_profit[d] = random.randint(-100, 1000)
# print(company_profit)
#
# list_profit = []   ### O(1)
# result = {}        #### O(1)
#
# for v in company_profit.values():   ### O(n)
#     list_profit.append(v)           ### O(1)
# profit_3 = sorted(list_profit)[-3:]  ###O(1)
# for k, v in company_profit.items():  ####O(n)
#     if v in profit_3:                ###O(1)
#         result[k] = v                ####O(1)
# print(result)
#
#

