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
    ''' Функция проверки уникальных строк '''
    verify_string = string.lower ()
    string_set = set ()
    print (f'Строка "{verify_string}" имеет длину {len (verify_string)} символов')
    for i in range (len (verify_string)):
        for j in range (len (verify_string) - 1 if i == 0 else len (verify_string), i, -1):
            string_set.add (hash (verify_string[i:j]))
    return len (string_set)



if __name__ == '__main__':
    print (f'Количество уникальных подстрок в этой строке: '
           f'{verify_func (str (input ("Введите строку: ")))}')
