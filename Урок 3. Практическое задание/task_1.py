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

my_list = []
my_dict = {}

def time_decorator(function):
    def my_func(n):
        my_time = time.time()
        function(n)
        return time.time() - my_time
    return my_func

# Сложность константная O(1)
@time_decorator
def time_list(n):
    for ls in range(n):
        my_list.append(ls)

# Сложность константная O(1)
@time_decorator
def time_list_1(n):
    my_list = [ls for ls in range(n)]

# Сложность константная O(1)
@time_decorator
def time_dict(n):
    for dc in range(n):
        my_dict[dc] = dc

# Сложность константная O(1)
@time_decorator
def time_dict_1(n):
    my_dict = {dc: dc for dc in range(n)}

# Сложность линейная O(n) - перебор элементов
@time_decorator
def operation_list_del(n):
    for i in range(n):
        my_list.pop(0)


@time_decorator
def operation_list_change(n):
    for ls in range(n):
        my_list[ls] = ls * 2

# Сложность линейная O(n) - перебор элементов
@time_decorator
def operation_dict_del(n):
   for key in range(n):
        my_dict.pop(key)

@time_decorator
def operation_dict_change(n):
    for key, value in my_dict.items():
        my_dict[key] = value*2

k = 100000
print(f'time_list(for ... append)          = {time_list(k)}')
print(f'time_dict(for ... my_dict[dc]=dc)  = {time_dict(k)}')
print()
print(f'time_list(list comprehensions)     = {time_list_1(k)}')
print(f'time_dict(dict comprehensions)     = {time_dict_1(k)}')
print()
print(f'time_operation_list_change         = {operation_list_change(k)}')
print(f'time_operation_dict_change         = {operation_dict_change(k)}')
print()
print(f'time_operation_list_del            = {operation_list_del(k)}')
print(f'time_operation_dict_del            = {operation_dict_del(k)}')


'''
    а) Я считаю, что сложность в предоставленных функциях одинаковая - константная O(1), так как
цикл мы задаем фиксировано range(n), где n например 10000000.
    Результаты замеров показывают, что для заполнения списка лучше использовать list comprehensions.
Код более лаконичный и замер времени min. Для словаря лучше использовать наполнение путем цикла
for и присваивания нового элемента my_dict[dc] = dc
    Также исходя из замеров видно что заполнение списков более быстрый процесс,  чем словарей. Я думаю, 
что это связано с структурой хранение данных в словарях, а именно для хранения одного элемента словаря,
необходимо обрабатывать ключ: значение, а в списках только значение...
    б) Сложность функций операции изменения над словарями и списками линейная O(n), потому что идет перебор
элементов, а согласно таблице "for i in d для типа items" - для словаря и "for v in l" - для списка является
линейной сложностью . Поэтому время выполлнения по замерам практически одинаковое...
       Сложность функций операции удаления над словарями - O(1), над списками - линейная O(n), поэтому 
операция удаления элементов словарей выполняется бысстрее чем элемнтов списка...
       
 

'''

