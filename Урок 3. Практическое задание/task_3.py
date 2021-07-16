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


def generator(in_str):
    h_dict = {}
    for a in range(0, len(in_str)-1):
        for b in range(a+1, len(in_str) if a == 0 else len(in_str) + 1):
            sub_str = in_str[a: b]
            hsh = hash(sub_str)
            if hsh not in h_dict:
                h_dict[hsh] = sub_str
    print(f'Количество уникальных подстрок в слове {in_str}: {len(h_dict)}')
    for k in h_dict.values():
        print(k)


generator('papa')
