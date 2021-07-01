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


# служебная функция для проверки введенных цифр
def check_number(string):
    if string.isdigit():
        result = int(string)
    else:
        try:
            result = float(string)
        except ValueError:
            result = 0
    return result


# Получение среднего и наименований фирм.
def get_average(lst):
    result = []
    for el in lst:
        result.append(sum([check_number(num) for num in el]) / 4)   # Оставил генератором, чтобы потом получать индекс
    average = sum(result) / len(lst)
    print(f'Средняя годовая прибыль всех предприятий: {average} \n')
    print(f'Предприятия, с прибылью выше среднего значения: '
          f'{str([lst[i].name for i, el in enumerate(result) if el > average])}')
    print(f'Предприятия, с прибылью ниже среднего значения: '
          f'{[lst[i].name for i, el in enumerate(result) if el < average]}')


#  Введение данных, контроль введенных данных
def input_firms():
    data = []
    messages = ['Введите название предприятия: ',
                'Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): \n',
                'Вы ошибочно ввели данные. \n']
    count_firms = input('Введите количество предприятий для расчета прибыли. Необходимо целое число:\n ')
    firm = namedtuple('firm', ['name', 'first_quarter', 'second_quarter', 'thr_quarter', 'fore_quarter'])

    if check_number(count_firms) != 0:
        for i in range(int(count_firms)):
            name = input(messages[0] + str(i + 1) + '\n')
            res = (input(messages[1])).split(' ')
            if len(res) == 4 and name != 0:
                data.append(firm(name=name, first_quarter=res[0], second_quarter=res[1],
                                 thr_quarter=res[2], fore_quarter=res[3]))
            else:
                print(messages[2])
                input_firms()
    else:
        print(messages[2])
        input_firms()
    get_average(data)


input_firms()

