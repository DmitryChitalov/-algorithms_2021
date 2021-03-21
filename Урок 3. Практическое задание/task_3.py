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


def distinct_substr(text):
    dt = {}
    for i in range(len(text) + 1):
        for j in range(i + 1, len(text) + 1):
            new_substr = text[i:j]
            if new_substr != text:
                dt[hash(new_substr)] = new_substr
    print(f'{text} - {len(dt)} уникальных подстрок\n')
    print('\n'.join(dt.values()))


distinct_substr('papa')
