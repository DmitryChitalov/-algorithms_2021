from time import time
from random import randint


def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        ent_time = time()
        print(f'Время работы функции {func.__name__} составило {ent_time - start_time}')
        return result

    return wrapper


@time_logger
def test_fill_dict(dict_for_fill):
    for i in range(100000):
        dict_for_fill[i] = randint(0, 100000)  # сложность d[k] = v константная O(1)


@time_logger
def test_fill_list(list_for_fill):
    for _ in range(100000):
        list_for_fill.append(randint(0, 100000))  # сложность .append константная O(1)


@time_logger
def test_dict_read(dict_to_test):
    for i in range(len(dict_to_test)):
        _ = dict_to_test.get(i)  # O(1)


@time_logger
def test_dict_update(dict_to_test):
    for i in range(len(dict_to_test)):
        dict_to_test[i] = 'test'  # O(1)


@time_logger
def test_dict_remove(dict_to_test):
    for i in range(20000, 30000):
        dict_to_test.pop(i)  # O(1)


@time_logger
def test_list_read(list_to_test):
    for i in range(len(list_to_test)):
        _ = list_to_test[i]  # O(1)


@time_logger
def test_list_update(list_to_test):
    for i in range(len(list_to_test)):
        list_to_test[i] = 'test'  # O(1)


@time_logger
def test_list_remove(list_to_test):
    for i in range(20000, 30000):
        list_to_test.pop(i)  # O(n)


if __name__ == '__main__':
    numbers_dict = {}
    numbers_list = []
    test_fill_dict(numbers_dict)
    test_fill_list(numbers_list)
    test_dict_read(numbers_dict)
    test_list_read(numbers_list)
    test_dict_update(numbers_dict)
    test_list_update(numbers_list)
    test_dict_remove(numbers_dict)
    test_list_remove(numbers_list)

    """
    a) 
    Время работы заполнения со списком меньше, засчет вычисления хешей в словаре.
    
    b)
    Операции обновления, чтения, удаления элемента в словаре проиходят быстрее чем в списке
    """
