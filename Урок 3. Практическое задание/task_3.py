"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной length_str, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
a
"""

# hash?
given_str = input('Введите строку')
unique_ = set()
length_str = len(given_str)
for el in range(length_str):
    if el == 0:
        length_str = len(given_str) - 1
    else:
        length_str = len(given_str)
    for el_1 in range(length_str, el, -1):
        unique_.add(hash(given_str[el:el_1]))
print(f'В строке {given_str} {len(unique_)} уникальных подстрок')
