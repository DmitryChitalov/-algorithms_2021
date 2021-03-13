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


def max_profit_3el_company_ver_1(par_companies):
    # O(n Log n) - Линейно-логарифмическая сложность
    print(f'Компании: {par_companies}')
    return sorted(par_companies.items(), key=lambda item: item[1], reverse=True)[:3]


def max_profit_3el_company_ver_2(par_companies):
    # O(n) - Линейная сложность
    print(f'Компании: {par_companies}')
    top_company = {}
    for i in range(3):
        max_name = ''
        max_profit = 0
        for key in par_companies:
            if par_companies.get(key) > max_profit:
                max_name = key
                max_profit = par_companies.get(key)
        par_companies.pop(max_name)
        top_company.update({max_name: max_profit})
    print(par_companies)
    return top_company


companies = {'Fly': 100000, 'Honor': 120000, 'Samsung': 550555,
             'Apple': 666666, 'Nokia': 3450, 'Huawei': 435054, 'Xiaomi': 350900, 'BQ': 245000, }

print(max_profit_3el_company_ver_1(companies))
print()
print(max_profit_3el_company_ver_2(companies))

# Вторая функция будет эффективней и быстрей т.к. имеет O(n) линейную сложнсоть и задействуют меньше ресурсов
