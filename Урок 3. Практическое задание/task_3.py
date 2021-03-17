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

import hashlib

def count_unique_substrs(input_str):
    substrs_list = []
    for counter in range(1, len(input_str)):
        for i in range(len(input_str)):
            if i + counter <= len(input_str):
                el = input_str[i: i + counter]
                substrs_list.append(el)
            else:
                break

        counter += 1

    print(f'все возможные значения подстрок: {substrs_list}')

    answer = {hashlib.sha256(el.encode()).hexdigest() for el in substrs_list}
    print(f'хеш значения всех уникальных подстрок: {answer}')

    print('все уникальные подстроки:')
    tmp_list = []
    for el in substrs_list:
        if hashlib.sha256(el.encode()).hexdigest() in answer and el not in tmp_list:
            tmp_list.append(el)
            print(el)
    print(f'количество уникальных подстрок: {len(tmp_list)}')


input_str = 'papa'
count_unique_substrs(input_str)