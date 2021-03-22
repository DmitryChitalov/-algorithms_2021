"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

from timeit import default_timer, timeit


# собственный декоратор для проверки замеров времени с помощью timeit
def exec_time_decorator(count):
    def exec_time(func):
        def wrapper(*args):
            result = 0

            for number in range(count):
                start = default_timer()  # левая отсечка времени
                func(args[0])
                tmp_res = default_timer() - start  # правая отсечка времени
                result += tmp_res  # формирование итогового значения

            print(f'время выполнения: {result}')

        return wrapper

    return exec_time


# исходная функция, уже присутствующая в задании
def func_1_for_timeit(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# для генерации нового списка использовал LC, поскольку это лаконичнее и выполняется быстрее, нежели вариант с циклом for.
# К тому же для генерации нового списка производится меньшее количество операций (не создаем новый промежуточный список
# new_arr и не используем append() для его заполнения)  => выигрыш в скорости выполнения и в объеме занимаемой памяти
def get_index_in_list_for_timeit(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


# исходная функция, уже присутствующая в задании, только с применением декоратора
@exec_time_decorator(10000)
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# собственный вариант оптимизации, только с применением декоратора
@exec_time_decorator(10000)
def get_index_in_list(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


numbers_list = [i for i in range(100)]
print(timeit("func_1_for_timeit(numbers_list)", number=10000, globals=globals()))  # результат: 0.085 с
print(timeit('get_index_in_list_for_timeit(numbers_list)', number=10000, globals=globals()))  # результат: 0.07 с

func_1(numbers_list)  # результат: 0.082 с
get_index_in_list(numbers_list)  # результат: 0.068 с => получили близкие значения временных замеров
