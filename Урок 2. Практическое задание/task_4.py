"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def sum_of_n(user_count, base_int=1, result=1, count=1):
    if user_count  == 1:
        return result
    if count < user_count:
        element = 0 - (base_int / 2)
        result += element
        base_int = element
        count += 1
        return sum_of_n(user_count, base_int, result, count)
    return result

if __name__ == '__main__':
    user_count = input('Введите количество элементов: ')
    try:
        user_count = int(user_count)
    except Exception:
        print('Вы ввели не число, а строку! Исправьтесь.')

    print(f'Результат: {sum_of_n(user_count)}')

