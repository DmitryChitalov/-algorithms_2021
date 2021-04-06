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


def count_substrings(u_str):
    rez_set = set()
    for i in range(len(u_str)):
        for j in range(i + 1, len(u_str) + 1):
            rez_set.add(hash(u_str[i:j]))
            print(f'{u_str[i:j]}, ', end='')
    rez_set.remove(hash(u_str[:len(u_str)]))
    return len(rez_set)


user_str = 'zxxxx'
print(f'\nВ строке "{user_str}" содержится {count_substrings(user_str)} уникальных подстрок')
