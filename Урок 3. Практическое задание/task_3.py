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

string = input('Введите набор строчных латинских букв: ')

hash_set = set()

for i in range(len(string)):
    for j in range(len(string[i:])):
        hash_set.add(hash(string[i:][:j+1]))
        print(string[i:][:j+1])

hash_set.remove(hash(string))

print(len(hash_set))

print(hash_set)





