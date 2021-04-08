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


def unique_search(word):
    temp_hash = {}
    for i in range(len(word)):
        for el in range(i, len(word)):
            element = word[i:el + 1]
            temp_hash[hash(element)] = element
    temp_hash.pop(hash(word))
    print(f'{word} - {len(temp_hash)} уникальных подстрок \n')
    for num, words in enumerate(temp_hash.values()):
        print(f'{num + 1}) {words}')


unique_search('papa')
print("*" * 40)
unique_search('google')
