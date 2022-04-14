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
def get_num():
    try:
        num = int(input('Введите число элементов ряда: '))
        return num
    except ValueError:
        print('На число не похоже. Попробуйте еще раз.')

def get_sum(cur_num, count):
    return cur_num + get_sum(cur_num+1, count) if cur_num < count else cur_num

num = get_num()
if num is not None:
    row_sum = get_sum(1, num)
    sum_expr = num*(num+1)/2
    if row_sum == sum_expr:
        print('Ура! Формула для ряда верная. Сумма ряда:', row_sum)
    else:
        print('Где то косяяк')
