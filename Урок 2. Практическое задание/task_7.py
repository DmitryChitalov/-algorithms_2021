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
n = int(input("Enter any natural number: "))


def equal(number):
    if number == 0:
        return number
    else:
        num = number + equal(number - 1)
        return num

print("Equality is true" if equal(n) == n * (n + 1) / 2 else "Equality is not true")
print(f'1+2+...+{n} = {n}({n}+1)/2')
