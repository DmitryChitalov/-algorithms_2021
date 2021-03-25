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


def count_word(word):
    hash_dict = {}
    for i in range(len(word) + 1):
        for j in range(i + 1, len(word) + 1):
            update_word = word[i:j]
            hash_dict[hash(update_word)] = update_word
    hash_dict.pop(hash(word))
    return hash_dict


user_str = input('Введите одно слово: ')
user_in_str = count_word(user_str)
print(f'В строке {user_str} {len(user_in_str)} уникальных подстрок:')
for el in user_in_str.values():
    print(el)
