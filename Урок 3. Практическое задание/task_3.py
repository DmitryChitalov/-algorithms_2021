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
import hashlib

str_in = input('Введите строку: ')

subs_hash = set()
subs_md5 = set()
subs_sha1 = set()
subs_sha256 = set()

str_len = len(str_in)
if str_len > 0:
    for i in range(str_len):
        for j in range(i, str_len):
            subs_hash.add(hash(str_in[i:j+1]))
        for j in range(i, str_len):
            subs_md5.add(hashlib.md5(str_in[i:j+1].encode('utf-8')).hexdigest())
        for j in range(i, str_len):
            subs_sha1.add(hashlib.sha1(str_in[i:j+1].encode('utf-8')).hexdigest())
        for j in range(i, str_len):
            subs_sha256.add(hashlib.sha256(str_in[i:j + 1].encode('utf-8')).hexdigest())

    print('hash. Количество неповторяющихся подстрок - ', len(list(subs_hash)) - 1)
    print('md5. Количество неповторяющихся подстрок - ', len(list(subs_md5)) - 1)
    print('sha1. Количество неповторяющихся подстрок - ', len(list(subs_sha1)) - 1)
    print('sha256. Количество неповторяющихся подстрок - ', len(list(subs_sha256)) - 1)
else:
    print('Вы ввели пустую строку')
