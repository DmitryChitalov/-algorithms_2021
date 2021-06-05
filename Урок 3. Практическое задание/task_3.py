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

word = '12'

def num_unique(word):
    unique_date = set()

    for i in range(len(word) + 1):
        for j in range(i + 1, len(word) + 1):
            value = word[i:j]
            print(value)
            if value != word:
                hash_value = hashlib.sha256(value.encode()).hexdigest()
                unique_date.add(hash_value)

    return unique_date

print(num_unique(word))