from task_1 import memory_time_profiler
"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


@memory_time_profiler
def profiler_recursion(num, even=0, odd=0):
    def even_odd_num_1(num, even=0, odd=0):
        if num > 0:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
            num = num // 10
            return even_odd_num_1(num, even, odd)
        else:
            return print(f'В вашем числе: четных {even}, нечетных {odd}')


@memory_time_profiler
def even_odd_num_2(num, even=0, odd=0):
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10


num_1 = 1472583690547893154598465132789648654321987654321987546321541356698
num_2 = 1472583699846513278964865432198765432198754632154135669805478931545
# сделал два числа разных но с одинаковым количеством чет и нечетных между
# собой
print(profiler_recursion(num_1))
print(even_odd_num_2(num_2))
"""
После ухода от рекурсии значительное улучшение но использованию памяти, но  
немного в ущерб скорости.
"""
