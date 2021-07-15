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


def get_set_with_hash(string):
    string = ''.join(string.split())
    return {hashlib.sha256(string[i:j].encode()).hexdigest() for i in range(len(string)) for j in
            range(i + 1, len(string) + 1) if len(string[i:j]) != len(string)}


my_string = 'papa'
hash_set = get_set_with_hash(my_string)
print(f"Строка {my_string} содержит {len(hash_set)} уникальных подстрок")
