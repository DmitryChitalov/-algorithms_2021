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

# Заметим из примера, что строка самой себе не подстрока (), как и пустая строка.

user_input = input('Введите непустую строку: ')

while 1:
    if user_input:
        break
    else:
        user_input = input('Пустая строка не принимается.\nВведите строку: ')

unique_hash, values = set(), []

for i in range(len(user_input)):
    for j in range(i, len(user_input)):
        unique_hash.add(hash(user_input[i:j + 1]))
        values.append(user_input[i:j + 1])

print(f'{user_input} - {len(unique_hash) - 1} уникальных подстрок\n')
for i in values:
    if i == user_input:
        continue
    if hash(i) in unique_hash:
        print(i)
        unique_hash.remove(hash(i))
