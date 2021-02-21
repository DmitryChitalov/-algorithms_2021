import hashlib
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


def search_str(new_string):
    length = len(new_string)
    result = set()
    for elem in range(length):
        if elem == 0:
            length = len(new_string) - 1
        else:
            length = len(new_string)
        for j in range(length, elem, -1):
            # result.add(new_string[elem:j])
            result.add(hashlib.sha1(new_string[elem:j].encode('utf-8')).hexdigest())
    return f'кол-во подстрок <<{new_string}>> равно {len(result)}'


print(search_str('papa'))


