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


def insert_data():
    """
    Функция получающая данные от пользователя для наполнения namedtuple
    :return (namedtuple): данные о компании
    """
    name = input('Введите название компании: ')

    while True:
        qr_profit = input('Введите через пробел квартальную прибыль компании (4 квартала): ').split()

        try:
            qr_profit = [int(x) for x in qr_profit]
            if len(qr_profit) != 4:
                raise Exception('Введено неустановленное количество значений квартальной прибыли!!!')
            break
        except ValueError:
            print('Введены данные несоответствующие установленным параметрам!!!')
            continue
        except Exception as e_len:
            print(e_len)
            continue

    inform = comp_data(
        name=name,
        qr_profit_1=qr_profit[0],
        qr_profit_2=qr_profit[1],
        qr_profit_3=qr_profit[2],
        qr_profit_4=qr_profit[3]
    )
    return inform


if __name__ == '__main__':
    while True:
        comp_data = namedtuple('Company',
                               'name qr_profit_1 qr_profit_2 qr_profit_3 qr_profit_4')
        comp_list = []
        over_profit = 0

        print('=' * 50)
        number = input('Для выхода введите "0"\n'
                       'Введите количество компаний: ')
        if number == "0":
            print('Выход')
            break

        try:
            number = int(number)
        except ValueError:
            print('Не введено численное значение!!!')
            continue

        for i in range(number):
            comp_list.append(insert_data())
            over_profit += sum(comp_list[i][1:])

        comp_good = []
        comp_bad = []
        for i in range(number):
            if sum(comp_list[i][1:]) >= over_profit / number:
                comp_good.append(comp_list[i].name)
            else:
                comp_bad.append(comp_list[i].name)

        print('-' * 50)
        print(f'Средняя годовая прибыль всех компаний: {over_profit / number}')
        print(f'Компании, с прибылью выше среднего значения: {", ".join(comp_good)}')
        print(f'Компании, с прибылью ниже среднего значения: {", ".join(comp_bad)}')