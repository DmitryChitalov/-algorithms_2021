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
line = input("Введите строку :")
list_strings = set()


res_set = set()
for el in range(len(line)):
    last_str = line[el:]
    for length in range(1, len(last_str) + 1):
        sub_str = line[el:el + length]
        if line != sub_str:
            hash_sub_str = hash(sub_str)
            res_set.add(hash_sub_str)

print(len(res_set))
print(f"Количество подстрок в строке {line} равно {len(list_strings)}")