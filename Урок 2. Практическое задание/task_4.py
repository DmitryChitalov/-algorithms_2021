"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Массив в этом задании строить нельзя!
Нужно решить без него!

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_num(end_num=int(input('Введите число: ')), count_num=1, a=1, result=0.5):
    if count_num == end_num:
        return a
    elif count_num % 2 == 0:
        return sum_num(end_num, count_num+1, a+result, result/2)
    elif count_num % 2 == 1:
        return sum_num(end_num, count_num+1, a-result, result/2)


print(sum_num())
