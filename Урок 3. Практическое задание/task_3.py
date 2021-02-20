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

from re import search


result = set({})

initial_str = input('Введите строку: ')
initial_str = initial_str.lower()

if search(r'^[a-z]*$', initial_str):
    for i in range(len(initial_str)):
        slice_1 = initial_str[i:]
        slice_2 = initial_str[:i]
        slice_3 = initial_str[i:-i]
    
        if 0 < len(slice_1) < len(initial_str):
            result.add(hash(slice_1))
        if 0 < len(slice_2) < len(initial_str):
            result.add(hash(slice_2))
        if 0 < len(slice_3) < len(initial_str):
            result.add(hash(slice_3))
        
    print(f'{initial_str} - {len(result)} уникальных подстрок')

else:
    print('Можно использовать только латинские буквы!')
