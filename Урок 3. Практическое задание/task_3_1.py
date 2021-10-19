from time import time


def full_time():
    """
        a) заполнение списка и словаря,
        сделайте замеры и сделайте выводы, что выполняется быстрее и почему
        И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
        У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и
        отличаться.
         b) выполните набор операций и со списком, и со словарем,
        сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
        И укажите сложность ф-ций, которые вы используете для операций.
        Операцию clear() не используем.
    """


# a)


main_list = []
main_dict = {}


def timers_list():
    start = time()
    append_list()
    end = time()
    print(f"Время выполнения составило по листу  {end - start}")
    result = end - start
    return result


def timers_dict():
    start = time()
    append_dict()
    end = time()
    print(f"Время выполнения составило по словарю {end - start}")
    result = end - start
    return result


def append_list():
    for numb in range(1, 10000):
        main_list.append(numb)  # O(1)
        # Заполняем список данными.


def append_dict():
    for numb in range(1, 10000):
        main_dict[numb] = numb  # О(1).
        # Заполняем словарь

print('Пункт a)')
timers_list()
timers_dict()

"""
Пункт a)
Время выполнения составило по листу  0.00099945068359375
Время выполнения составило по словарю 0.0009987354278564453 
"""
# Выводы:  операция с заполнением листа по времени выходит меньше чем операция со словарем.

# b)

def timers_list_b():
    start = time()
    change_list()
    end = time()
    print(f"Время выполнения составило по листу  {end - start}")
    result = end - start
    return result


def timers_dict_b():
    start = time()
    change_dict()
    end = time()
    print(f"Время выполнения составило по словарю {end - start}")
    result = end - start
    return result


def change_list():
    for nums in range(1, 10000):
        main_list.remove(nums)
        # удаляем все улементы

    for numb1 in range(1, 10000):
        main_list.append(numb1)    # О(1)
        # добавляем элементы.
    return main_list


def change_dict():
    for nums in range(1, 10000):
        main_dict.pop(nums)
        # удаляем все улементы

    for numb2 in range(1, 10000):
        main_dict[numb2] = numb2    # О(1)
        # добавляем элементы.
    return main_list

print('\nПункт b)')
timers_list_b()
timers_dict_b()


# Вывод: В этот раз удаление и добавление элементов лучше всего показал словарь.

"""
Пункт b)
Время выполнения составило по листу  0.015990257263183594
Время выполнения составило по словарю 0.0019986629486083984

У словаря есть кеш таблицы, и на это требуется тоже время, по этому лист быстрее будет отрабатывать по времени !

"""