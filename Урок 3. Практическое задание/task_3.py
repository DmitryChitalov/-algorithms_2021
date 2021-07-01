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


def check_str(str_value):
    result = set(hash(str_value[i:j]) for i in range(len(str_value)) for j in range(len(str_value)))
    return result


if __name__ == '__main__':
    print(f"{check_str('papa')}\nCount of elements: {len(check_str('papa'))}")
