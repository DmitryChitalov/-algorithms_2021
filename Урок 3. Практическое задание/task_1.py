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
    Время работы функции test_fill_dict составило 0.20324254035949707
    Время работы функции test_fill_list составило 0.19592976570129395
    Время работы со списком чуть-чуть меньше, засчет вычисления хешей в словаре.
    
    b)
    Время работы функции fill_dict составило 0.20324254035949707
    Время работы функции fill_list составило 0.19592976570129395
    Время работы функции test_dict_read составило 0.017052173614501953
    Время работы функции test_list_read составило 0.012124776840209961
    Время работы функции test_dict_update составило 0.011615276336669922
    Время работы функции test_list_update составило 0.006996631622314453
    Время работы функции test_dict_remove составило 0.0014197826385498047
    Время работы функции test_list_remove составило 0.15018868446350098
    Операция удаления из середины списка занимает намного больше времени, чем операция удаления из середины словаря
    Остальные операции работают примерно одинаково
    """
