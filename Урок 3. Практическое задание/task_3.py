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

st = input("input word>>> ").lower()
dsd=set()
import itertools
import hashlib

items = st
for i in range(1,len(items)):
    for combination in itertools.combinations(st, i):
        if ''.join(list(combination)) in st:
            dsd.add(hashlib.sha256(''.join(list(combination)).encode()).hexdigest())
print(len(dsd))
print(dsd)
