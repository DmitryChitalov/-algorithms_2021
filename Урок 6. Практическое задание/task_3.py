"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from timeit import default_timer

import memory_profiler


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = func()
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - start_time
        return res, mem_diff, time_diff
    return wrapper


# Вот функция с рекурсией. К ней применен декоратор.

@decorator
def get_number():
    result_dict = {'num_1': 0, 'num_2': 0}
    num_list = list("5368966623569")

    def check_number():
        if (len(num_list)) != 0:
            num = int(num_list.pop())
            if num % 2 != 0:
                result_dict['num_2'] += 1
                check_number()
            else:
                result_dict['num_1'] += 1
                check_number()
    check_number()
    return f'Четных: {result_dict["num_1"]}; нечетных: {result_dict["num_2"]}'


if __name__ == '__main__':

    res, mem_diff, time_diff = get_number()
    print(f"Выполнение get_number() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")
    print('-' * 30)


"""
Решение как обсуждали на уроке - когда рекурсивная функция втраивается в другую.
"""