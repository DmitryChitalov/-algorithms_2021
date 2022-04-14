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
S = 'string'
N = len(S)

print('Строка', S, 'имеет длину', N, 'символов.')

substring_s = set()
for i in range(len(S)):
    for j in range(len(S) - 1 if i == 0 else len(S), i, -1):
        substring_s.add(hash(S[i:j]))
        print(S[i:j], i, j)

print("Количество подстрок в строке:", S, 'равно:', len(substring_s))

# hash?
