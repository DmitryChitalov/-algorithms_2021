"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_of_list_numbers(amount, num, i, list_num=[]):

    if i == amount:
        print(f"Ряд чисел из указанного количества элементов - {list_num}, их сумма - {sum(list_num)}")
    elif i < amount:
        list_num.append(num)
        return sum_of_list_numbers(amount, num / 2 * -1, i + 1)


try:
    user_amount = int(input("Введите количество чисел в ряду: "))
    sum_of_list_numbers(user_amount, 1, 0)
except ValueError:
    print("Это не число. Попробуйте еще раз")
