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

# Тяжелее вторая функция, так как её доминанта - линейно-логарифмическая, а у первой - линейная.


def max_dict_rev1(company_dict_func):                    # n + 1 + 3(3n + n + 1 + n) + 1 = 16n + 5
    company_dict_temp = company_dict_func.copy()            # O(n)
    best_companies = []                                     # O(1)
    for n in range(3):                                      # O(3)
        max_number = list(company_dict_temp.values())[0]    # O(n)
        for i in company_dict_temp:                         # O(n)
            if company_dict_temp.get(i) >= max_number:      # O(1)
                max_number = company_dict_temp.get(i)       # O(1)
                max_key = i                                 # O(1)
        best_companies.append(max_key)                      # O(1)
        del company_dict_temp[max_key]                      # O(n)
    return best_companies                                   # O(1)


def max_dict_rev2(company_dict_func1):                  # n + nlogn + 3 + 1 + 3(2n) + 2n + 1 = nlogn + 9n + 5
    rev_list = list(company_dict_func1.values())        # O(n) Я не нашёл значение для values. И хотел бы узнать,
    rev_list.sort(reverse=True)                         # O(nlogn)    в таком случае надо складывать или умножать
    top_3_rev = rev_list[:3]                            # O(3)
    top_3_comp = []                                     # O(1)
    for i in top_3_rev:                                 # O(3)
        for comp, rev in company_dict_func1.items():    # O(n) Я не нашёл цену items и хотел бы узнать как считать цену,
            if rev == i:                                # O(1)                когда мы итерируемся по результату функции
                top_3_comp.append(comp)                 # O(1)
    top_3_comp = list(set(top_3_comp))                  # O(2n)
    return top_3_comp                                   # O(1)


company_dict = {'company1': 55555, 'company2': 66666, 'company3': 77777, 'company4': 88888,
                'company5': 99999, 'company6': 11111, 'company7': 22222, 'company8': 33333, 'company9': 44444,
                'company10': 12345, 'company11': -11111, 'company12': 99999}

print(max_dict_rev1(company_dict))
print(max_dict_rev2(company_dict))
