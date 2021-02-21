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
a
"""


def hash_func(word):
    hash_dict = {}
    for el in range(len(word) + 1):
        for elem in range(el + 1, len(word) + 1):
            update_word = word[el:elem]
            hash_dict[hash(update_word)] = update_word
    hash_dict.pop(hash(word))
    return hash_dict


user_word = 'papa'
user_in_word = hash_func(user_word)

print(f"{user_word} - {len(user_in_word)} уникальных подстрок:")
for element in user_in_word.values():
    print(element)
