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


def enter_number():
    try:
        val = abs(int(input('Please enter some number\n')))
    except ValueError:
        print("Error you've entered incorrect value")
        return enter_number()
    return val


def count_figures(num, count_1=0, count_2=0):
    if num != 0:
        if num % 2 == 0:
            count_1 += 1
        else:
            count_2 += 1
        return count_figures(num // 10, count_1, count_2)
    return print(f'Number of even numbers = {count_1}\nNumber of uneven numbers = {count_2}')


number = enter_number()
count_figures(number)
