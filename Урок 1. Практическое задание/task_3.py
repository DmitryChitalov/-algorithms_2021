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
import math


def find_3_companies_with_max_income(companies):
    max_incomes = [-math.inf, -math.inf, -math.inf]
    companies_with_max_income = [None, None, None]
    for company in companies:
        income = company['income']
        max_incomes_index = -1
        for i, max_income in enumerate(max_incomes):
            if income > max_income:
                max_incomes_index = i
            else:
                break
        if max_incomes_index != -1:
            max_incomes[max_incomes_index] = income
            companies_with_max_income[max_incomes_index] = company
        print(max_incomes)
    return companies_with_max_income

test_cases = [
    {
        'props': [
            {
                'name': 'yandex',
                'income': 3,
            },
            {
                'name': 'google',
                'income': 5,
            },
            {
                'name': 'ibm',
                'income': 2,
            },
            {
                'name': 'amazon',
                'income': 9
            },
        ],
        'result': [
            {
                'name': 'yandex',
                'income': 3,
            },
            {
                'name': 'google',
                'income': 5,
            },
            {
                'name': 'amazon',
                'income': 9
            },
        ],
    },
]

passed_tests = 0
for test_case in test_cases:
    props = test_case["props"]
    expected_result = test_case["result"]
    real_result = find_3_companies_with_max_income(props)
    is_ok = real_result == expected_result
    if is_ok:
        passed_tests += 1
    print(f'{is_ok} find_3_companies_with_max_income\n{props} => \n{real_result}')
print(f'passed tests: {passed_tests}/{len(test_cases)}\n')
#
# passed_tests = 0
# for test_case in test_cases:
#     props = test_case["props"]
#     expected_result = test_case["result"]
#     real_result = find_min_n(props)
#     is_ok = real_result == expected_result
#     if is_ok:
#         passed_tests += 1
#     print(f'{is_ok} find_min_n({props}) => {real_result}')
# print(f'passed tests: {passed_tests}/{len(test_cases)}\n')

