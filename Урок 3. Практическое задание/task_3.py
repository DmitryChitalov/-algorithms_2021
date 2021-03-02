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
# Задание не смог выполнить. Код из примера преподавателя.

string = input('>> ')
sub_strings = set()

for sub in range(len(string)):
    last_str = string[sub:]
    for length in range(1, len(last_str) + 1):
        sub_str = string[sub:sub + length]
        if string != sub_str:
            hash_sub_str = sub_str.encode().hex()
            sub_strings.add(hash_sub_str)

print(len(sub_strings), sub_strings)
