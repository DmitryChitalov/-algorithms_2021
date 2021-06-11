from memory_profiler import profile


# @profile
def odd_even_num(num, even=0, odd=0):
    if num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
        return odd_even_num(num, even, odd)
    else:
        return print(f"В вашем числе: четных цифр {even}, нечетных {odd}")


odd_even_num(765987)

"""
При профилировании рекурсии, функция декоратор будет вызываться каждый раз когда в теле функции
будет происходить рекурсивный вызов.
"""


@profile
def profile_recursion(num, even=0, odd=0):
    def odd_even_num(num, even=0, odd=0):
        if num > 0:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
            num = num // 10
            return odd_even_num(num, even, odd)
        else:
            return print(f"В вашем числе: четных цифр {even}, нечетных {odd}")


profile_recursion(765987)

"""
Для решения этой проблемы достаточно профилируемую функцию с рекурсией поместить в другую функцию.
"""