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


def mirror_for_number(user_number, mirrored=[]):

    if user_number == 0:
        return int(f"".join(map(str, mirrored)))
    else:
        rem_of_div = user_number % 10
        user_number = user_number // 10
        mirrored.append(rem_of_div)
        return mirror_for_number(user_number)


try:
    number = int(input("Введите число, которое требуется перевернуть: "))
    print(f"Перевернутое число: {mirror_for_number(number)}")
except ValueError:
    print("Это не число. Попробуйте еще раз")
