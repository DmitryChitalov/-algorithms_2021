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

def unique_string(letter, substring_hash=[]):

    for i in range(2, len(letter) + 1):
        substring_hash.append(hash(letter[1:i]))
        substring_hash.append(hash(letter[:i - 1]))
    return f'{set(substring_hash)}\n {len(set(substring_hash))} уникальных подстрок'

print(unique_string('geek'))