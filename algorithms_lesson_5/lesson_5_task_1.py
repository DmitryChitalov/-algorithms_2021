from collections import namedtuple


def company_calc():
    n = int(input('Введите количество предприятий для расчета прибыли: '))
    RES = namedtuple('Profit', 'company year_profit')
    profit_list = {}  # словарь, где будут храниться названия компаний и их годовая прибыль

    for i in range(n):
        company_data = RES(
        company=input('Введите название компании: '),
        year_profit=list(map(lambda x: float(x), input('Через пробел введите прибыль поквартально: ').split()
                                  )))
        
        # сразу вычисляем годовую прибыль, т.к. отдельно поквартальные показатели не нужны по условию задачи
        profit_list[company_data.company] = sum(company_data.year_profit)

    total_year_profit = 0
    for val in profit_list.values():
        total_year_profit += val
    aver_year_profit = total_year_profit / n    # среднегодовая прибыль для всех компаний

    for key, val in profit_list.items():    
        if val < aver_year_profit:
            print(f'Прибыль компании {key} составляет {val} - это меньше среднего значения')
        elif val > aver_year_profit:
            print(f'Прибыль компании {key} составляет {val} - это больше среднего значения')
        else:
            print(f'Прибыль компании {key} составляет {val} - это на срендем уровне')

company_calc()
