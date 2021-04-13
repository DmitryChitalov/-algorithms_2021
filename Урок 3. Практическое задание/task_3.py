"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

# hash?

def count_uniq_sub_strings(string):
    return string

test_cases = [
    {
        'props': 'рара',
        'result': 6,
    },
    {
        'props': 'pa',
        'result': 2,
    },
]

passed_tests = 0
for test_case in test_cases:
    props = test_case["props"]
    expected_result = test_case["result"]
    real_result = count_uniq_sub_strings(props)
    is_ok = real_result == expected_result
    if is_ok:
        passed_tests += 1
    print(f'{is_ok} {count_uniq_sub_strings.__name__}({props}) => {real_result}{(f", but {expected_result} expected", "")[is_ok]}')
print(f'passed tests: {passed_tests}/{len(test_cases)}\n')