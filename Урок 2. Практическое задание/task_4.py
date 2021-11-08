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


def get_number_series(input_number, element_value=1, sum_elements=0):
    """
    Подсчёт суммы элементов числового ряда.
    :param input_number: Количесво элементов числового ряда.
    :param element_value: Значение элемента.
    :param sum_elements: Сумма элементов.
    :return:
    """
    if input_number == 0:
        return sum_elements
    else:
        # print(element_value)
        sum_elements += element_value
        element_value *= -0.5
        input_number -= 1
        return get_number_series(input_number, element_value, sum_elements)


number = int(input("Введите количество элементов: \n"))
print(f"Вы ввели: {number}\n")
print(get_number_series(number))
