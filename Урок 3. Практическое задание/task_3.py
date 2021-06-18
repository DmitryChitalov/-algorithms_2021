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
# hash вариант 1
print('вариант 1 через хеш')
string_hash = 'рара'
result_hash = []
res_hash = [hash(string_hash)]
for i in range(len(string_hash)):
    for j in range(len(string_hash[i:])):
        if hash(string_hash[i:][:j+1]) not in res_hash:
            result_hash.append(string_hash[i:][:j+1])
            res_hash.append(hash(string_hash[i:][:j+1]))

print(f'количество различных (уникальных) подстрок {len(result_hash)}')
print(result_hash)

# set вариант 2
print('\nвариант 2 через множества')
s = 'рара'
res = set()
for i in range(len(s)):
    for j in range(len(s[i:])):
        res.add(s[i:][:j+1])
res.remove(s)

print(f'количество различных (уникальных) подстрок {len(res)}')
print(res)
