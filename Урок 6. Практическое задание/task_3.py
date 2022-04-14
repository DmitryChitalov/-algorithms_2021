"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile

@profile
def profiler_recursion(num, even=0, odd=0):
    def even_odd_num_1(num, even=0, odd=0):
        if num > 0:
            if num % 2 == 0:
                even +=1
            else:
                odd +=1
            num = num // 10
            return even_odd_num_1(num, even, odd)
        else:
            return print(f'В вашем числе: четных {even}, нечетных {odd}')


@profile
def even_odd_num_2(num, even=0, odd=0):
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd +=1
        num = num // 10


numb_1 = 1472583690547893154598465132789648654321987654321987546321541356698
numb_2 = 1472583699846513278964865432198765432198754632154135669805478931545

print(even_odd_num_2(numb_2))
print(profiler_recursion(numb_1))
