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
# Ряд сумм получается: 0.5 0.75 0.625

def input_digit():
    try:
        number = abs(int(input("Введите колличество элементов: ")))
    except ValueError:
        return input_digit()
    return number

def summ_of_row(idx, current_elem=1, summ=1):
    if idx-1 == 0:
        return summ
    else:
        # решение через переменные, которые после поместила в вызов следующего шага рекурсии
        # print("summ", summ)
        # print("current_elem", current_elem)
        # current_elem = (current_elem / 2) * (-1)
        # summ += current_elem
        # print(summ)
        return summ_of_row(idx-1, (current_elem / 2) * (-1), summ + (current_elem / 2) * (-1))

def summ_of_row_one_row(idx, elem=1, summ=1):
    # решение через тернарный оператор в одну строчку
    return summ if idx-1 == 0 else summ_of_row_one_row(idx-1, (elem / 2) * (-1), summ + (elem / 2) * (-1))

num_input = input_digit()
# print(f"Колличество элементов: {num_input}, их сумма {summ_of_row(num_input)}")
print(f"Колличество элементов: {num_input}, их сумма {summ_of_row_one_row(num_input)}")
