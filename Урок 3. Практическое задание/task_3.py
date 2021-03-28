import random
import string

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


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


# generate_random_string(16)

# s = 'papa'
s = generate_random_string(6)
print(f'Рандомная строка: {s}')
hash_substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

print(set(hash_substrings))
print(f'Уникальных подстрок: {len(set(hash_substrings)) - 1}')  # -1 значение, собственно сама строка
