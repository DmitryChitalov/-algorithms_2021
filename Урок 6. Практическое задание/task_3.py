"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""


from memory_profiler import profile


@profile
def num_even_odd(number, even=0, odd=0):
    if number == 0:
        print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
    else:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        return num_even_odd(number // 10, even, odd)


number = int(input('Введите число: '))
num_even_odd(number)


"""
 Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     19.1 MiB     19.1 MiB           3   @profile
    13                                         def num_even_odd(number, even=0, odd=0):
    14     19.1 MiB      0.0 MiB           3       if number == 0:
    15     19.1 MiB      0.0 MiB           1           print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
    16                                             else:
    17     19.1 MiB      0.0 MiB           2           if number % 2 == 0:
    18     19.1 MiB      0.0 MiB           1               even += 1
    19                                                 else:
    20     19.1 MiB      0.0 MiB           1               odd += 1
    21     19.1 MiB      0.0 MiB           2           return num_even_odd(number // 10, even, odd)



На основе измерений можно сделать вывод, что рекурсия в оптимизации не нуждается
"""