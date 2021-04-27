"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

import hashlib

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def get_all_sub_strings(string):
    string_len = len(string)
    all_sub_strings = []
    for i in range(string_len):
        for j in range(i + 1, string_len + 1):
            all_sub_strings.append(string[i:j])
    # delete whole string, because it is not substring
    del all_sub_strings[string_len - 1]
    return all_sub_strings


def count_uniq_sub_strings(string):
    all_sub_strings = get_all_sub_strings(string)
    sub_strings_hash_set = set()
    for sub_string in all_sub_strings:
        sub_strings_hash_set.add((sub_string))
    return len(sub_strings_hash_set)

test_cases = [
    {
        'props': 'рара',
        'result': 6,
    },
    {
        'props': 'abcdefg',
        'result': 27,
    },
    {
        'props': 'ab',
        'result': 2,
    },
    {
        'props': 'a',
        'result': 0,
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