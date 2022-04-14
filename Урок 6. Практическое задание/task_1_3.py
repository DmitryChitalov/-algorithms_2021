from task_1 import memory_time_profiler


@memory_time_profiler
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


@memory_time_profiler
def odd_even_num_2(num, even=0, odd=0):
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num//10


my_num = 1460987345073497675845779864623742513564563454568729365863567567235437896564567687543
profile_recursion(my_num)
print("--------------------------------------")
odd_even_num_2(my_num)

"""
Функция из дз: подсчет четных и нечетных цифр числа. Рекурсия как и ожидалось более затратная как по времени так и по 
используемой памяти, так как ей необходимо создавать таблицу для каждого шага. 
Использовано памяти: 0.00390625 , выполнено за: 9.80000000000425e-06
--------------------------------------
Использовано памяти: 0.0 , выполнено за: 4.7699999999983866e-05
"""