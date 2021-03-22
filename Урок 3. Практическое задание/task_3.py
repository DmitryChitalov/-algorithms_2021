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

# hash?

while True:
    print('-' * 50)
    string = input('Для выхода введите "0"\n'
                   'Введите строчное значение: ')
    #tring = 'papa'

    if string == '0':
        break
    string_list = []
    len_list = len(string)

    for i in range(len(string)):
        a = string[len(string) - len_list:]
        len_sub = 0
        for j in range(len(a)):
            b = a[:len(a) - len_sub]
            string_list.append(hash(b))
            len_sub += 1
        len_list -= 1

    string_set = set(string_list[1:])
    print(f'Введенная строка имеет {len(string_set)} подстр.')










