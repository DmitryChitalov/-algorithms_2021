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
my_string = input('Enter the string: ')
my_set = set()

for i in range(len(my_string)):
    for j in range(len(my_string) - 1 if i == 0 else len(my_string), i, -1):
        my_set.add(hash(my_string[i:j]))

substrings_count = len(my_set)
print(f"In the line: '{my_string}' {substrings_count} substrings. \n"
      f"Hash {my_set}")
