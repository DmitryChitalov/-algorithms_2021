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


def str_counter(str_for_count):
    word_dict = {}
    for i in range(len(str_for_count) + 1):
        for j in range(i + 1, len(str_for_count) + 1):
            new_word = str_for_count[i:j]
            word_dict[hash(new_word)] = new_word
    word_dict.pop(hash(str_for_count))  # удалим исходное слово из вариантов
    print(f'Количество уникальный строк {len(word_dict)}')
    for word in word_dict.values():
        print(word)


str_counter(input('Введите строку для подсчета: '))
