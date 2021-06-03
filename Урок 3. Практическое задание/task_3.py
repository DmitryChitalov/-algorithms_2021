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


source_line = input('Введите слово: ')
str_set = set()
hash_set = set()
for i in range(len(source_line)):
    for j in range(len(source_line), i, -1):
        str_set.add(source_line[i:j])
        hash_set.add(hash(source_line[i:j]))
str_set.remove(source_line)

print(f'{source_line} - {len(hash_set) - 1} уникальных подстрок')
for sub_str in str_set:
    print(sub_str)

# Непонятно, зачем нужны хэши в этой задаче.

