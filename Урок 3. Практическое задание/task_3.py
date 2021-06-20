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

import hashlib, uuid


my_str = 'papa'
hash_my_set = set()
substrings = set()
n = 0
salt = uuid.uuid4().hex

for i in range(len(my_str)):
    for j in range(i+1, len(my_str) + 1):
        if my_str[i:j] != 'papa':
            substrings.add(my_str[i:j])
            hash_my_set.add(hashlib.sha256(salt.encode() + my_str[i:j].encode()).hexdigest())

print(f'Result: {my_str} - {len(hash_my_set)} уникальных подстрок.')
for i in substrings:
    print(f'{n+1}я подстрока: "{i}". Хеш подстроки: "{list(hash_my_set)[n]}"')
    n += 1
