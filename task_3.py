"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
"""


my_string = input('Введите строку: ')
my_set = set()

for i in range(len(my_string)):
    for j in range(len(my_string) - 1 if i == 0 else len(my_string), i, -1):
        my_set.add(hash(my_string[i:j]))

substrings_count = len(my_set)
print(f"В строке: '{my_string}' {substrings_count} подстрок.\n"
      f"Хеш {my_set}")
