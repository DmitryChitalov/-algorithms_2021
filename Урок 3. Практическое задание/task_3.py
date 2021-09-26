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


def calc_substrings(el: str):
    substrings = set()
    for i in range(len(el)):
        for z in range(i, len(el)):
            substrings.add(hash(el[i:z + 1]))
    substrings.remove(hash(el))
    return len(substrings)


print(calc_substrings('papa'))
