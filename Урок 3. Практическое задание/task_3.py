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


def uniq(word):
    arr = set()
    for i in range(0, len(word) + 1):
        for j in range(i + 1, len(word) + 1):
            arr.add(hash(word[i:j]))
    arr.remove(hash(word))
    return len(arr)


print(uniq('papa'))
