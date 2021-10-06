from collections import namedtuple

companies = []
amount_of_companies = int(input('Введите кол-во предприятий для расчета прибыли: '))
for i in range(amount_of_companies):
    comp = namedtuple('report', 'name income1 income2 income3 income4 full_income')
    name_of_comp = input('Введите название предприятия: ')
    income_of_comp = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
    Company = comp(name_of_comp, *income_of_comp.split(), sum(map(int, income_of_comp.split())))
    companies.append(Company)

middle_income = sum(Company.full_income for Company in companies) / len(companies)
print(f"Средняя годовая прибыль всех предприятий: {middle_income}")
print("Предприятия, с прибылью выше среднего значения: ")
print(*(Company.name for Company in companies if Company.full_income >= middle_income))
print("Предприятия, с прибылью ниже среднего значения: ")
print(*(Company.name for Company in companies if Company.full_income < middle_income))
