import time

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
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""


def profile(f):
    def g(x):
        start_time = time.time()
        value = f(x)
        end_time = time.time()
        print(end_time-start_time)
        return value
    return g


@profile
def create_list_1(n):
    """
    Маленькое время создания, так как новые элементы вставляются в конец списка
    O(1)
    :param n:
    :return:
    """
    return [i for i in range(n)]


@profile
def create_list_2(n):
    """
    Эллементы вставляются в начало списка сдвигая уже существующие, в связи с этим врем создания увеличивается
    O(n)
    :param n:
    :return:
    """
    lst = []
    for i in range(n):
        lst.insert(0, i)
    return lst


@profile
def create_dict_1(n):
    """
    Словарь создается быстро
    O(1)
    :param n:
    :return:
    """
    return {i: i for i in range(n)}


@profile
def create_dict_2(n):
    d = {}
    for i in range(n):
        d[i] = i
    return d


@profile
def change_list(n):
    """
    O(n)
    Чтение списка заметно выше, по сравнению со словарем, так как в списке скрипту приходится последовательно
    перебирать занчения
    :param n:
    :return:
    """
    for i in range(1000):
        n.pop(i)
    for j in range(100):
        n[j] = n[j + 1]


@profile
def change_dict(n):
    """
    O(1)
    :param n:
    :return:
    """
    for i in range(1000):
        n.pop(i)
    for j in range(101, 202):
        n[j] = 'fill'


val = 10000
print('-'*30)
print('Создание списков')
crt_lst = create_list_1(val)
create_list_2(val)
print('-'*30)
print('Создание словарей')
crt_dct = create_dict_1(val)
create_dict_2(val)
print('-'*30)
print('Чтение списка')
change_list(crt_lst)
print('-'*30)
print('Чтение словаря')
change_dict(crt_dct)
print('-'*30)
