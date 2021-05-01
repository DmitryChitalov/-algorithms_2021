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
    result = []
    for i in range(len(string)):
        for j in range(1, len(string)):
            result.append(hash(string[i:i + j]))
    print(f'Unique substrings: {len(set(result))}\n')


substrings('papa')
substrings('rhhjf')
substrings('asdfg')
