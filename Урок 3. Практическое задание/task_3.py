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

s_string = input("Введите строку:")
s_string_set = set()
for i in range(len(s_string)):
    for j in range(len(s_string)):
        #s_string_set.add(hashlib.sha256(s_string[i:j].encode()).hexdigest())
        s_string_set.add(hash(s_string[i:j]))

print(f"{s_string} - {(len(s_string_set))} уникальных подстрок")


