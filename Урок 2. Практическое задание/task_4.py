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

# solution for the task
# def sum_n(base: float, n: int) -> float:
#     if n > 1:
#         return base + sum_n(base / -2, n - 1)
#     else:
#         return base


# solution optimised to be used in task 7
def sum_n(base: float, n: int, func) -> float:
    if n > 1:
        return base + sum_n(func(base), n - 1, func)
    else:
        return base


def get_next(num: float) -> float:
    return num / -2


if __name__ == '__main__':
    # print(sum_n(1, int(input("set N nuber:"))))
    print(sum_n(1, int(input("set N number:")), get_next))

    for i in range(20):
        print("N:", i, ") = ", sum_n(1, i, get_next))


