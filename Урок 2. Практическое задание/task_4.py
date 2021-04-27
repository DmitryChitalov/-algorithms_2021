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


# Рекурсивная функция для подсчета элементов в ряде чисел
# def sum_series(n, base=1):
def sum_series(n, base):
    if n == 0:  # базовый(нулевой) случай
        return f'сумма элементов равна 0'
    if n == 1:  # базовый случай
        return base
    while n > 0:
        return base + sum_series(n-1, base*-0.5)


def program():
    try:
        num = int(input('Введите количество элементов: '))
        rez = sum_series(num, 1)
        # rez = sum_series(num)
        print(f'Количество элементов - {num} \nсумма элементов - {rez}')
    except ValueError:
        print('Необходимо количество!!!')
        program()


if __name__ == '__main__':
    program()
