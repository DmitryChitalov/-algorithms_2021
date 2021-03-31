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
a
"""

# hash?

input_string = str(input("Введите произвольную строку: "))


def hash_function(string):

    string_set = set()

    for i in range(len(string)):

        for j in range(len(string) - 1 if i == 0 else len(string), i, -1):

            string_set.add(hash(string[i:j]))

    return f"Количество различных подстрок в этой строке: {len(string_set)}"


print(hash_function(input_string))
