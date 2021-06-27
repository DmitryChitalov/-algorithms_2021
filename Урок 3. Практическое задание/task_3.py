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


def substrings_pass(password):
    substrings = set()
    for i in range(len(password)):
        for j in range(len(password)):
            substrings.add(password[i:j + 1])
    substrings.remove(password)
    substrings.remove("")
    return set(map(hash, substrings))


print(substrings_pass(input("Введите пароль: ")))
