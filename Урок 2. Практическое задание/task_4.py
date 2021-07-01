"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Массив в этом задании строить не нужно!
Нужно решить без него!

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def progression_sum(n, iter_counter=0, number=1.0, total_sum=0.0):
    if n == 0 or n == iter_counter:
        return f"Количество элементов: {n}, их сумма: {total_sum}"
    elif iter_counter < n:
        return progression_sum(n=n, iter_counter=iter_counter+1, number=number/2*(-1), total_sum=total_sum + number)


def number_request():   # Добавил функцию для запроса ввода и простейшей проверки вводимого числа
    try:
        n = int(input("Введите количество элементов: "))
        return n
    except ValueError:
        print("Вы должны ввести натрульное число")
        return number_request()


if __name__ == '__main__':
    print(progression_sum(number_request()))
