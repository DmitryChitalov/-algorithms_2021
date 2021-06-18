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
Правой части в рекурсии быть не должно. Необходимо сравнить результат, который даст рекурсивная ф-ция
со значением, полученным в правой части (здесь нужно просто подставить n и подсчитать)

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def check(element):
    if element == 1 or element == 0:
        return element
    else:
        return element + check(element - 1)


def check_2(element):
    return element if element in (0, 1) else element + check(element - 1)


if __name__ == '__main__':
    while True:
        try:
            num_of_elements = int(input('Введите число элементов'))
            if num_of_elements < 0:
                raise ValueError
            break
        except ValueError:
            print('Ошибка ввода! Это должно быть натуральное число.')

    if check(num_of_elements) == num_of_elements * (num_of_elements + 1) / 2:
        print(f'Равенство верно и равно {check(num_of_elements)}')

    if check_2(num_of_elements) == num_of_elements * (num_of_elements + 1) / 2:
        print(f'Равенство верно и равно {check_2(num_of_elements)}')