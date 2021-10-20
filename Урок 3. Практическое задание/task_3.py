"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

# hash?

import hashlib

subs_set = set()
str_user = str(input("Введите строку: "))

print(f"Строка {str_user} имеет длину {len(str_user)} сиволов.")

for i in range(len(str_user)):
    for j in range(i + 1, len(str_user) + 1):
        if str_user[i:j] != str_user:
            subs_set.add(hashlib.sha256(str_user[i:j].encode()).hexdigest())
            print(str_user[i:j])

print("количество элементов в множестве: ", len(subs_set))
print("Хеш элементов: ")
print(*subs_set, sep="\n")
