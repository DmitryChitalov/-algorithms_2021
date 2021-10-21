
from memory_profiler import memory_usage
from timeit import default_timer

memory_used = []
wasted_time = []


def memory_and_time_to_lists(func):  # Взял наработку с разбора заданий и немножко допилил

    def wrapper(*args):
        current_used_memory = float(str(memory_usage())[1:-1])
        current_wasted_time = default_timer()
        res = func(*args)
        wasted_time.append(round(default_timer() - current_wasted_time, 3))
        memory_used.append(round(float(str(memory_usage())[1:-1]) - current_used_memory, 3))

        return res

    return wrapper


@memory_and_time_to_lists
def get_sum_by_recursion(number, sum_by_recursion=0):
    """ Рекурсивно считает сумму чисел от 1 до number, где number - натуральное число """
    return sum_by_recursion + 1 if number == 1 else get_sum_by_recursion(number - 1, sum_by_recursion + number)


user_number = int(input('Введите целое положительное число: '))

print(f'Сумма натуральных чисел до {user_number} включительно: {get_sum_by_recursion(user_number)}')
print(f'Потраченная память на вызовы рекурсивной функции: {memory_used[-1]}')
print(f'Потрачено времени на вызовы рекурсивной функции: {wasted_time[-1]}')


# Сумма натуральных чисел до 100 включительно: 5050
# Потраченная память на вызовы рекурсивной функции: 0.293
# Потрачено времени на вызовы рекурсивной функции: 20.058

memory_used.clear()
wasted_time.clear()


@memory_and_time_to_lists
def get_sum_native(number):
    return (number + 1) / 2 * number


user_number = int(input('Введите целое положительное число: '))

print(f'Сумма натуральных чисел до {user_number} включительно: {get_sum_native(user_number)}')
print(f'Потраченная память на получение результата от данной функции: {memory_used[-1]}')
print(f'Потрачено времени на получение результата от данной функции: {wasted_time[-1]}')

# Сумма натуральных чисел до 1000000 включительно: 500000500000.0
# Потраченная память на получение результата от данной функции: 0.0
# Потрачено времени на получение результата от данной функции: 0.0

# В данном примере видно неэффективность рекурсии.
# Помимо того, что данный алгоритм с использованием рекурсии имеет временную сложность O(N)
# и имеет ограничение по глубине стека вызовов, оно также затрачивает ресурсы памяти

# Второй алгоритм имеет константную временную сложность, что гораздо оптимальнее по времени,
# и не затрачивает ресурсы памяти (т.е. затраты почти равны нулю)
