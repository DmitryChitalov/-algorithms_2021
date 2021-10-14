import time

# a) заполнение списка и словаря

my_list = []

def filling_in_the_my_list(): # Сложность O(1)
    for i in range(10):
        my_list.append(i)

start_time = time.perf_counter()
filling_in_the_my_list()
print(time.perf_counter() - start_time, "seconds")


my_dict = {}

def filling_out_the_dictionary(): # сложность О(1)
    for i in range(100):
        my_dict[i] = i

start_time = time.perf_counter()
filling_out_the_dictionary()
print(time.perf_counter() - start_time, "seconds")

"""
Вывод:
Время выполнения filling_in_the_my_list() составило - 1.940000000000275e-05 seconds
Время выполнения filling_out_the_dictionary составило - 1.3299999999993872e-05 seconds
Из чего следует, что заполнение словаря занимает меньше времени, так как 
он представляет из себя хеш-таблицу и его сложность О(1).
"""

# b) выполните набор операций и со списком, и со словарем

def filling_in_the_my_lst(): # Сложность O(N)
    for i in range(5):
        my_list.pop(i)
    for k in range(5):
        my_list.copy()

start_time = time.perf_counter()
filling_in_the_my_lst()
print(time.perf_counter() - start_time, "seconds")


def filling_out_the_dict(): # Сложность O(1)
    for i in range(15):
        my_dict[i]
    for k in range(20):
        my_dict.pop(k)


start_time = time.perf_counter()
filling_out_the_dict()
print(time.perf_counter() - start_time, "seconds")

"""
Вывод
ремя выполнения filling_in_the_my_lые() составило - 1.6299999999996873e-05 seconds
Время выполнения filling_out_the_dict составило - 1.5299999999995872e-05 seconds
Операция pop() из списка выполняется со сложностью О(N), как и операция copy() - O(N).
Операции для словарей почти все имеют сложность O(1), поэтому выполняются намного быстрее.
"""

