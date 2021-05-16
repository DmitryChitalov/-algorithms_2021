"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""


# Какая фигня с интерпретатором, в новом проекте работает тут не хочет

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func_1():

    for x in range(len(numbers) - 1):
        if numbers[x] < numbers[x + 1]:
            print(f'Минимальное число ' + f'{numbers[x]}')
            break
        else:
            print(f'Минимальное число ' + f'{numbers[x + 1]}')


def func_2():
    print(min(numbers))


func_1()
func_2()
