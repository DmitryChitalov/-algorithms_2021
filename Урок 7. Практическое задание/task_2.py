"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from timeit import timeit
from memory_profiler import profile
from random import uniform


# вариант реализации (похожий на код с урока), взятый с сайта
# https://tproger.ru/translations/sorting-algorithms-in-python/
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


# код с урока
def merge_sort_from_lesson(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


@profile
def mrg_sort_mem_profile(list_to_sort):
    merge_sort(list_to_sort)


@profile
def mrg_sort_from_lesson_mem_profile(list_to_sort):
    merge_sort_from_lesson(list_to_sort)


numbers_list = [uniform(0, 49) for _ in range(10)]
print(f'исходный массив: {numbers_list}')
print(f'отсортированный массив: {merge_sort(numbers_list[:])}')

# время - 0.017 с, память - 20 MiB
print('новая реализация:')
print(f"время выполения: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_mem_profile(numbers_list[:])

# время - 0.017 с, память - 20 MiB
print('реализация с урока:')
print(f"время выполения: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_from_lesson_mem_profile(numbers_list[:])

numbers_list = [uniform(0, 49) for _ in range(100)]

# время - 0.24 с, память - 20 MiB
print('новая реализация:')
print(f"время выполения: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_mem_profile(numbers_list[:])

# время - 0.023 с, память - 20 MiB
print('реализация с урока:')
print(f"время выполения: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_from_lesson_mem_profile(numbers_list[:])

numbers_list = [uniform(0, 49) for _ in range(1000)]

# время - 3.18 с, память - 20.3 MiB
print('новая реализация:')
print(f"время выполения: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_mem_profile(numbers_list[:])

# время - 3.28 с, память - 20 MiB
print('реализация с урока:')
print(f"время выполения: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_from_lesson_mem_profile(numbers_list[:])

numbers_list = [uniform(0, 49) for _ in range(10000)]

# время - 40.29 с, память - 21.9 MiB
print('новая реализация:')
print(f"время выполения: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_mem_profile(numbers_list[:])

# время - 40.23 с, память - 21.7 MiB
print('реализация с урока:')
print(f"время выполения: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_from_lesson_mem_profile(numbers_list[:])

numbers_list = [uniform(0, 49) for _ in range(100000)]

# время - 486.45 с, память - 25.4 MiB
print('новая реализация:')
print(f"время выполения: {timeit('merge_sort(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_mem_profile(numbers_list[:])

# время - 494.23 с, память - 25.9 MiB
print('реализация с урока:')
print(f"время выполения: {timeit('merge_sort_from_lesson(numbers_list[:])', number=1000, globals=globals())}")
print('занимаемая память:\n')
mrg_sort_from_lesson_mem_profile(numbers_list[:])

'''
результаты временных замеров показали, что сложность алгоритма действительно O(NlogN), поскольку с ростом длины 
входного массива время выполенения алгоритма сортировки (в сравнении с длиной входных данных) увеличивается 
незначительно. при этом замеры памяти показали, что с ростом длины входных данных требуемый объем памяти 
увеличивается существенно: 20.3 МиБ = 2660761.6 байт для входных данных длины 1000 и 25.4 = 3329228.8 байт для 
входных данных длины 100000 причиной такого увеличения требуемого объема памяти является увеличение длины входного 
массива чисел, также на потребляемый объем памяти влияет рекурсивная реализация алгоритма сортировки
также результаты замеров времени выполнения и памяти показали, что реализация алгоритма из интернета несущественно
уступает реализации алгоритма, приведенной на уроке. разница в показателях замеров соответствует погрешности
'''
