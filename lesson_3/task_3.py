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

test_set = set()
test_string = 'papa'
cnt = 0
for el_1 in test_string:
    cnt += 1
    substring = el_1
    hash_substring = hash(substring)
    test_set.add(hash_substring)
    for el_2 in test_string[cnt:]:
        substring += el_2
        hash_substring = hash(substring)
        test_set.add(hash_substring)
test_set.discard(hash(test_string))
print(len(test_set))

