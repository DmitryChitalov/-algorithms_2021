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
import collections


def collect_companies_data():
    companies = []
    try:
        companies_number = int(input("Введите количество предприятий для расчета прибыли: "))
        for i in range(companies_number):
            comp_name = input("Введите название предприятия: ")
            profits = input("через пробел введите прибыль данного предприятия "
                            "за каждый квартал(Всего 4 квартала): ")

            company_profit = collections.namedtuple("company",
                                                    "company_name q_1_profit q_2_profit q_3_profit q_4_profit")
            companies.append(company_profit(comp_name, *[int(elem) for elem in profits.split(' ')]))
    except (ValueError, TypeError):
        print("Неверный ввод!!!")

    return companies


def avg_company_profit(company_profit):
    return (company_profit.q_1_profit + company_profit.q_2_profit
            + company_profit.q_3_profit + company_profit.q_4_profit) / 4


def all_companies_avg_profit(companies):
    total_profit = 0
    for company in companies:
        total_profit += avg_company_profit(company)
    return total_profit / len(companies) if len(companies) > 0 else "Не было введено ни одной компании"


data = collect_companies_data()
total_avg_prof = all_companies_avg_profit(data)
print(f"Средняя прибыль компаний: {total_avg_prof}")
print("Компании с прибылью выше среднего:")
print(*[data[i].company_name for i in range(len(data)) if avg_company_profit(data[i]) > total_avg_prof], sep=', ')
print("Компании со средней прибылью или ниже среднего:")
print(*[data[i].company_name for i in range(len(data)) if avg_company_profit(data[i]) <= total_avg_prof], sep=', ')
