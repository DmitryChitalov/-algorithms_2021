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

el_numbers = int(input("Введите число "))


def number_elements(number, reference_point, zero_variable):
    if number == 0:
        print("Вычисление закончено")
    else:
        zero_variable = zero_variable + reference_point
        return number_elements(number - 1, -(reference_point / 2), zero_variable)
    print("Итоговое значение - ", zero_variable)


if __name__ == '__main__':
    number_elements(el_numbers, 1, 0)
