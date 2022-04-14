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

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time


def dict_insert(insert_dict):
    insert_dict['test_1'], insert_dict['test_2'], insert_dict['test_3'] = \
        'test_data_1', 'test_data_2', 'test_data_3'


def list_insert(insert_list):
    insert_list.append('test_1')
    insert_list.append('test_2')
    insert_list.append('test_3')


test_dict = {}
test_list = []

start_time = time.perf_counter_ns()
dict_insert(test_dict)  # 0(1)
print('заполнение словаря', time.perf_counter_ns() - start_time, 'ns')

start_time = time.perf_counter_ns()
test_dict.pop('test_1')  # 0(1)
print('Удаление элемента словаря', time.perf_counter_ns() - start_time, 'ns')

start_time = time.perf_counter_ns()
for el in test_dict:  # O(n)
    pass
print('Перебор словаря в цикле', time.perf_counter_ns() - start_time, 'ns')
print()

start_time = time.perf_counter_ns()
list_insert(test_list)  # 0(1)
print('заполнение списка', time.perf_counter_ns() - start_time, 'ns')

start_time = time.perf_counter_ns()
test_list.remove('test_1')  # O(n)
print('Удаление элемента списка', time.perf_counter_ns() - start_time, 'ns')

start_time = time.perf_counter_ns()
for el in test_list:  # O(n)
    pass
print('Перебор списка в цикле', time.perf_counter_ns() - start_time, 'ns')
