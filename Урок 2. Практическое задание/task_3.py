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


# в общем, пытался я это вот так сделать, но не взлетает оно.
# number_to_reverse = 0
#
#
# def reversing_numbers(number):
#     if number < 10:
#         return str(number)
#     else:
#         remainder = number % 10
#         number = (number * 10) + remainder
#
#         reversing_numbers(number // 10)
#         return str(number) + str(reversing_numbers(remainder))
#
#
# number_to_reverse = reversing_numbers(int(input('Введите число для реверса ')))
# print("Reversed number is" + number_to_reverse)


def reverse_numb(numb):
    rest_numb, numeral = divmod(numb, 10)  # про divmod я забыл напрочь
    if rest_numb == 0:
        return str(numeral)
    else:
        return str(numeral) + str(reverse_numb(rest_numb))


number = int(input("Число для реверса: "))
print(reverse_numb(number))
