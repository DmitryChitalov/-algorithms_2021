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
from hashlib import sha256

def string_hash(string):
    firstset = set()
    secondset = set()
    n = len(string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            firstset.add(string[i:j])
    print(firstset)
    for i in firstset:
        secondset.add(sha256(i.encode('utf-8')).hexdigest())
    print(secondset)

string_hash('papa')