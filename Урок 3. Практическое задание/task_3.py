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

my_set = set()
my_string = 'idiom'
for i in range(len(my_string)):
    for j in (i + 1, len(my_string) + 1):
        if my_string[i:j] != my_string:
            my_set.add(hashlib.sha256(my_string[i:j].encode()).hexdigest())
            print(my_string[i:j], end=' ')
print(f'\n{my_set}')
print(f'Element in set: {len(my_set)}')
