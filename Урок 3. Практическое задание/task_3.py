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


def unique(word):
    bd_hash = {}
    for i in range(len(word) + 1):
        for j in range(i + 1, len(word) + 1):
            upd = word[i:j]
            bd_hash[hash(upd)] = upd
    bd_hash.pop(hash(word))
    return bd_hash


in_word = 'papa'
split_word = unique(in_word)
print(f'{in_word} - {len(split_word)} уникальных подстрок:\n')
for key in split_word:
    print(split_word[key])
