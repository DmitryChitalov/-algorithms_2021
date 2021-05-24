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


company_dict = {'company1': 576567567, 'company2': 765876876, 'company3': 76547566, 'company4': 87567456,
                'company5': 5435345, 'company6': 765756, 'company7': 65754645, 'company8': 765654, 'company9': 6546544,
                'company10': 543432,'company11': 6543434, 'company12': 4234324}
# for i in company_dict:
#     print(i)
#     a = company_dict.get(i)
#     print(a)


# def max_dict_number(company_dict1):
#     company_dict = company_dict1
#     best_companies = []
#     for n in range(3):
#         max_number = list(company_dict.values())[0]
#         for i in company_dict:
#             if company_dict.get(i) > max_number:
#                 max_number = company_dict.get(i)
#         best_companies.append(max_number)
#         # company_dict.pop(i)
#         del company_dict[i]
#     return best_companies
#
# print(max_dict_number(company_dict))

best_companies = []
for n in range(3):
    max_number = list(company_dict.values())[0]
    for i in company_dict:
        if company_dict.get(i) > max_number:
            max_number = company_dict.get(i)
        best_companies.append(max_number)
        # company_dict.pop(i)
        del company_dict[i]
    print(company_dict)