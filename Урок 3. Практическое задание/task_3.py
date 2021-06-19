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

uniq_set = set()

input_value = 'papa'

for i in range(len(input_value)):
    for j in range(i + 1, len(input_value) + 1):
        if input_value[i:j] != input_value:
            uniq_set.add(hashlib.sha256(input_value[i:j].encode()).hexdigest())

print(f'{input_value} - {len(uniq_set)} уникальных подстрок.')
