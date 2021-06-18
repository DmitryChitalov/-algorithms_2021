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


def substrings(s):  # возвращает подстроки
    length = len(s)
    result = []
    for i in range(length):
        for j in range(i, length):
            if len(s[i:j+1]) < length: result.append(s[i:j+1])
    return result


def uniq_substrings(s):  # возвращает количество уникальных хешей подстрок
    length = len(s)
    result = set()
    for i in range(length):
        for j in range(i, length):
            if len(s[i:j+1]) < length:
                result.add(hash(s[i:j+1]))
    return len(result)


def uniq_substrings_oneline(s):  # и тоже самое в одну строку, для прикола
    return len(set([hash(s[i:j+1]) for i in range(len(s)) for j in range(i, len(s)) if len(s[i:j+1]) < len(s)]))


print(substrings('papa'))
print(uniq_substrings('papa'))
print(uniq_substrings_oneline('papa'))
