"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Подсказка:
Правой части в рекурсии быть не должно!!! Необходимо сравнить результат, который даст рекурсивная ф-ция
со значением, полученным в правой части (здесь нужно просто подставить n и подсчитать)

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def get_sum(number, counter=0, sum_numbers=0):
    if number == counter:
        return sum_numbers
    else:
        counter += 1
        sum_numbers += counter
        return get_sum(number, counter, sum_numbers)


my_number = 15
calc_rec_function = get_sum(my_number)
calc_formula = int(my_number*(my_number+1)/2)
print(f"Сумма элементов от 1 до {my_number} = {calc_rec_function}")
print(f"{my_number} * ({my_number} + 1) / 2 = {calc_formula}")
print(f"Равенство верно. Сумма элементов от 1 до {my_number} = {my_number} * ({my_number} + 1) / 2") \
    if calc_rec_function == calc_formula else print("Равенство неверно.")
