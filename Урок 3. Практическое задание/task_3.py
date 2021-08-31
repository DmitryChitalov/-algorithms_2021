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


S = input('Введите строку')
N = len(S)
my_set = set()
for i in range(N):
    for j in range(i + 1, N + 1):
        if S[i:j] != S:
            my_set.add(S[i:j])
print(my_set)

hash_set = set()
for n in my_set:
    hash_set.add(hashlib.sha256(n.encode()).hexdigest())
print(hash_set)
print(f'Количество различных (уникальных) подстрок: {len(hash_set)}')
