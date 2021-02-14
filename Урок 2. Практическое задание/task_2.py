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


# Вариант 1. Выводим списки четных и нечетных чисел
def even_or_odd_numbers(number, even_numbers=None, odd_numbers=None):
    if even_numbers is None:
        even_numbers = []
    if odd_numbers is None:
        odd_numbers = []

    if number == 0:
        return f'Четные числа: {even_numbers}, \nНечетные числа: {odd_numbers}.\nВсего четных чисел - {len(even_numbers)}, нечетных - {len(odd_numbers)}'
    else:
        el = number % 10
        number = number // 10
        if el % 2 == 0:
            even_numbers.append(el)
        else:
            odd_numbers.append(el)
        return even_or_odd_numbers(number, even_numbers, odd_numbers)


print(even_or_odd_numbers(34560))


# Вариант 2. Выводим только количество четных и нечетных чисел
def even_or_odd_numbers2(number, even=0, odd=0):
    if number == 0:
        return f'Четных чисел: {even}; нечетных чисел: {odd}'
    else:
        el = number % 10
        if el % 2 == 0:
            even += 1
            return even_or_odd_numbers2(number // 10, even, odd)
        else:
            odd += 1
            return even_or_odd_numbers2(number // 10, even, odd)


print(even_or_odd_numbers2(34560))

