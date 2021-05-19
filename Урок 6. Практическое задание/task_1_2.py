from task_1 import memory_time_profiler


@memory_time_profiler
def app_list(lst):
    new_lst = []
    for item in lst:
        new_lst.append(int(item))
    return new_lst


@memory_time_profiler
def map_list(lst):
    new_lst = list(map(int, lst))
    return new_lst


my_list = (i for i in range(100000000))
app_list(my_list)
print("------------------------------------------")
map_list(my_list)

"""
Как видно из теста для преобразования строки в число встроенная функция map тратит на несколько порядков меньше памяти и 
времени чем цикл for. 
Использовано памяти: 3859.61328125 , выполнено за: 20.926012800000002
------------------------------------------
Использовано памяти: 0.0078125 , выполнено за: 0.005759199999999964
"""