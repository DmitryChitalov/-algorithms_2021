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

s = input()
subs_set = set()
hash_set = set()
for start in range(0, len(s)):
    for finish in range(start + 1, len(s) + 1):
        subs = s[start:finish]
        subs_hash = hash(subs)
        if subs_hash not in hash_set:
            hash_set.add(subs_hash)
            subs_set.add(subs)

subs_set.remove(s)
print(subs_set)