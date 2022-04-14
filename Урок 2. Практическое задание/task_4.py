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


def sum_of_elements(count_of_elements, sum_value=1, all_sum=1):
    if count_of_elements == 1:
        return all_sum
    count_of_elements -= 1
    sum_value = sum_value / -2
    all_sum += sum_value
    return sum_of_elements(count_of_elements, sum_value, all_sum)


cnt = input("Введите количество элементов: ")
if cnt.isdigit():
    print(sum_of_elements(int(cnt)))
