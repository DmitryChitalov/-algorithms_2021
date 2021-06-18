from memory_profiler import memory_usage
from timeit import default_timer
from random import randint
import json


def memory_time(func):
    def wrapper(*args):
        t_1 = default_timer()
        mem_1 = memory_usage()[0]
        result = func(*args)
        print(f'Время: {default_timer() - t_1}\nПамять: {memory_usage()[0] - mem_1}')
        return result

    return wrapper


@memory_time
def top_company(dict_com):
    sorted_dict = sorted(dict_com.values())
    empty_dict = {}  # O(1)
    for i in range(1, 4):
        for key in dict_com.keys():  # O(1)
            if dict_com[key] == sorted_dict[-i]:  # O(1)
                empty_dict[key] = sorted_dict[-i]  # O(1)
    return empty_dict


@memory_time
def top_company_prof(dict_com):
    sorted_dict = sorted(dict_com.values())
    empty_dict = {}  # O(1)
    for i in range(1, 4):
        for key in dict_com.keys():  # O(1)
            if dict_com[key] == sorted_dict[-i]:  # O(1)
                empty_dict[key] = sorted_dict[-i]  # O(1)
    json_d = json.dumps(empty_dict)
    del empty_dict
    return json_d


company = {chr(i): round(i * randint(1, 300)) for i in range(100, 11000)}
print(top_company(company))
print(top_company_prof(company))

'''
оригинальная функция
Время: 0.12028470000000002
Память: 0.0234375

Измененная
Время: 0.11432529999999996
Память: 0.0

Уменьшилось время и память. Изменение: в финале функции словарь был заменен на json объект и удален ненужный словарь,
что позволило уменьшить занимаемую память.
'''