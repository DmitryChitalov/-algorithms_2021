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


name_tuple = namedtuple("company", "name profit")
company_dict = {}

while True:
    try:
        company_sum = int(input("Введите количесивр фирм: "))
        if company_sum <= 0:
            raise ValueError
        break
    except ValueError:
        print("Ошибка. Требуется указать целое число, больше 0. Попробуйте снова.")

for i in range(1, company_sum + 1):
    name = input(f"Введите название {i}-й компании: ")
    while True:
        try:
            user_input_profit = input(f"Введите прибыль по кварталам через пробел: ").split()
            if len(user_input_profit) != 4:
                raise ValueError
            profit = sum(int(i) for i in user_input_profit)
            break
        except ValueError:
            print("Ошибка. Требуется указать 4 целых числа через пробел. Попробуйте снова.")
    company = name_tuple(name=name, profit=profit)
    company_dict[company.name] = profit / 4


average = sum(company_dict.values()) / company_sum
more_aver = [k for k in company_dict if company_dict[k] >= average]
les_aver = [k for k in company_dict if company_dict[k] < average]
print(f"Средняя годовая прибыль всех предприятий: {average:.2f}\n"
      f"Предприятия, с прибылью выше среднего значения: {', '.join(more_aver)}\n"
      f"Предприятия, с прибылью ниже среднего значения: {', '.join(les_aver)}")
