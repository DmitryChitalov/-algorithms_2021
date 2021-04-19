"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

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
average_profit = 0
company_lst = []
tup_lst = ['name', 'profit1', 'profit2', 'profit3', 'profit4', 'average']
company = namedtuple('Profits', tup_lst)
print('Расчет средней прибыли предприятий')
while True:
    new_name = input(' Для окончания ввода нажмите Enter\n Введите название фирмы >')
    if len(new_name) == 0:
        break
    lst_profit = [int(i) for i in input('Введите прибыль за 4 квартала через пробел >').split(' ')]
    new_company = company(name=new_name
                          , profit1=lst_profit[0]
                          , profit2=lst_profit[1]
                          , profit3=lst_profit[2]
                          , profit4=lst_profit[3]
                          , average=sum(lst_profit)/len(lst_profit))
    company_lst.append(new_company)
for c in company_lst:
    average_profit += c.average
average_profit /= len(company_lst)
print(f'Среднегодовая прибыль фирм ={average_profit}')
print(f'Фирмы с прибылью выше средней: {", ".join( c.name for c in company_lst if c.average > average_profit)}')
print(f'Фирмы с прибылью равной/ниже средней :{", ".join( c.name for c in company_lst if c.average <= average_profit)}')

