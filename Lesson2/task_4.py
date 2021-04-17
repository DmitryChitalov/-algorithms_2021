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

'''
for i in range(n):
    el = (-1) ** n / (2 ** n)
    print(el)
    summ += el
    print(summ)'''


def row(n):

    if n == 1:
        return 1
    elif n > 1:
        n -= 1
        return row(n) + ((-0.5) ** n)


print(row(1))
print(row(2))
print(row(3))
print(row(4))


def enter_number():

    try:
        custom_numbers = int(input('Enter a number of elements in row: '))
        if custom_numbers < 1:
            raise ValueError

    except ValueError:
        print('Please enter only integer numbers bigger than zero!')
    else:
        print(f'Sum of {custom_numbers} elements in row is equal {row(custom_numbers)}')
        return
    enter_number()


enter_number()
