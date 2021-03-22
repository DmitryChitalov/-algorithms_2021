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


def unique(word, string_hash=[]):
    for k in range(2, len(word) + 1):
        string_hash.append(hash(word[1:k]))
        string_hash.append(hash(word[:k - 1]))

    return f'{set(string_hash)}\nКоличество элементов: {len(set(string_hash))}'

print(unique('papa'))

