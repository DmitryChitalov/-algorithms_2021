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


def find_substring(user_string):
    substring = set()
    for i in range(len(user_string)):
        for j in range(i + 1, len(user_string) + 1):
            if user_string[i:j] != user_string:
                substring.add(hash(user_string[i:j]))
    print(f'{substring}')
    print(f'{user_string} - {len(substring)} уникальных подстрок.')


u_string = 'papa'
find_substring(u_string)
