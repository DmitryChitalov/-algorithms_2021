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


def equal_string(srt_val):
    equal_r={}
    for i in range(len(srt_val)):
        for length in range(1, len(srt_val[i:]) + 1):
            sub_str = srt_val[i:i + length]
            if (srt_val != sub_str):
                equal_r[hash(sub_str)]=sub_str
    print( f"Уникальных строк{len(equal_r)}")
    print( f"{ equal_r.values()}")
    
equal_string('papa')
