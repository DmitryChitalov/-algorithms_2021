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

class Company:
    def __init__(self):
        self.company_arr = []
        self.c = namedtuple('company', 'name first_quarter second_quarter third_quarter fourth_quarter')
        self.quantity = int(input('Input the number of companies to calculate the profit: '))

    def fill_collection(self):
        count = 0
        while count < self.quantity:
            company = input(f'Input the name of the company {count + 1}: ')
            self.company_arr.append(company)
            profit = input(
                'Input the profit of this company for each quarter through a space(The total 4 quarters): ').split()
            self.company_arr[count] = self.c(self.company_arr[count], profit[0], profit[1], profit[2], profit[3])
            count += 1
        return ''

    def calc_companies_profit(self):
        above = []
        below = []
        summ = 0
        self.fill_collection()
        for i in self.company_arr:
            summ += int(i.first_quarter) + int(i.second_quarter) + int(i.third_quarter) + int(i.fourth_quarter)
        avg = summ / self.quantity
        for i in self.company_arr:
            if int(i.first_quarter) + int(i.second_quarter) + int(i.third_quarter) + int(i.fourth_quarter) >= avg:
                above.append(i.name)
            else:
                below.append(i.name)
        return f"Avarage year profit of all companies: {avg}\n" \
               f"The companies with above average profit:\n {','.join(above)}\n" \
               f"The companies with below average profit:\n {','.join(below)}"

c = Company()

print(c.calc_companies_profit())