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


Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
"""


def unique_substrings_hash(string):
    unique_substring = set( )
    for i in range(len(string)):
        for q in range(1, len(string) + 1):
            if i == q or q < i:
                continue
            if string[i:q] == string:
                continue
            unique_substring.add(string[i:q].__hash__( ))
    return f'{string} - {len(unique_substring)} уникальных подстрок'

print(unique_substrings_hash('papa'))
print(unique_substrings_hash('apapa'))
print(unique_substrings_hash('ab'))