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

s = input("Введите строку: ")

all_substrings = [s[i: j] for i in range(len(s))
                  for j in range(i + 1, len(s) + 1)]

my_hash_set = []
my_set = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        if hash(s[i: j]) not in my_hash_set:
            my_set.append(s[i: j])
            my_hash_set.append(hash(s[i: j]))

print(all_substrings)
print(set(all_substrings))
print(my_set)
print(my_hash_set)
print(f"Количество подстрок всего - {len(all_substrings)}")
print(f"Количество уникальных подстрок - {len(set(all_substrings))}")
print(f"Мой счетчик уникальных комбинаций подстрок - {len(my_hash_set)}")
