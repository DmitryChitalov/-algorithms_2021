import time
from collections import deque

storage = []
coll_dq = deque()
filling = [s for s in range(30 ** 5)]

filling_2 = 30 ** 5


def my_decorator(function_to_decorate):
    def time_calculation(*args, **kwargs):
        start_time = time.time()
        result = function_to_decorate(*args, **kwargs)
        end_time = time.time()
        print(f'* Время выполнения функции {function_to_decorate.__name__} составляет: '
              f'{end_time - start_time} секунд.' + " ")
        return result

    return time_calculation


# заполнение списка простым способом
@my_decorator
def lst_func(introduction, bulkhead):
    for i in range(bulkhead):
        introduction.append(i)


# заполнение списка через коллекцию deque
@my_decorator
def dq_func(introduction, bulkhead):
    for i in range(bulkhead):
        introduction.append(i)


# добавление в список в начало через коллекцию deque
@my_decorator
def addendum_dq(introduction, bulkhead):
    for i in range(bulkhead):
        introduction.appendleft(i)


# удаление из начала списка через коллекцию deque
@my_decorator
def removal_dq(introduction):
    for _ in range(10000):
        introduction.popleft()


# добавление списка в конец другого списка через коллекцию deque
@my_decorator
def dob_box_dq(introduction, bulkhead):
    for _ in range(10):
        introduction.extendleft(bulkhead)


# добавление в список простым способом
@my_decorator
def addendum_lst(introduction, bulkhead):
    for i in range(bulkhead):
        introduction.append(i)


# удаление из списка простым способом
@my_decorator
def removal_lst(introduction):
    for _ in range(10000):
        introduction.pop()


# добавление списка в конец другого списка простым способом
@my_decorator
def dob_box_lst(introduction, bulkhead):
    for _ in range(10):
        introduction.insert(0, bulkhead)


lst_func(storage, filling_2)
dq_func(coll_dq, filling_2)
print('_' * 100)
addendum_dq(coll_dq, filling_2)
addendum_lst(storage, filling_2)
print('_' * 100)
# removal_dq(coll_dq)
# removal_lst(storage)
print('_' * 100)
dob_box_dq(coll_dq, filling)
dob_box_lst(storage, filling)

# * Время выполнения функции lst_func составляет: 2.007831335067749 секунд.
# * Время выполнения функции dq_func составляет: 1.7310295104980469 секунд.
"""
        При выполнении просто заполнения list и deque, выполнение deque происходит быстрее 
    поскольку deque обеспечивает сложность времени O (1) для операций добавления
     по сравнению со списком, который обеспечивает сложность времени O (n).
"""

# ____________________________________________________________________________________
# * Время выполнения функции addendum_dq составляет: 4.000900983810425 секунд.
# * Время выполнения функции addendum_lst составляет: 4.121171712875366 секунд.

"""
        Тут добовляем в уже созданнный список list и deque, и deque снова будет быстрее т.к. мы уже говорили,
    что временная сложность при добавлении является O(1). 
"""

# ____________________________________________________________________________________
# * Время выполнения функции removal_dq составляет: 0.06596231460571289 секунд.
# * Время выполнения функции removal_lst составляет: 0.0069959163665771484 секунд.

"""
        При удалении из списка list и deque, выполнение удаления происходит быстрее у списка list,т.к.
    временная сложность при выполнении удаления является O(1), а удаление у список deque равен O(n) времнной сложности.
"""
# ____________________________________________________________________________________
# * Время выполнения функции dob_box_dq составляет: 3.0382444858551025 секунд.
# * Время выполнения функции dob_box_lst составляет: 0.27784156799316406 секунд.
"""
    При добавлении нескольких элементов в список list снова будет быстрее т.к. при добавлении у списка list 
    временная сложность O(1), а у списка deque при добавлении методом extendleft временная сложность равна O(n) в
    отличии от добавления appendleft. 
"""
