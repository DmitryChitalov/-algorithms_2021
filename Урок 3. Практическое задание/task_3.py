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


def count_unique(word):
    hash_dict = {}
    for ind in range(len(word) + 1):
        for ind_2 in range(ind + 1, len(word) + 1):
            update_word = word[ind:ind_2]
            hash_dict[hash(update_word)] = update_word
    hash_dict.pop(hash(word))
    return hash_dict


user_word = input('Введите любое слово: ')
user_in_word = count_unique(user_word)
print(f'В строке {user_word} {len(user_in_word)} подстрок:')
for i in user_in_word.values():
    print(i)
