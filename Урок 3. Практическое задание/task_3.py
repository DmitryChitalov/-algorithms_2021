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


def substring_count(string):
    substrings = [hash(string[i:i+j]) for i in range(len(string))
                                      for j in range(1, len(string))]
    print(f'В строке {string} {len(set(substrings))} уникальных подстрок.')


if __name__ == '__main__':

    substring_count('papa')
    substring_count('papapa')
    substring_count('qwerty')
