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
import time

def time_check(func):
    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time()
        return end - start
    return wrapper

@time_check
def list_filling(input_list):
    list1 = []
    for i in input_list:
        list1.append(i)
    return list1

@time_check
def dict_filling(input_dict):
    dict1 = {}
    for key, value in input_dict.items():
        dict1[key] = value
    return dict1

@time_check
def list_search(input_list):
    input_list.index(7074)

@time_check
def dict_search(input_dict):
    input_dict.get(7074, 0)

@time_check
def list_clear(input_list):
    return input_list.clear()

@time_check
def dict_clear(input_dict):
    return input_dict.clear()

test_dict = dict((int(n), int(n)) for n in range(9000000))
test_list = list((int(n)) for n in range(9000000))

print(list_filling(test_list))  # 0.549741268157959
print(dict_filling(test_dict))  # 0.660146951675415 Словарь заполняеется дольше
print(list_search(test_list))  # 0.004565238952636719
print(dict_search(test_dict))  # 0.0 Поиск по словарю отрабатывает моментально из-за использования хеша
print(list_clear(test_list))  # 0.08336877822875977
print(dict_clear(test_dict))  # 0.09193658828735352 Очищание словаря происходит чуть медленнее