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


def search_substring(string):
    set_unic_string = set()
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            if hash(string[i:j]) not in set_unic_string and string[i:j] != string:
                set_unic_string.add(hash(string[i:j]))
                print(string[i:j])
    return len(set_unic_string)


search_substring(input('Введите строку: '))
