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


def input_num():
    try:
        num = int(input("Введите натуральное число, которое требуется перевернуть: "))
        if num <= 0:
            print("Ошибка! Число должно быть натуральным.")
            return input_num()
    except ValueError:
        print("Вы ввели не число.")
        return input_num()
    return num_reversed(num)


def num_reversed(num):
    if num < 10:
        # если переданное в функцию число или в процессе рекурсии число
        # стало меньше или равно 9, то возвращаем это число
        print("Перевернутое число: ")
        return str(num)
    # для того, что бы числа у нас не складывались необходимо их перобразовать в строку,
    # тогда получим конкатенацию строк, в нашем случае отдельных цифр числа
    return str(num % 10) + num_reversed(num // 10)


print(input_num())
