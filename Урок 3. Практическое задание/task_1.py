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

from time import time

test_list = [1, 2, 4, 10]
test_dict = {1: 'one', 2: 'two', 4: 'four', 10: 'ten'}


def time_measure(func_to_decorate):
    def the_wrapper(n):
        for i in range(100000000):  # it's CPU power up
            1 / 100
        start_time = time()
        execute = func_to_decorate(n)
        print(f'The execution time is {time() - start_time}')
        return execute
    return the_wrapper


@time_measure
def list_filler_comprehension(k):       # Сложность функции O(N) - линейная
    lst = [i for i in range(k)]         # O(N) - линейная
    return 'Created list by comprehension'

@time_measure
def list_filler_append(k):              # Сложность функции O(N) - линейная
    lst = []                            # O(1) - константная
    for i in range(k):                  # O(N) - линейная
        lst.append(i)                   # O(1) - константная
    return 'Created list by append'

@time_measure
def dict_filler_comprehension(k):       # Сложность функции O(N) - линейная
    dict = {i: i for i in range(k)}     # O(N) - линейная
    return 'Created Dictionary by comprehension'

@time_measure
def dict_filler_setdefault(k):          # Сложность функции O(N) - линейная
    dict = {}                           # O(1) - константная
    for i in range(k):                  # O(N) - линейная
        dict.setdefault(i, 1000)        # O(1) - константная
    return 'Created Dictionary by setdefault'

@time_measure
def dict_filler_update(k):              # Сложность функции O(N) - линейная
    dict = {}                           # O(1) - константная
    for i in range(k):                  # O(N) - линейная
        dict.update({i: i})             # O(1) - константная
    return 'Created Dictionary by update'

@time_measure
def list_oper(k):                       # Сложность функции O(N) - линейная
    num = 10                            # O(1) - константная
    if num in k:                        # O(N) - линейная
        None                            # O(1) - константная
    k.pop(len(k)-1)                     # O(1) - константная
    return 'list operations'

@time_measure
def dict_oper(k):                       # Сложность функции O(N) - линейная
    num = 10                            # O(1) - константная
    if num in k.keys():                 # O(N) - линейная
        None                            # O(1) - константная
    k.pop(num)                          # O(1) - константная
    return 'Dictionary operations'

print(list_filler_comprehension(1000000))
print(list_filler_append(1000000))
print(dict_filler_comprehension(1000000))
print(dict_filler_setdefault(1000000))
print(dict_filler_update(1000000))
print(list_oper([1, 2, 4, 10]))
print(dict_oper({1: 'one', 2: 'two', 4: 'four', 10: 'ten'}))

"""
Вывод: словарь работает медленнее при аналогичных функциях наполнения.
Причина: использование бОльшего объема памяти для словаря чем для списка.
Однако выполнение операций занимает примерно равное время, что говорит о том что
для операций нет разницы в использовании типа данных словарь или список.
"""