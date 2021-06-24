
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


def get_len_unique_str(my_string):
    unique_str = set([hash(my_string[i:j + i + 1]) for i in range(len(my_string)) for j in range(len(my_string) + 1)])
    unique_str.discard(hash(my_string))
    return f'В строке {my_string} - {len(unique_str)} уникальных строк'


my_str = 'papa'
print(get_len_unique_str(my_str))
