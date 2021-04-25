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


def task04(item_count, next_item, item_summ, items_list):

    if item_count == 0:
        print(f'Сумма элементов числового ряда {items_list} = {item_summ}')
        return

    items_list.append(next_item)
    item_summ += next_item
    item_count -= 1

    task04(item_count, next_item / (-2), item_summ, items_list)


while True:
    input_value = input('Введите количество элементов числового ряда, либо 0 для завершения: ')
    if input_value == '0':
        break

    try:
        input_value = int(input_value)
    except ValueError:
        print('Введено некорректное значение!')
    else:
        task04(input_value, 1, 0, [])
