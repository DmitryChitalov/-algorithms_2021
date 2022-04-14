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

def get_num():
    try:
        num = int(input('Введите число: '))
        return num
    except ValueError:
        print('На число не похоже. Попробуйте еще раз.')


def check_numbers(num, count_even, count_odd):
    base = 10
    if num >= base:
        tail = num % base
        if tail % 2 > 0:
            count_odd += 1
        else:
            count_even += 1
        check_numbers(num // base, count_even, count_odd)
    else:
        if num % 2 > 0:
            count_odd += 1
        else:
            count_even += 1
        print(f'Количество четных и нечетных цифр в числе равно: ({count_even}, {count_odd})')

num = get_num()
if num is not None:
    check_numbers(num, 0, 0)