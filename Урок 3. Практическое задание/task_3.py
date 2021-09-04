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

uniq_string = ""


def substring(string):
    for i in range(len(string)):
        for j in range(i, len(string)):
            if not string[i:j + 1] == string:
                uniq_string.add(hash(string[i:j + 1]))
    return f'{string} - {len(uniq_string)} подстрок'


string = "papa"
uniq_string = set(uniq_string)
print(substring(string))
