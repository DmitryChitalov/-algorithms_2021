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


def strip(string: str):
    substr_list = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substr_list.append(string[i:j])
    substr_list.remove(string)
    return substr_list


def uniq(lst):
    uniq_substr = set()
    for item in lst:
        uniq_substr.add(hash(item))
    print('Уникальных элементов: ', len(uniq_substr))


print(strip('abc'))
print(uniq(strip('abc')))
print(strip('abcdef'))
print(uniq(strip('abcdef')))
print(strip('papa'))
print(uniq(strip('papa')))
print(strip('aaaaaaaaa'))
print(uniq(strip('aaaaaaaaa')))