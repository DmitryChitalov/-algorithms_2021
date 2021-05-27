from time import time

new_list = []
new_dict = {}
second_dict = {1: "один",
               2: "два"}
third_dict = {7: "семь",
              8: "восемь",
              4: "четыре"}
n = 100000



def time_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} '
              f'составило {end - start}')
        return result

    return timer



#Заполнение списков. 2 вида: добавление в конец и в определенное место
@time_decorator
def append1(lst, num):
    for i in range(num):
        lst.append(i)
append1(new_list, n)


@time_decorator
def insert2(lst, num):
    for i in range(num):
        lst.insert(0, i)
insert2(new_list, n)



#Заполнение словаря. 2 вида: добавление в словарь и обычное заполнение элементами
@time_decorator
def update1(dict, val):
    dict.update(val)
update1(third_dict, second_dict)

@time_decorator
def f(dict, num):
    for i in range(num):
        dict[i] = i
f(new_dict, n)

""" Вот такой итог получился:
Время выполенения функции append1 составило 0.021592140197753906 быстрее, так как элемент просто добавляется в конец списка. Сложность О(1)
Время выполенения функции insert2 составило 8.09197473526001 дольше, так как элемент добавляется в определенное место. Сложность О(n)
Время выполенения функции update1 составило 0.0 Маленький объем данных, просто попробовала)
Время выполенения функции fill_dict составило 0.009256839752197266 Сложность так же О(1),  поэтому так быстро
"""



print()
@time_decorator
def remove1(lst):
    num = int(input("Введите количество элементов, которые хотите удалить: "))
    for i in range(num):
        lst.remove(i)
remove1(new_list)

@time_decorator
def pop2(lst):
    num = int(input("Введите количество элементов, которые хотите удалить: "))
    for i in range(num):
        lst.pop(i)
pop2(new_list)


@time_decorator
def pop1(dict):
    num = int(input("Введите количество значений, которые хотите удалить: "))
    for i in range(num):
        dict.pop(i)
pop1(new_list)

"""
Я удаляла везде по 1000 элементов
Время выполенения функции remove1 составило 6.391886234283447 Медленнее, сложность О(n)
Время выполенения функции pop2 составило 2.825349807739258 Тоже быстро обрабатывается, так как сложность О(1)
Время выполенения функции pop1 составило 2.812386989593506 Обрабатывается быстрее, так как сложность О(1)
"""

