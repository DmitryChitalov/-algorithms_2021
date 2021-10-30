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

import random

EVENS = [0, 2, 4, 6, 8]
ODDS = [1, 3, 5, 7, 9]
BASIC = 10


def evenodd(val, sumevens=0, sumodds=0) -> tuple:
    if val > BASIC:
        return evenodd(val // BASIC, sumevens + 1 if val % BASIC in EVENS else sumevens,
                       sumodds + 1 if val % BASIC in ODDS else sumodds)
    return sumevens + 1 if val % BASIC in EVENS else sumevens, \
           sumodds + 1 if val % BASIC in ODDS else sumodds


if __name__ == '__main__':

    # randlist = {random.randint(10000000, 99999999) for x in range(3)}
    randlist = [1234567890, 1111111111, 2222222223]
    for v in randlist:
        print(f'for digit {v} result as', 'even {}, odd {}'.format(*evenodd(v)))
