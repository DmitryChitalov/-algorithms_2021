from memory_profiler import memory_usage
from timeit import default_timer


def mem_time_prof(func):
    def wrapper(*args, **kwargs):
        time1 = default_timer()
        m1 = memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        time2 = default_timer()
        print(f'Время выполнения: {time2 - time1}\nИспользуемая память: {m2[0] - m1[0]} MiB')
        return res
    return wrapper


@mem_time_prof
def check_even_odd(num):
    def check_numbers(user_num, even_numbers=[], odd_numbers=[]):
        if user_num == 0:
            return f'The number of evens is {len(even_numbers)}, ' \
               f'The number of odds is {len(odd_numbers)}'
        else:
            current_num = user_num % 10
            user_num = user_num // 10
        if current_num % 2 == 0:
            even_numbers.append(current_num)
        else:
            odd_numbers.append(current_num)

        return check_numbers(user_num, even_numbers, odd_numbers)


@mem_time_prof
def even_odd_loop(num):
    even, odd = 0, 0
    while num != 0:
        last_num = num % 10
        if last_num % 2:
            odd += 1
        else:
            even += 1
        num //= 10
    return even, odd


if __name__ == '__main__':
    print(f'Рекурсия: ')
    check_even_odd(12357693458577790812357693)
    print('###########################################################')
    print(f'Цикл: ')
    even_odd_loop(12357693458577790812357693)


'''
Рекурсия: 
Время выполнения: 0.2090173
Используемая память: 0.00390625 MiB
###########################################################
Цикл: 
Время выполнения: 0.21862340000000002
Используемая память: 0.0 MiB

ВЫВОД: Использование цикла вместо рекурсии в данном случае не дало большой экономии памяти. По скорости
результаты тоже сопоставимы. 
'''
