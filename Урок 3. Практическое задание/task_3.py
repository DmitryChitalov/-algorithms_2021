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


def verify_func(string):
    verify_string = string.lower ()
    string_set = set ()
    print (f'Строка "{verify_string}" имеет длину {len (verify_string)} символов')
    for i in range (len (verify_string)):
        for j in range (len (verify_string) - 1 if i == 0 else len (verify_string), i, -1):
            string_set.add (hash (verify_string[i:j]))
            print (verify_string[i:j], i, j)
    return len (string_set)


def recursive_func(string, start=0, stop=0, string_set=()):
    string_set = set(string_set)
    start = len(string)
    if start < 0:
        return len(string_set)
    else:
        string_set.add(hash (string[start:stop]))
        stop -= 1
    start -= 1
    return recursive_func (string, start, stop, string_set)


if __name__ == '__main__':
    print (f'Количество уникальных подстрок в этой строке: {verify_func (str (input ("Введите строку: ")))}')
    main_data = (str (input ("Введите строку: ")))
    print (f'Количество уникальных подстрок в этой строке: '
           f'{recursive_func (main_data, len(main_data), len(main_data))}')
