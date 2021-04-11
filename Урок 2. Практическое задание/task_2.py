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

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def even_odd_counter(number):
    if number < 10:
        if number % 2 == 0:
            return [1, 0]
        else:
            return [0, 1]
    else:
        if number % 2 == 0:
            return [even_odd_counter(number // 10)[0] + 1, even_odd_counter(number // 10)[1]]
        else:
            return [even_odd_counter(number // 10)[0], even_odd_counter(number // 10)[1] + 1]


print(f'Количество четных и нечетных цифр в числе равно: {even_odd_counter(int(input("Введите число: ")))}.')


"""
Если я все учел, доставать цифру не обязательно - если последняя цифра числа четная, то и все число четное, 
значит нам достаточно проверять четность самого числа. Если я что-то упустил - прошу указать.
"""