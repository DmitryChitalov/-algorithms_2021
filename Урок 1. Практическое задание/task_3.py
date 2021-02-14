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

companies = {'first_company': 10, 'second_company': 20, 'third_company': 30,
             'fourth_company': 40, 'fifth_company': 50}

# 1) Линейно-логарифмическая сложность O(n log n)
income = sorted(companies.values())[2]
for key, value in companies.items():
    if value >= income:
        print(f"{key}: ${value}m.")


# 2) Линейная сложность O(n)
new_companies_dict = {}
for i in range(3):
    company_name = ''
    company_income = 0
    for el in companies:
        if companies.get(el) > company_income:
            company_name = el
            company_income = companies.get(el)
    new_companies_dict.update({company_name: companies.pop(company_name)})

companies.update(new_companies_dict)

for key, vale in new_companies_dict.items():
    print(f"{key}: ${value}m.")

# Второе решение более эффективное, потому что имеет линейную сложность O(n) -> быстрее отработает
