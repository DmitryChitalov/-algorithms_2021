"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

Не забудьте проверить и на числах, заканчивающихся нулем.
Пример:
Введите число, которое требуется перевернуть: 1230
Перевернутое число: 0321
"""


def inverse(number, inverted_number=0, i=0, j=0):

    if number // 10 == 0 and i == j:
        inverted_number = inverted_number * 10 + number % 10
        print(inverted_number)

    elif number // 10 == 0 and i > j:
        inverted_number = inverted_number * 10 + number % 10
        print(f'0{inverted_number}')

    elif number % 10 == 0 and i == 0:
        return inverse(number // 10, inverted_number * 10 + number % 10, i + 1, j)

    elif number // 10 > 0:
        return inverse(number // 10, inverted_number * 10 + number % 10, i + 1, j + 1)


def inverse_2(number):

    if number == 0:
        return ''
    else:
        return str(number % 10) + inverse_2(number // 10)


inverse(123)
print(inverse_2(123))
inverse(1230)
print(inverse_2(1230))
