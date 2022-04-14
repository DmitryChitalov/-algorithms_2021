from memory_profiler import profile
"""Приведу пример @profile на рекурсии из урока 2 задание 2"""
@profile
def profile_rec_stop(*args):
    def amount_of_even_odd(number: int, even: int = 0, odd: int = 0):
        if number != 0:
            if (number % 10) % 2 == 0:
                even += 1
            else:
                odd += 1
            return amount_of_even_odd(number // 10, even, odd)
        else:
            print(f'Количество четных цифр: {even}, нечетных цифр {odd})')
            return

    return amount_of_even_odd(*args)
print(profile_rec_stop(12345678910111213))

"""
На мой взгляд для того чтобы  @profile не обрабатывал каждую итерацию, можно просто 
вставить рекурсию (ф точнее ее функцию) в еще одну функцию

Вот итог:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     2     19.7 MiB     19.7 MiB           1   @profile
     3                                         def profile_rec_stop(*args):
     4     19.8 MiB      0.0 MiB          19       def amount_of_even_odd(number: int, even: int = 0, odd: int = 0):
     5     19.8 MiB      0.0 MiB          18           if number != 0:
     6     19.8 MiB      0.0 MiB          17               if (number % 10) % 2 == 0:
     7     19.8 MiB      0.0 MiB           6                   even += 1
     8                                                     else:
     9     19.8 MiB      0.0 MiB          11                   odd += 1
    10     19.8 MiB      0.0 MiB          17               return amount_of_even_odd(number // 10, even, odd)
    11                                                 else:
    12     19.8 MiB      0.0 MiB           1               print(f'Количество четных цифр: {even}, нечетных цифр {odd})')
    13     19.8 MiB      0.0 MiB           1               return
    14                                         
    15     19.8 MiB      0.0 MiB           1       return amount_of_even_odd(*args)


"""