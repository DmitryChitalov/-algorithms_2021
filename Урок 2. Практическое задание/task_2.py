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

# Не совсем рабочий вариант


def check_number(num_list):
    num_list = str(num_list)
    if len(num_list) == 1:
        return int(num_list) % 2
    if len(num_list) == 2:
        return int(num_list) // 10 % 2 + (check_number(int(num_list) % 10))
    if len(num_list) > 1:
        return 'Нечётных чисел : ' + str(int(num_list) // 10**(len(num_list) - 1) % 2
                                         + (check_number(int(num_list) % 10**(len(num_list) - 1)))),\
               'Чётных чисел : ' + str(len(num_list) - (int(num_list) // 10**(len(num_list) - 1) % 2
                                       + check_number(int(num_list) % 10**(len(num_list) - 1))))


print(check_number('1099'))

# Рабочий вариант


def check_number_1(num, not_even=0, even=0):
    if num == 0:
        return f'Нечетных: {not_even}\nЧетных: {even}'
    if num % 2 == 0:
        return check_number_1(num // 10, not_even, even+1)
    else:
        return check_number_1(num // 10, not_even+1, even)


print(check_number_1(987123456))
