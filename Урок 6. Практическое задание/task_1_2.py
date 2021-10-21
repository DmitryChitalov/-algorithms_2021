from timeit import default_timer
import memory_profiler

def mem_tm(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        t1 = default_timer()
        res = func(*args, **kwargs)
        time_diff = default_timer() - t1
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return f'Заняло памяти: {mem_diff} MiB\n Заняло времени: {time_diff}'
    return wrapper


@mem_tm
def lesson_1():
    start_list = []
    total_1 = 0
    total_2 = 0
    for i in range(1, 100000, 2):
        number = i ** 3
        start_list.append(number)
    for i in start_list:
        count = 0
        for number in str(i):
            count += int(number)
        if not count % 7:
            total_1 += i
    for i in start_list:
        i += 17
        count = 0
        for number in str(i):
            count += int(number)
        if not count % 7:
            total_2 += i
    return total_1, total_2


@mem_tm
def lesson_1_fix():
    start_list = [i**3 for i in range(1, 100000, 2)]
    total_1 = 0
    total_2 = 0
    for i in start_list:
        count_1 = 0
        count_2 = 0
        for number in str(i):
            count_1 += int(number)
        if not count_1 % 7:
            total_1 += i
        for number in str(i+17):
            count_2 += int(number)
        if not count_2 % 7:
            total_2 += i
    del start_list
    return total_1, total_2


print(f'Циклы с первого урока основ Python:\n {lesson_1()}')          # 0.2421875 MiB, 0.2659444000000001
print(f'Оптимизация первого урока основ Python:\n {lesson_1_fix()}')  # 0.0 MiB, 0.2265212000000001

"""
Оптимизировано создание списка через ls. в конце функции удалил созданный список, т.к далее он уже не используется.
Тем самым высвободили память.
"""