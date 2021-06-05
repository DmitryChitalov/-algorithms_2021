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
from hashlib import sha256

def unique_str(base_str, set_of_str=set()):
    for word in range(1, len(base_str)):
        if base_str[-word] == '':
            continue

        set_of_str.add(sha256(base_str[:-word].encode()).hexdigest())
    set_of_str.add(sha256(base_str[1:].encode()).hexdigest())
    if len(base_str) == 1:
        return set_of_str
    else:
        return unique_str(base_str[1:], set_of_str)


print(unique_str('dogfrog'))
