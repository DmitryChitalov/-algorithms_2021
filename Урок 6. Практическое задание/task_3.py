"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile


@profile
def check_recur(mul_num):
    def factorial(number):
        if number == 1:
            return number
        else:
            return number * factorial(number - 1)
    return factorial(mul_num)


print(check_recur(900))

'''
Думаю, минус данного варианта профилирования состоит в том, что мы не можем четко
увидеть, сколько памяти занимает каждый из вызовов функции
'''