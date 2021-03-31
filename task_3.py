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
a
"""

# hash?

my_string  = input('введите строку: ')
my_set = set()
for i in range(len(my_string)):
    for j in range(i+1, len(my_string)+1):
        my_str= my_string[i:j]
        # print(my_str)
        my_hash = hash(my_str)
        if my_hash not in my_set and my_str != my_string:
            my_set.add(my_hash)

print(my_set)
print('число вхождений ', len(my_set))




# if hash('p') in my_set:
#     print(1)
