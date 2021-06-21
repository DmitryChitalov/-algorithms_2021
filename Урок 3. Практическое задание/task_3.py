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


def find_unique(string):
    unique_hash_set = set()
    unique_string_set = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] != string:
                unique_hash_set.add(hash(string[i:j]))
                unique_string_set.add(string[i:j])
    print(f"'{string}' - {len(unique_hash_set)} уникальных подстрок:\n")
    print(*unique_string_set, sep="\n")


find_unique('papa')
