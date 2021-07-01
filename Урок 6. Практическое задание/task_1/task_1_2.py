from collections import namedtuple
from recordclass import recordclass
from pympler import asizeof
from sys import getsizeof

Сompanies = namedtuple('companies', 'name first_quarter second_quarter third_quarter fourth_quarter')
Сompanies_1 = recordclass('companies_1', 'name first_quarter second_quarter third_quarter fourth_quarter')
number_of_companies = int(input('Введите количество компаний'))


def aver_profit(num_of_comp):
    profit_avr = {}
    for i in range(num_of_comp):
        companies = Сompanies(
            name=input('название'),
            first_quarter=int(input('Введите значение прибыли для 1 квартала ')),
            second_quarter=int(input('Введите значение прибыли для 2 квартала ')),
            third_quarter=int(input('Введите значение прибыли для 3 квартала ')),
            fourth_quarter=int(input('Введите значение прибыли для 4 квартала ')))

        profit_avr[companies.name] = round((companies.first_quarter +
                                            companies.second_quarter +
                                            companies.third_quarter +
                                            companies.fourth_quarter) / 4, 2)

    total_profit_avr = round(sum(profit_avr.values()) / num_of_comp)

    for key, values in profit_avr.items():
        if values > total_profit_avr:
            print(f'У компании {key} прибыль выше среднего')
        elif values < total_profit_avr:
            print(f'У компании {key} прибыль ниже среднего')


if __name__ == '__main__':
    # aver_profit(number_of_companies)
    a = Сompanies(name='qwerty', first_quarter=20, second_quarter=25, third_quarter=20, fourth_quarter=35)
    b = Сompanies_1(name='qwerty', first_quarter=20, second_quarter=25, third_quarter=20, fourth_quarter=35)
    print(f'Объем занимаемой памят объектом namedtuple = {asizeof.asizeof(a)}')
    print(f'Объем занимаемой памят объектом recordclass = {asizeof.asizeof(b)}')
    print(f'Объем занимаемой памят объектом namedtuple = {getsizeof(a)}')
    print(f'Объем занимаемой памят объектом recordclass = {getsizeof(b)}')

"""
Мы видим, что при создании объекта recordclass память переменной ниже, но общий размер всего объекта больше, 
чем у namedtuple
Объем занимаемой памят объектом namedtuple = 232
Объем занимаемой памят объектом recordclass = 1048
Объем занимаемой памят объектом namedtuple = 80
Объем занимаемой памят объектом recordclass = 64
"""
