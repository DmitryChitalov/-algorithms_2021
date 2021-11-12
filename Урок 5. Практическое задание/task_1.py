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


def profit_the_year(sttr):
    return sum((int(i) for i in sttr.split(' ')))


def main():
    # шаблон 
    company = namedtuple('company', 'name_company profit')
    # сколько фирм для расчета будет подано
    how_firms = int(input('Введите количество предприятий для расчета прибыли: '))
    # ввходные данные в список кортежей: [(имя фирмы - тип строка, поквартальные занчения прибыли - тип строка),(...)]
    input_data = [
        (
            input(f'Введите название предприятия # {number+1}: '),
            profit_the_year(
                input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
            )
        ) for number in range(how_firms)
    ]
    # создаю хранилище в виде словаря, где ключ - это имя компании и в тоже врямя как бы переменная, которая будет
    # хранить экземпляр шаблона. То есть для для получения информации по компании нужно:
    # обратиться к словарю, в качестве ключа указать имя компании, а чтобы получить значение прибыли например
    # использовать метод profit
    # storage['имя компании'].profit
    # Таким образом я использовал именованный кортеж и вышло уйти от "шифрокода"
    storage = {name_company: company(name_company=name_company, profit=profit) for name_company, profit in input_data}
    # считаю среднию годовую прибыль всех предприятий
    average_profit = sum([storage[name_company].profit for name_company in storage]) / how_firms
    # блок возрата - тут все очень варияативно, прописал так как есть.
    # возращаю Ф-строчищу в которую впихано 2 списка - у кого выше и ниже средней
    return f'''Средняя годовая прибыль всех предприятий: {average_profit}
===>Предприятия, с прибылью выше среднего значения:
===>{[storage[_].name_company for _ in storage if storage[_].profit > average_profit]}
===>Предприятия, с прибылью ниже среднего значения:
===>{[storage[_].name_company for _ in storage if storage[_].profit < average_profit]}'''


print(main())

# Пример выполнения
# Введите количество предприятий для расчета прибыли: 3
# Введите название предприятия # 1: company_1
# через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 50 70 50 80
# Введите название предприятия # 2: company_2
# через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 20 20 30 40
# Введите название предприятия # 3: company_3
# через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 60 60 50 70
# Средняя годовая прибыль всех предприятий: 200.0
# ===>Предприятия, с прибылью выше среднего значения:
# ===>['company_1', 'company_3']
# ===>Предприятия, с прибылью ниже среднего значения:
# ===>['company_2']