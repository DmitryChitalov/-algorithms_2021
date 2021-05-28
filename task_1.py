import time


def my_func(n, new_list):
    start_val = time.time()
    for i in range(n): # o(n)
        new_list.append(i)  # o(1)
    end_val = time.time()
    return end_val-start_val, new_list # = 8.446875810623169


def my_func_1(n, new_dict):
    start_val = time.time()
    for i in range(n): #o(n)
        new_dict[i] = i # o(1)
        i = i-1
    end_val = time.time()
    return end_val-start_val, new_dict # = 28.923725843429565


def my_func_del(new_list):
    start_val = time.time()
    for i in range(1000):  # o(n)
        new_list.pop(i)  # o(1)
    end_val = time.time()
    return end_val - start_val


def my_func_1_del(new_dict):
    start_val = time.time()
    for i in range(1000):  # o(n)
        new_dict.pop(i)  # o(1)
    end_val = time.time()
    return end_val - start_val


my_list = []
my_dict = {}
print(my_func(100000, my_list))
print(my_func_1(100000, my_dict))
# можно увидеть что функции одинаковые по сложности, обе имеют линейную сложность
# по времени функция со словарем работает медленнее


print(my_func_del(my_list))
print(my_func_1_del(my_dict))
#здесь же наоборот функция со словарем работает быстрее