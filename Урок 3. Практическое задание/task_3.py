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

string = 'papa'
str_set = set()
count = 0
for el_1 in string:
    count += 1
    substring = el_1
    hash_substring = hash(substring)
    str_set.add(hash_substring)
    for el_2 in string[count:]:
        substring += el_2
        hash_substring = hash(substring)
        str_set.add(hash_substring)
str_set.discard(hash(string))
print(len(str_set))
