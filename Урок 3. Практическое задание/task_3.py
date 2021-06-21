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
s = input('Enter some string: ')
hash_set = set()
substring_set = set()
for i in range(len(s)):
    for j in range(len(s), i, -1):
        if s[i:j] != s:
            substring_set.add(s[i:j])
            hash_set.add(hash(s[i:j]))


print(f'there are {len(hash_set)} unique substrings in string "{s}": {substring_set}')
