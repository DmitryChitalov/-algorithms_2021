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

def search_of_unique(word):
    temp_hash = {}
    for i in range(len(word)):
        for el in range(i, len(word)):
            element = word[i:el + 1]
            temp_hash[hash(element)] = element
    temp_hash.pop(hash(word))
    print(f'{word} - {len(temp_hash)} unique substrings \n')
    for num, words in enumerate(temp_hash.values()):
        print(f'{num + 1}) {words}')


search_of_unique('papa')
print("*" * 40)
search_of_unique('google')
