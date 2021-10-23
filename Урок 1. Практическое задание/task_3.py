"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
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

#  O(n log n)
companies = {'names': ['amoCrm', 'Facebook', 'WhatsApp', 'Samsung', 'iPhone', 'Xiaomi', 'Dell', 'HP'],
             'annual_profit': [200, 5448, 3665, 6514, 8774, 4785, 100, 3321]}
# sorted_list = sorted(companies['annual_profit'])
company_number_1 = sorted(companies['annual_profit'])[-1]  # O(n log n)
index_company_1 = companies['annual_profit'].index(company_number_1)  # O(n)
company_number_2 = sorted(companies['annual_profit'])[-2]  # O(n log n)
index_company_2 = companies['annual_profit'].index(company_number_2)  # O(n)
company_number_3 = sorted(companies['annual_profit'])[-3]  # O(n log n)
index_company_3 = companies['annual_profit'].index(company_number_3)  # O(n)
# print(sorted_list)
# print(company_number_1, index_company_1)
# print(company_number_2, index_company_2)
# print(company_number_3, index_company_3)
result_2 = \
    f"First company: {companies['names'][index_company_1]}, profit: {companies['annual_profit'][index_company_1]} \n" \
    f"Second company: {companies['names'][index_company_2]}, profit: {companies['annual_profit'][index_company_2]} \n" \
    f"Third company: {companies['names'][index_company_3]}, profit: {companies['annual_profit'][index_company_3]}"
print(result_2)
#
# # O(n log n ) вышло одинакого...
#
# companies = [['amoCrm', 'Facebook', 'WhatsApp', 'Samsung', 'iPhone', 'Xiaomi', 'Dell', 'HP'],
#              [200, 5448, 3665, 6514, 8774, 4785, 100, 3321]]
#
# new_result = {'first': [companies[0][companies[1].index(sorted(companies[1])[-1])], sorted(companies[1])[-1]],
#               'second': [companies[0][companies[1].index(sorted(companies[1])[-2])], sorted(companies[1])[-2]],
#               'third': [companies[0][companies[1].index(sorted(companies[1])[-3])],
#                         sorted(companies[1])[-3]]}  # [name,profit]  # O(n log n )
#
# print(new_result)

# O( n log n) опять??
companies = {'names': ['amoCrm', 'Facebook', 'WhatsApp', 'Samsung', 'iPhone', 'Xiaomi', 'Dell', 'HP'],
             'annual_profit': [200, 5448, 3665, 6514, 8774, 4785, 100, 3321]}
result = {'first': [0, 0], 'second': [0, 0], 'third': [0, 0]}  # [profit,index of the company]
sorted_list = sorted(companies['annual_profit'])
for i in range(len(companies['annual_profit'])):
    for j in range(len(companies['annual_profit'])):
        if companies['annual_profit'][i] == sorted_list[-1]:
            result['first'][0] = companies['annual_profit'][i]
            result['first'][1] = i

        elif companies['annual_profit'][i] == sorted_list[-2]:
            result['second'][0] = companies['annual_profit'][i]
            result['second'][1] = i

        elif companies['annual_profit'][i] == sorted_list[-3]:
            result['third'][0] = companies['annual_profit'][i]
            result['third'][1] = i

print(result)

# ## New O(n^2)
# sorted_list_by_me = companies['annual_profit']  # O(1)
# print(sorted_list_by_me)  # O(1)
# for j in range(len(companies['annual_profit']) - 1):  # O(n)
#     for i in range(len(companies['annual_profit']) - 1):  # O(n)
#         if sorted_list_by_me[i + 1] < sorted_list_by_me[i]:  # O(1)
#             x = sorted_list_by_me[i]  # O(1)
#             sorted_list_by_me[i] = sorted_list_by_me[i + 1]  # O(1)
#             sorted_list_by_me[i + 1] = x  # O(1)
#
# for i in range(len(companies['annual_profit'])):  # O(n)
#
#     if companies['annual_profit'][i] == sorted_list_by_me[-1]:  # O(1)
#         result['first'][0] = companies['annual_profit'][i]  # O(1)
#         result['first'][1] = i  # O(1)
#
#     elif companies['annual_profit'][i] == sorted_list_by_me[-2]:  # O(1)
#         result['second'][0] = companies['annual_profit'][i]  # O(1)
#         result['second'][1] = i  # O(1)
#
#     elif companies['annual_profit'][i] == sorted_list_by_me[-3]:  # O(1)
#         result['third'][0] = companies['annual_profit'][i]  # O(1)
#         result['third'][1] = i  # O(1)
#
# print(result)
# Думаю, что второй метод эффективнее, так как сложность меньше, и он проще всех