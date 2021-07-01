"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать,
   так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
from time import time


def diff_time(s_func):
    def diff_time_wrap(*args):
        start = time()
        result = s_func(*args)
        print(f'Spent time {time()-start}')
        return result
    return diff_time_wrap


@diff_time
def adding_data_list():
    """
    Заполнение списка происзодит быстрее, так как заполняются только значения.
    затраченное время, примерно в 2 раза меньше, чем для заполнения словаря.
    """
    test_list = [el for el in range(1000)]
    return test_list


@diff_time
def adding_data_dict():
    """
    Заполнение словаря дольшее, так как происходит генерация пары "Ключ: Значение".
    """
    test_dict = {x: x+1 for x in range(1000)}
    return test_dict


@diff_time
def find_with_del_list(s_list, element):
    """
    Удаление функцией pop() затратило одинаковое количество времени, что для списка, что для словаря.
    """
    try:
        s_list.pop(element)
        return f'Element {element} was found and deleted'
    except IndexError:
        return f'Element is not in list'


@diff_time
def find_with_del_dict(s_dict, key):
    """
    Поиск значения в словаре по ключу происходит быстрее, чем в списке. Предположение, что список работает с индексами,
    а поиск по индексу работает медленнее.
    """
    try:
        s_dict.pop(key)
        return f'Element {s_dict.get(key)} was found and deleted'
    except KeyError:
        return f'Key {key} does not exists'


t_list = adding_data_list()
t_dict = adding_data_dict()

print(find_with_del_list(t_list, 500))
print(find_with_del_list(t_list, 5000))
print(find_with_del_dict(t_dict, 400))
print(find_with_del_dict(t_dict, 3333))
