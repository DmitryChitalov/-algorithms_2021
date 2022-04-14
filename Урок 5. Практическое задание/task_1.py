"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple


def sorting_by_profit(some_list, quant_num):
    """Function sorts companies by its profit and outputs values"""
    total_annual_profit = sum(i.sum for i in some_list) / quant_num
    winners, loosers, middlings = [], [], []
    for company in some_list:
        if company.sum > total_annual_profit:
            winners.append(company.name)
        elif company.sum < total_annual_profit:
            loosers.append(company.name)
        else:
            middlings.append(company.name)
    print(f"Средняя годовая прибыль всех предприятий: {total_annual_profit}\n"
          f"Предприятия, с прибылью выше среднего значения: {', '.join(map(str,winners))}\n"
          f"Предприятия, с прибылью ниже среднего значения: {', '.join(map(str,loosers))}\n")
    if len(middlings) > 1:
        print(f"Предприятия с прибылью, равной среднему значению:"
              f" {', '.join(map(str,middlings))}\n")


def data_collection():
    """Function collects initial data and calculates average total profit"""
    quantity = int(input("Введите количество предприятий для расчета прибыли:"))
    my_storage = []
    for elem in range(quantity):
        company_name = input("Введите название предприятия: ")
        RES = namedtuple('Information', ['name', 'sum'])
        annual_profit = sum(map(float, input("Через пробел введите прибыль данного предприятия "
                                             "за каждый отработанный квартал года:").split()))
        my_storage.append(RES(company_name, annual_profit))
    sorting_by_profit(my_storage, quantity)


def annual_report():
    """A startup function that checks the input data"""
    while True:
        try:
            data_collection()
            break
        except ValueError:
            print('Вводите только числа. Попробуйте еще раз')


annual_report()
