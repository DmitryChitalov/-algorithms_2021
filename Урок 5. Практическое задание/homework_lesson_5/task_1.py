from collections import namedtuple

company = namedtuple('firm', ['name', 'q1', 'q2', 'q3', 'q4'])


def average(avg):
    return avg.q1 + avg.q2 + avg.q3 + avg.q4


def company_profit():
    company_list = []
    less = []
    more = []
    number_firm = int(input('Введите количество предприятий для расчета прибыли: '))

    for i in range(number_firm):
        firm = input('Введите название предприятия: ')
        profits = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        company_list.append(company(firm, *map(int, profits.split())))

    avg_profit = sum(map(average, company_list)) / len(company_list)
    print(f'Средняя годовая прибыль всех предприятий: {avg_profit}')

    for elem in company_list:
        if average(elem) < avg_profit:
            less.append(elem.name)
        elif average(elem) > avg_profit:
            more.append(elem.name)

    print(f'Предприятия, с прибылью выше среднего значения: {", ".join(more)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(less)}')


company_profit()
