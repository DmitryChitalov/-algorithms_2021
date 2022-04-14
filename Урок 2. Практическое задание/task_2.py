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

from functools import reduce

def even_odd_collector(arrays, x):
    """
    :param arrays: Массив вида [0: [нечетные числа], 1: [четные числа]]
    :param x: Число
    :return: Массив вида [0: [нечетные числа], 1: [четные числа]]
    """
    x = int(x)
    arrays[x % 2].append(x)
    return arrays

n = input('Введите число: ')
(odd, even) = reduce(even_odd_collector, n, [[], []])
print('{} нечетных цифр {} и {} четных цифр {}'.format(len(even), even, len(odd), odd))
