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


def find_func(some_str):
    cache = []
    count = -1
    for idx in range(1, len(some_str)):
        if hash(some_str[:idx]) not in cache:
            count += 1
            cache.append(hash(some_str[:idx]))
        if hash(some_str[idx:]) not in cache:
            count += 1
            cache.append(hash(some_str[idx:]))
        for idx2 in range(len(some_str), 0, -1):
            if hash(some_str[idx:idx2]) not in cache:
                count += 1
                cache.append(hash(some_str[idx:idx2]))
    print(count)


if __name__ == '__main__':
    find_func('papa')
