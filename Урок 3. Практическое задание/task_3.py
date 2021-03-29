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

substring_set = set()

def substring_finder(input_string,count):
    print("*"*25)
    for i in range(len(input_string)-count+1):
        subs = input_string[i:(i+count)]        
        substring_set.add((hash(subs),subs))
    if count < len(input_string)-1:
        substring_finder(input_string,count+1)        
    else:
        print(f"\nНайдены {len(substring_set)} подстрок строки: '{input_string}'")


###################################################################
res = substring_finder('papapa',1)
print(res)
for i in substring_set:
    print(i)
