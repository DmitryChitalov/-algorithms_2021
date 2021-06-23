"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile

@profile
def reverse1(num):
    if num == 0:
       return ''
    else:
       return str(num % 10) + reverse1(num // 10)
    return reverse1(num)

@profile
def reverse2(num):
    def revers_numbers(number):
        if number == 0:
            return ''
        else:
            return str(number % 10) + revers_numbers(number // 10)

    return revers_numbers(num)

reverse1(100500)
reverse2(100500)


'''
Если попытаться профилировать функцию с рекурсией, то будет профилироваться каждый вызов рекурсии. 
Пример, профилирование функции reverse1.
 
Для того, чтобы избежать профилирования каждого вызова рекурсии, необходимо рекурсию обернуть в еще одну функцию.
Пример, профилирование функции reverse2.
'''