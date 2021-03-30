"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
"""


def get_special_sum(number, current_sum=1.0):
    if number <= 1:
        return current_sum
    number -= 1
    new_sum = current_sum / -2
    return current_sum + get_special_sum(number, new_sum)


try:
    number_of_elements = int(input("Number of elements: "))
    print(get_special_sum(number_of_elements))
except ValueError:
    print("Only digits are allowed")
