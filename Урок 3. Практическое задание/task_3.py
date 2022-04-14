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


Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
"""

S = 'papa'
hash_obj = hash(S)
some_set = {hash_obj,}
some_list = []

for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        hash_str = hash(S[i:j])
        if hash_str not in some_set:
            some_set.add(hash_str)
            some_list.append(S[i:j])

print(some_list)

