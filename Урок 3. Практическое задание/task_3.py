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


my_str = input('Введите строку: ')
my_list = []

for i in range(len(my_str)):
    print(my_str[i])
    for p in range(len(my_str)):
        if my_str[i:p+1] != '' and my_str[i:p+1] != my_str:
            my_list.append(hashlib.sha256(my_str[i:p+1].encode()).hexdigest())
my_set = set(my_list)
print(my_list)
print(my_set)
print(len(my_list))
print(len(my_set))


