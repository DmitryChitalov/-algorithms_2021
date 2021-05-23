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

def substrings_count(user_text):
    substrings_hash = {}
    for i in range(len(user_text) + 1):
        for j in range(i + 1, len(user_text) + 1):
            substring = user_text[i:j]
            substrings_hash[hash(substring)] = substring
    substrings_hash.pop(hash(user_text))
    return substrings_hash


def substrings_print(user_text):
    for value in substrings_count(user_text).values():
        print(value)
    return f''


print(substrings_print('papa'))
