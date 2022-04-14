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


def get_user_data():
    company_count = input('Введите количество компаний:\n')
    company_list = []
    profit_sum = 0

    if company_count.isdigit() and int(company_count) != 0:
        company_structure = namedtuple('Company', 'name, profit_1, profit_2, profit_3, profit_4, profit_sum')
        while_range = int(company_count)

        while len(company_list) != while_range:
            company_data = input(f'Введите данные {len(company_list)+1} компании: (Наименование: Прибыль1кв, Прибыль2кв, Прибыль3кв, Прибыль4кв):\n')

            try:
                c_name, c_profit = company_data.split(':')
                profit_1, profit_2, profit_3, profit_4 = map(int, c_profit.split(','))
                company = company_structure(c_name, profit_1, profit_2, profit_3, profit_4,
                                            profit_1 + profit_2 + profit_3 + profit_4)
                company_list.append(company)
                profit_sum += company.profit_sum
            except ValueError:
                print('Введены некорректные данные. Попробуйте еще раз')

    else:
        get_user_data()

    return company_list, profit_sum, profit_sum / while_range


"""
Данные для ввода:
test1: 211, 3421, 231, 143
test2: 2121, 3421, 231, 143
test3: 211, 3421, 231, 1432
"""

company_array, profits, avg_profit = get_user_data()
print(f'Среднегодовая прибыль всех предприятий: {round(avg_profit, 2)}')
print(f'Предприятия, с прибылью выше среднего значения: '
      f'{", ".join([comp.name for comp in company_array if comp.profit_sum > avg_profit])}')
print(f'Предприятия, с прибылью ниже среднего значения: '
      f'{", ".join([comp.name for comp in company_array if comp.profit_sum < avg_profit])}')
