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


def count_even_odd(int_obj):
    global count_even, count_odd
    if int_obj > 0:
        if int_obj % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        int_obj //= 10
        return count_even_odd(int_obj)
    else:
        return print(f'Количество четных и нечетных цифр в числе равно: ({count_even}, {count_odd})')


ind = True
count_even, count_odd = 0, 0

while ind:
    try:
        number = int(input('Введите натуральное число: '))
        ind = False
    except ValueError:
        print('Ошибка ввода числа!')

count_even_odd(number)
