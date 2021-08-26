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

hash_set = set()
some_str = 'papa'
for i in range(len(some_str)):
    for j in range(i + 1, len(some_str) + 1):
        if some_str[i:j] != some_str:
            hash_set.add(hashlib.sha256(some_str[i:j].encode()).hexdigest())
            print(some_str[i:j])

print(f'Количество уникальных подстрок: {len(hash_set)}')
print(f'\n{hash_set}')
