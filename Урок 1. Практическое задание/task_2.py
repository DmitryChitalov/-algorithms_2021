"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import math


def find_min_n_pow_2(arr):
    min_el = math.inf
    for el1 in arr:
        min_num = 0
        for el2 in arr:
            if el1 <= el2:
                min_num += 1
        if min_num == len(arr):
            min_el = el1
    return min_el


def find_min_n(arr):
    min_el = math.inf
    for el1 in arr:
        if el1 < min_el:
            min_el = el1
    return min_el


test_cases = [
    {
        'props': [8, 3, 0, 1, 5, 6],
        'result': 0,
    },
    {
        'props': [9, 7, 5, 3],
        'result': 3,
    },
    {
        'props': [-1, 9, 7, 5, 3],
        'result': -1,
    },
    {
        'props': [0],
        'result': 0,
    },
    {
        'props': [],
        'result': math.inf,
    }
]

passed_tests = 0
for test_case in test_cases:
    props = test_case["props"]
    expected_result = test_case["result"]
    real_result = find_min_n_pow_2(props)
    is_ok = real_result == expected_result
    if is_ok:
        passed_tests += 1
    print(f'{is_ok} find_min_n_pow_2({props}) => {real_result}')
print(f'passed tests: {passed_tests}/{len(test_cases)}\n')

passed_tests = 0
for test_case in test_cases:
    props = test_case["props"]
    expected_result = test_case["result"]
    real_result = find_min_n(props)
    is_ok = real_result == expected_result
    if is_ok:
        passed_tests += 1
    print(f'{is_ok} find_min_n({props}) => {real_result}')
print(f'passed tests: {passed_tests}/{len(test_cases)}\n')
