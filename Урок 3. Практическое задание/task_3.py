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


def count_substrings(string):
    result = set()
    for i in range(len(string)):
        count = len(string)
        for j in range(len(string)):
            """
            для отсечения пустых строк и
            для отсечения самой строки, хотя она тоже должна являться подстрокой (но это противоречит условию задачи)
            """
            if len(string[i:count - j]) != 0 and hash(string[i:count - j]) != hash(string):
                result.add(hash(string[i:count - j]))
    return len(result)


if __name__ == '__main__':
    print(count_substrings('aaaan'))  #8
    print(count_substrings('papa'))   #6
    print(count_substrings(''))       #0