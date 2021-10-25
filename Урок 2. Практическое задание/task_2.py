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


class Count:
    def __init__(self):
        self.even_num = 0
        self.odd_num = 0

    def plus_even(self):
        self.even_num += 1

    def plus_odd(self):
        self.odd_num += 1

    def result_even(self):
        return self.even_num

    def result_odd(self):
        return self.odd_num


c_obj = Count()


def count_numbers(number):
    try:
        if len(number) == 0:
            return f'Количество четных числе равно {c_obj.result_even()}. ' \
                   f'Количество нечетных числел равно {c_obj.result_odd()}.'
        else:
            if (int(number) // 10 ** (len(number) - 1)) % 2 == 0:
                c_obj.plus_even()
                return count_numbers(number[1:])
            else:
                c_obj.plus_odd()
                return count_numbers(number[1:])
    except ValueError:
        print('Вы ввели не число.')
        return count_numbers(input('Введите натуральное число: '))


print(count_numbers(input('Введите натуральное число: ')))
