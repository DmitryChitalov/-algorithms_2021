"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile


@profile
def wrapper(input_number):
    def turn_over(number, reversed_number=''):
        if number == 0:
            return reversed_number
        else:
            digit = number % 10
            return turn_over(number // 10, reversed_number + str(digit))

    return turn_over(input_number)


numb = int(input('Введите число, которое требуется перевернуть: '))
print(f'Перевернутое число: {wrapper(numb)}')

'''
Проблема заключается в том, что при каждом вызове функции мы получаем новую таблицу. Решается обертыванием рекурсивной 
функции. 
'''
