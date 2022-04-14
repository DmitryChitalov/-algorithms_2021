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


s = input("Введите строку: ")
res=set()
n=len(s)
for i in range(n):
    if i == 0:
        n=len(s)-1
    else:
        n=len(s)
    for j in range(n,i,-1):
        res.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())


print(f"Колличество подстрок {len(res)}")