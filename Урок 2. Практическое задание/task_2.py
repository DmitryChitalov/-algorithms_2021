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


def check(num_in, div_val=0, mod_val=0):
    if num_in > 0:
        if num_in % 10 % 2 == 0:
            div_val += 1
        else:
            mod_val += 1
        check(num_in // 10, div_val, mod_val)
    else:
        print(f'Количество четных и нечетных цифр в числе равно: ({div_val}, {mod_val})')


def main(att=3):
    try:
        x = int(input('Введите произвольное число: '))
        check(x)
    except:
        att -= 1
        print(f'Вы точно ввели число? Попробуйте еще раз... (Попыток осталось: {att}) ')
        main(att)


main(3)
