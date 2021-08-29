import hashlib

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


def strings_count(word):
    a_set = set()
    for i in range(len(word)):
        for j in range(i, len(word)):
            if hashlib.sha256(word[i:j+1].encode()).hexdigest() != hashlib.sha256(word.encode()).hexdigest():
                a_set.add(hashlib.sha256(word[i:j+1].encode()).hexdigest())
            else:
                continue
    return len(a_set)


print(strings_count(input('Введите строку - ')))
