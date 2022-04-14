"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""


from memory_profiler import profile


@profile
def new_fun():
    def num_even_odd(number, even=0, odd=0):
        if number == 0:
            print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
        else:
            if number % 2 == 0:
                even += 1
            else:
                odd += 1
            return num_even_odd(number // 10, even, odd)


# number = int(input('Введите число: '))
# new_fun(number)
print(new_fun())

"""
 Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    13     19.0 MiB     19.0 MiB           1   @profile
    14                                         def new_fun():
    15     19.0 MiB      0.0 MiB           1       def num_even_odd(number, even=0, odd=0):
    16                                                 if number == 0:
    17                                                     print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
    18                                                 else:
    19                                                     if number % 2 == 0:
    20                                                         even += 1
    21                                                     else:
    22                                                         odd += 1
    23                                                     return num_even_odd(number // 10, even, odd)
    
    

Чтобы сделать корректную профилировку рекурсивной функции, необходимо ее вложить в другую функцию.
"""