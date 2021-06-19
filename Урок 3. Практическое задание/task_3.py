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

def substrings(text):
    res = []
    for i in range(1, len(text)):
        for j in range(len(text)):
            start = j
            end = start + i
            res.append(text[start:end])
    for i in range(1, len(text)):
        for j in range(len(text)):
            start = j
            end = start + i
            res.append(text[::-1][start:end])
    return res


does_not_hashed_substrings = substrings('papa')
hash_res = set(i for i in map(hash, does_not_hashed_substrings))

hashed_unique_substrings = []
for i in hash_res:
    for j in does_not_hashed_substrings:
        if hash(j) == i:
            hashed_unique_substrings.append(j)
            break
print(hashed_unique_substrings)