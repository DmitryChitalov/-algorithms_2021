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

import hashlib

word = str(input('Введите слово: '))
hash_set = set()
number = 1

for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        if word[i:j] != word:
            print(number, '-', word[i:j])
            number += 1
            hash_set.add(hashlib.sha256(word[i:j].encode()).hexdigest())

print(f'Уникальных подстрок: {len(hash_set)}')
