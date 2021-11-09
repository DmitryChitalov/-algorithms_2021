'''
Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
'''


def turn_over(number, reversed_number=''):
    if number == 0:
        return reversed_number
    else:
        digit = number % 10
        return turn_over(number // 10, reversed_number + str(digit))


numb = int(input('Введите число, которое требуется перевернуть: '))
print(f'Перевернутое число: {turn_over(numb)}')
