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

def substrings(string):
    list_of_substrings = []
    for i in range(len(string)):
        for j in range(len(string) - i):
            substring = string[i:len(string)-j]
            list_of_substrings.append(hash(substring))
    list_of_substrings.remove(hash(string))
    result = set(list_of_substrings)
    print(f'Количество уникальных подстрок строки "{string}": {len(result)}')


substrings('papa')