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

from hashlib import sha256


def substring(string):
    hash_set = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] != string:
                hash_set.add(sha256(string[i:j].encode('utf-8')).hexdigest())
    print(f"строка '{string}' содержит {len(hash_set)} подстрок")


string = 'papa'
substring(string)
