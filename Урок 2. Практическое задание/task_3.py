"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

Не забудьте проверить и на числах, заканчивающихся нулем.
Пример:
Введите число, которое требуется перевернуть: 1230
Перевернутое число: 0321

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def number_back(num, num_over=''):
    if num == 0:
        print(f'Перевернутое число: {num_over}')
    else:
        number_back(num // 10, num_over + str(num % 10))


try:
    number_back(int(input('Введите число: ')))
except:
    print(f'Ввели не правильное число! Попробуйте еще раз!')
    number_back(int(input('Введите число: ')))
