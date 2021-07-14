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

my_str = 'helhel'

my_list = []
my_set = set()

for i in range(len(my_str)):
    for j in range(i+1,len(my_str)+1):
        if my_str[i:j] != my_str:
            my_list.append(my_str[i:j])
            if hash(my_str[i:j]) not in my_set:
                #print(f'hash = {hash(my_str[i:j])}')
                my_set.add(my_str[i:j])

print(f'Для проверки выводим все варианты, кроме слова целоком\n{my_list}')
print(f'Итоговое множество без повторов\n{my_set}')


