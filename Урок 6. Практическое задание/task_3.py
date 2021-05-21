"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""


from memory_profiler import profile


@profile
def reverse(num):
    def revers_numbers(number):
        if number == 0:
            return ''
        else:
            return str(number % 10) + revers_numbers(number // 10)

    return revers_numbers(num)


reverse(1230)


'''
Чтобы избежать срабатывание декоратора при каждом вызове рекурсии необходимо
поместить функцию с рекурсией в другую функцию.
'''

