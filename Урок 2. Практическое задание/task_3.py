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
'''
можно сделать так
def func_recursion_three(number):
    rest_number, numeral = divmod(number, 10)
    if rest_number == 0:
        return str(numeral)
    else:
        return str(numeral) + str(func_recursion_three(rest_number))
        
и можно еще и так
def func_recursion_three(number):
    return str(number) if number < 10 else str(number % 10) + def func_recursion_three(number // 10)
'''
def func_recursion_three(number):
    global my_list
    if number < 10:
        my_list.insert(0, number)
    else:
        func_recursion_three (number // 10)
        my_list.insert (0, number % 10)
    return ''.join(map(str, my_list))


if __name__ == '__main__':
    my_list = []
    print (f'Ваше число в перевернутом виде: ',
           func_recursion_three (int (input (f'Введите число: '))))