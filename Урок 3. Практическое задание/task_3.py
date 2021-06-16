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


def substrings(string):
    substrs = set()
    for i in range(1, len(string)):
        for j in range(len(string)):
            substr = string[j:j+i]
            print(hash(substr))
            substrs.add(substr)
    return substrs


print(substrings('papa'))