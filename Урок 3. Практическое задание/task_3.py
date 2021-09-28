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

import hashlib


def func(string):
    start = 0
    end = 1
    set_x = set()
    while start != len(string)-1:
        if end != len(string):
            set_x.add(hashlib.sha256(string[start:end].encode()).hexdigest())
            end += 1
        else:
            start += 1
            set_x.add(hashlib.sha256(string[start:].encode()).hexdigest())
            end = start + 1
    set_x.add(hashlib.sha256(string[start].encode()).hexdigest())
    return set_x


if __name__ == '__main__':
    string_x = 'qwerqwerio'
    print(len(func(string_x)))