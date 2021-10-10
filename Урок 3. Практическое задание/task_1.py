"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
   Операцию clear() не используем.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
from time import time

mass_dict = {}
mass_list = []

n = 100000

def calc_time(foo):
    def clock(*args, **kwargs):
        start_val = time()
        result = foo(*args, **kwargs)
        end_val = time()
        print(f'Время выполнения функции {foo.__name__} = {end_val - start_val}')
        return result

    return clock


@calc_time
def create_list_app(list_var, var):

    for i in range(var):
        list_var.append(i)  # Сложность O(1)


create_list_app(mass_list, n)


@calc_time
def create_list_ins(list_var, var):

    for i in range(var):
        list_var.insert(0, i)  # Сложность O(n)

@calc_time
def create_dict(var_dict, var):
#  Заполнение словаря выполняется быстрее, т.к. это хеш-таблица, операция добавления элемента имеет сложность О(1)
    for i in range(var):
        var_dict[i] = i


create_dict(mass_dict, n)

# Операция удаления
@calc_time
def change_list(list_var):    # Изменение списка

    for i in range(10000):
        list_var.pop(i) # удаление 10000 эл-тов из списка
    for j in  range(1000):
        list_var[j] = list_var[j + 1]  # измение 1000 эл-тов списка

change_list(mass_list)


@calc_time
def change_dict(var_dict):

    for i in range(10000):  #  Изменеие словаря
        var_dict.pop(i)  # удаление записей из словаря - 10000
    for j in range(5000, 6001):
        var_dict[j] = 'some_data'  # измение значений словаря. Сложность операций: О(1)

change_dict(mass_dict)



