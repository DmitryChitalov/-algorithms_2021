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
def substrings(string):
    my_set = set()
    for i in range(len(string)):
        if i == 0:
            delta = 0
        else:
            delta = 1
        for j in range(i + 1, len(string) + delta):
            my_set.add(hash(string[i:j]))
    return len(my_set)


print(substrings('papa'))
