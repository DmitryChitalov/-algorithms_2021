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
str_set = set()
str_set1 = set()


def str_set_fun(string):
    """Функция вычисляющая количество уникальных подстрок в строке"""
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if len(string[i:j]) != len(string):
                str_set.add(hash(string[i:j]))
                str_set1.add(string[i:j])
    return len(str_set)


print(str_set_fun('papa'))
print(str_set)
print(str_set1)
