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


def get_list_of_even_and_odd(number: int, even_digits=0, odd_digits=0):
    """
        Принимает в качестве агрумента натуральное число и распечатывает количество четных и нечетных цифр в нём
    """
    remainder = number % 2

    if len(str(number)) == 1:  # базовый случай, счётчики к этому времени заполнятся
        if remainder:
            odd_digits += 1
            print(f"Количество четных и нечетных цифр в числе равно: ({even_digits}, {odd_digits})")
            return
        else:  # remainder == 0
            even_digits += 1
            print(f"Количество четных и нечетных цифр в числе равно: ({even_digits}, {odd_digits})")
            return

    if remainder:
        odd_digits += 1
        new_number = number // 10
    else:  # remainder == 0  - чётное
        even_digits += 1
        new_number = number // 10
    return get_list_of_even_and_odd(new_number, even_digits, odd_digits)


def get_natural_number():
    """ Запрашивает у пользователя натуральное число пока пользователь не введёт корректно"""
    try:
        user_number = int(input('Введите натуральное число: '))
    except ValueError:
        print('Попробуйте снова.')
        return get_natural_number()
    if user_number <= 0:
        print('Попробуйте снова.')
        return get_natural_number()
    else:
        return user_number


get_list_of_even_and_odd(get_natural_number())
