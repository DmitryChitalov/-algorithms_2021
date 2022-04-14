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


# def get_set_sum(n: int, current_num=1, total_sum=1):
#     if current_num == n:
#         return total_sum
#
#     current_num += 1
#     total_sum += current_num
#
#     return get_set_sum(n, current_num, total_sum)
#
#
# while True:
#     try:
#         user_n = int(input('Введите любое натуральное число: '))
#         assert user_n > 0
#         break
#     except ValueError:
#         print('Вы вместо числа ввели строку (((. Исправьтесь')
#     except AssertionError:
#         print('Число должно быть > 0')
#
#
# if __name__ == '__main__':
#     print(f'1+2+...+{user_n} = {user_n}({user_n}+1)/2\n'
#           f'{get_set_sum(user_n) == (user_n * (user_n + 1) / 2)}')
#
# Пример:
# для n = 5
# 1+2+3+4+5 = 5(5+1)/2

def recur(n):
    return n if n < 1 else n + recur(n - 1)


while True:
    try:
        user_n = int(input('Введите любое натуральное число: '))
        assert user_n > 0
        break
    except ValueError:
        print('Вы вместо числа ввели строку (((. Исправьтесь')
    except AssertionError:
        print('Число должно быть > 0')

print(f'1+2+...+{user_n} = {user_n}({user_n}+1)/2\n'
      f'{recur(user_n) == (user_n * (user_n + 1) / 2)}')
