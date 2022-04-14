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

def substring(string):
    substrings = []
    string_len = len(string)
    for i in range(string_len):
        substrings.append(hash(string[i]))
        if i < string_len:
            temp_str = string[i + 1:]
            while temp_str:
                if i == 0:
                    temp_str = temp_str[:-1]
                substrings.append(hash(string[i] + temp_str))
                temp_str = temp_str[:-1]
    return print(f'Количество подстрок: {len(set(substrings))}')

#Не понял только зачем здесь множество? Если множество, то тогда хэш не нужен. Да и хэш тоже не понятно зачем.

substring('papa')
