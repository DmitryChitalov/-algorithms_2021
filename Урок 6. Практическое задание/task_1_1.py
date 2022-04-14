import memory_profiler
import timeit
from pympler.asizeof import asizeof
import json


def profiler(func):
    def wrapper(*args):
        start_time = timeit.default_timer()
        mem_start = memory_profiler.memory_usage()[0]
        func_result = func(*args)
        time_taken = timeit.default_timer() - start_time
        mem_used = memory_profiler.memory_usage()[0] - mem_start
        print("*" * 150)
        print(f"Функция {func.__name__} выполнялась {time_taken} сек и занимала в памяти {mem_used} MiB")
        print("*" * 150)
        return func_result

    return wrapper


@profiler
def find_profitable_companies_1(company_profits):
    """
    Функция получает на вход словарь {company_profit : company_name}.
    Находит максимальный профит, перебирая и сравнивая значения всех ключей,
    затем удаляет найденый максимальный элемент и
    добавляет его в словарь с результатами
    Сложность данного алгоритма: 2*n + 18 (линейная)
    """
    most_profitable = dict()  # O(1)
    for i in range(3):  # O(1)
        dict_items = list(company_profits.items())  # O(n)
        max_profit = dict_items[0][1]  # O(1) + O(1) + O(1)
        for j in range(1, len(dict_items)):  # O(n) + O(1)
            if max_profit < dict_items[j][1]:  # O(1) + O(1) + O(1)
                max_profit = dict_items[j][1]  # O(1) + O(1) + O(1)
                company_name = dict_items[j][0]  # O(1) + O(1) + O(1)
        most_profitable.update({company_name: company_profits.pop(company_name)})  # O(1) + O(1)
    return most_profitable  # O(1)


@profiler
def find_profitable_companies_2(company_profits_json):
    """
    Функция принимает на вход json словарь, производит десериализацию
    """
    company_profits = json.loads(company_profits_json)
    most_profitable = dict()  # O(1)
    for i in range(3):  # O(1)
        dict_items = list(company_profits.items())  # O(n)
        max_profit = dict_items[0][1]  # O(1) + O(1) + O(1)
        for j in range(1, len(dict_items)):  # O(n) + O(1)
            if max_profit < dict_items[j][1]:  # O(1) + O(1) + O(1)
                max_profit = dict_items[j][1]  # O(1) + O(1) + O(1)
                company_name = dict_items[j][0]  # O(1) + O(1) + O(1)
        most_profitable.update({company_name: company_profits.pop(company_name)})  # O(1) + O(1)
    return most_profitable  # O(1)


my_dict = {str(i): i for i in range(1000)}
print(f"размер словаря до сериализации: {asizeof(my_dict)}")
json_dict = json.dumps(my_dict)

print(find_profitable_companies_1(my_dict))
print(f"размер словаря сериализованного: {asizeof(json_dict)}")
print(find_profitable_companies_2(json_dict))

"""
Вывод: 
Использование сериализации\десериализации значительно сокращает затраты памяти.
размер словаря до сериализации: 124952
размер словаря сериализованного: 11832
"""