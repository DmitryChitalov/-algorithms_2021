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


def get_digit_stats(number, evens_count=0, odds_count=0):
    if number == 0:
        return evens_count, odds_count
    else:
        current_number = number % 10
        number = number // 10
        if current_number % 2 == 0:
            evens_count += 1  # even
        else:
            odds_count += 1  # odd
        return get_digit_stats(number, evens_count, odds_count)
            

try:
    string_to_process = int(input("Input number: "))
    print(get_digit_stats(string_to_process))
except ValueError:
    print("Only digits are allowed")
