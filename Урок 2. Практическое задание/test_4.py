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

def is_int(parametr_x):
    try:
        parametr_x = int(parametr_x)  #SDFA
    except ValueError:
        parametr_x = is_int(input('Вы ввели не цело число, введите, пожалуйста, число: '))
    return parametr_x




def get_summ(elements_left, current_summ = 1 , current_item = 1  ):
    if current_summ == 1:
        elements_left -= 1
        if elements_left == 0:
            print('сумма равна 1 ')

    current_item *= - 0.5
    current_summ += current_item
    elements_left = elements_left - 1
    if elements_left == 0:
        print('сумма равна ', current_summ )
        return
    get_summ(elements_left, current_summ, current_item)

get_summ(is_int(input('Введите колл-во элементов ряда ')))