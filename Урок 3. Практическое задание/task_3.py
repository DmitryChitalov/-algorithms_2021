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


class Substring:
    def __init__(self, my_str):
        self.my_set = set()
        self.my_str = my_str

    def substring(self):
        for k in range(len(self.my_str)):
            for x in range(k + 1, len(self.my_str) + 1):
                if self.my_str[k:x] != self.my_str:
                    self.my_set.add(hashlib.md5(self.my_str[k:x].encode()).hexdigest())
                    print(self.my_str[k:x], end=' ')


s = Substring('kue')
s.substring()
print(f'\nКоличество элементов в множестве: {len(s.my_set)}')
