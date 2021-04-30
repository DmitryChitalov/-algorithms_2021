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

def func_hash(user_str):
    system_set = set()
    for el in range(1, len(user_str)):
        for i in range(0, len(user_str)):
            k = user_str[i:i+el]
            system_set.add(hash(k.encode('utf-8')))
    return len(system_set)

user_str = "papak"
print(func_hash(user_str))