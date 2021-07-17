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


def find_substrings(string):
    my_set = set()
    my_set2 = set()
    for i in range(len(string)):
        for j in range(len(string)):
            t_slice = string[i:j + 1]
            if len(t_slice) > 0 and t_slice != string:
                my_set2.add(t_slice)  # только для наглядности
                my_set.add(hash(t_slice))
    for m in my_set2:
        print(m)
    return len(my_set)


temp_str = input("Введите строку для поиска построк: ")
print(f'Итого: {find_substrings(temp_str)} подстрок в строке {temp_str}')
