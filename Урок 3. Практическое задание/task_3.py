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
str = "papa"
str_initial_length = len(str)
set_ = set()
for i in range(0, len(str)):
    for j in range(1, len(str) + 1):
        if str_initial_length != len(str[:j]):
            set_.add(hash(str[:j]))
    str = str[1:]
print(f"Количество уникальных подстрок: {len(set_)}")
