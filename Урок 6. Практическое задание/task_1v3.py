from memory_profiler import memory_usage
from timeit import default_timer


def memory_time(func):
    def wrapper(*args):
        t_1 = default_timer()
        mem_1 = memory_usage()[0]
        result = func(*args)
        print(f'Время: {default_timer() - t_1}\nПамять: {memory_usage()[0] - mem_1}')
        return result

    return wrapper


@memory_time
def seasons_what(n):
    seasons = ["зима", "весна", "лето", "осень"]
    try:
        if n <= 0 or n > 12:
            raise OverflowError
    except ValueError:
        return f'Ошибка! необходимо ввести число месяца!'
    except OverflowError:
        return f'Ошибка! Такого месяца не существует! Введите число от 1 до 12'
    return f'Месяц относится к времени года: {seasons[0 if n == 12 else n // 3]}'
@memory_time
def seasons_what_prof(n):
    seasons = ("зима", "весна", "лето", "осень")
    try:
        if n <= 0 or n > 12:
            raise OverflowError
    except ValueError:
        return f'Ошибка! необходимо ввести число месяца!'
    except OverflowError:
        return f'Ошибка! Такого месяца не существует! Введите число от 1 до 12'
    return f'Месяц относится к времени года: {seasons[0 if n == 12 else n // 3]}'

print(seasons_what(11))
print(seasons_what_prof(11))

'''
Оригинальная функция
Время: 0.10412229999999997
Память: 0.015625

Измененная
Время: 0.11048429999999998
Память: 0.0

Единственное изменение - это то, что список был заменен на кортеж. Кортежи занимают меньше памяти.
'''