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
def sub_count(my_str):
    sub_set = set()
    for num in range(1, len(my_str)):
        for num2 in range(len(my_str)):
            str_sub = my_str[num:num2+num]
            sub_set.add(hash(str_sub))
    return len(sub_set)


print(sub_count('papa'))
print(sub_count('рар'))
print(sub_count('pa'))
print(sub_count('ap'))
print(sub_count('apa'))
print(sub_count('p'))
print(sub_count('a'))