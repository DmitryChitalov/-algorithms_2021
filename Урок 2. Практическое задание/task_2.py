"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
# можно сделать следующим образом
'''
def func_recursion_two(number, even_numbers=0, odd_numbers=0):
    if number == 0:
        return even_numbers, odd_numbers
    else:
        cur_n = number % 10
        number = number // 10
        if cur_n % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
        return func_recursion_two(number, even_numbers, odd_numbers)

необходимо сделать проверку на try except ValueError
'''

def func_recursion_two(number):
    global even_numbers, odd_numbers
    if number < 10:
        if number % 2:
            odd_numbers += 1
        else:
            even_numbers += 1
    else:
        func_recursion_two (number // 10)
        if (number % 10) % 2:
            odd_numbers += 1
        else:
            even_numbers += 1
    return even_numbers, odd_numbers


if __name__ == '__main__':
    even_numbers, odd_numbers = 0, 0
    print (f'Количество четных и нечетных цифр в числе равно: ',
           func_recursion_two (int (input (f'Введите число: '))))
