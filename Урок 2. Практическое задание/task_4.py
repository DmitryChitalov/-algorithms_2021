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


def get_sum(n, num, i=0, common_sum=0):
    if n == i:
        return print(f'Количество элементов: {n}, их сумма: {common_sum}')
    else:
        return get_sum(n, num / 2 * -1, i + 1, common_sum + num)


if __name__ == '__main__':
    while True:
        try:
            get_sum(int(input('Введите количество элементов:')), 1)
            break
        except ValueError:
            print('Вы вместо числа ввели строку (((')
