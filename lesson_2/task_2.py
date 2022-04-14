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

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_odd_even(number):
    """
    используя рекурсию подсчитаем количество четных и нечетных цифр в числе
    """

    if number < 10:
        return (1, 0) if number % 2 else (0, 1)

    odd, even = sum_odd_even(number // 10)

    if number % 2:
        odd += 1
    else:
        even += 1

    return odd, even


print(123, sum_odd_even(123))
print(13579, sum_odd_even(13579))
print(24680, sum_odd_even(24680))

while True:
    try:
        number = int(input('Введите число: '))
    except ValueError:
        print('Вы ввели не натуральное число! Повторите ввод!')
        continue

    print('Количество нечетных и четных цифр в числе равно: ', sum_odd_even(number))
