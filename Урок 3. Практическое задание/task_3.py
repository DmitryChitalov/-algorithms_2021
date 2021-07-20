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


def str_sub_count(str_text):
    str_hash = {}
    for i in range(len(str_text) + 1):
        for j in range(i + 1, len(str_text) + 1):
            str_hash[hash(str_text[i:j])] = str_text[i:j]
    str_hash.pop(hash(str_text))
    return str_hash


def str_sub(user_text):
    for i in str_sub_count(user_text).values():
        print(i)
    return f''


print(str_sub('papa'))
