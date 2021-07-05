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


def unic_substring(string, hash_set, substring_set):
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] != string:
                substring_set.add(string[i:j])
                hash_set.add(sha256(string[i:j].encode()).hexdigest())
    print(f"строка '{string}' содержит {len(substring_set)} подстрок")
    print(substring_set)


set_of_hash = set()
set_of_substring = set()
my_string = 'papa'
unic_substring(my_string, set_of_hash, set_of_substring)
