from collections import namedtuple
from recordclass import recordclass
from memory_profiler import memory_usage
from timeit import default_timer


def mem_time_prof(func):
    def wrapper(*args, **kwargs):
        time1 = default_timer()
        m1 = memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        time2 = default_timer()
        print(f'Время выполнения: {time2 - time1}\nИспользуемая память: {m2[0] - m1[0]} MiB')
        return res
    return wrapper


@mem_time_prof
def company_calc():
    n = int(input('Введите количество предприятий для расчета прибыли: '))
    RES = namedtuple('Profit', 'company year_profit')
    profit_list = {}

    for i in range(n):
        company_data = RES(
            company=input('Введите название компании: '),
            year_profit=list(map(lambda x: float(x), input('Через пробел введите прибыль поквартально: ').split()
                                 )))
        profit_list[company_data.company] = sum(company_data.year_profit)

    total_year_profit = 0
    for val in profit_list.values():
        total_year_profit += val
    aver_year_profit = total_year_profit / n

    for key, val in profit_list.items():
        if val < aver_year_profit:
            print(f'Прибыль компании {key} составляет {val} - это меньше среднего значения')
        elif val > aver_year_profit:
            print(f'Прибыль компании {key} составляет {val} - это больше среднего значения')
        else:
            print(f'Прибыль компании {key} составляет {val} - это на срендем уровне')


@mem_time_prof
def calc_optimized():
    n = int(input('Введите количество предприятий для расчета прибыли: '))
    RES = recordclass('Profit', ['company', 'year_profit'])
    profit_list = {}

    for i in range(n):
        company_data = RES(
            company=input('Введите название компании: '),
            year_profit=list(map(lambda x: float(x), input('Через пробел введите прибыль поквартально: ').split()
                                 )))
        profit_list[company_data.company] = sum(company_data.year_profit)

    total_year_profit = 0
    for val in profit_list.values():
        total_year_profit += val
    aver_year_profit = total_year_profit / n

    for key, val in profit_list.items():
        if val < aver_year_profit:
            print(f'Прибыль компании {key} составляет {val} - это меньше среднего значения')
        elif val > aver_year_profit:
            print(f'Прибыль компании {key} составляет {val} - это больше среднего значения')
        else:
            print(f'Прибыль компании {key} составляет {val} - это на срендем уровне')


if __name__ == '__main__':
    print(f'Решение с namedtuple: ')
    company_calc()
    print('###########################################################')
    print(f'Решение с recordclass: ')
    calc_optimized()

'''
Решение с namedtuple: 
Время выполнения: 40.6611612
Используемая память: 0.0625 MiB
###########################################################
Решение с recordclass: 
Время выполнения: 57.578350900000004
Используемая память: -0.0390625 MiB
ВЫВОД: recordclass работает несколько медленнее, чем namedtuple, но потребляет 
меньше памяти. 
'''

# АЛЬТЕРНАТИВНОЕ РЕШЕНИЕ ТОЙ ЖЕ ЗАДАЧИ:
# решение с namedtuple

from collections import namedtuple
from recordclass import recordclass
from memory_profiler import memory_usage
from timeit import default_timer


def mem_time_prof(func):
    def wrapper(*args, **kwargs):
        time1 = default_timer()
        m1 = memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        time2 = default_timer()
        print(f'Время выполнения: {time2 - time1}\nИспользуемая память: {m2[0] - m1[0]} MiB')
        return res
    return wrapper


COMPANY_DATA = (('company_1', '2000 3000 4000 5000'), ('company_2', '1000 2000 3000 4000'))


def add_to_companies_list(com_lst, lst, *args):
    company = lst(*args)
    com_lst.append(company)


def calc_avg_profit(lst):
    return sum([company.revenue for company in lst]) / len(lst)


def classify_companies(lst, aver_prof):
    above_average, below_average = [], []
    for company in lst:
        if company.revenue >= aver_prof:
            above_average.append(company.name)
        else:
            below_average.append(company.name)
    return above_average, below_average


@mem_time_prof
def nt_func():
    companies = namedtuple('company', ['name', 'revenue'])
    companies_lst = []
    for i in range(2):
        company_name, revenue = COMPANY_DATA[i]
        add_to_companies_list(companies_lst, companies, company_name, sum(map(int, revenue.split())))
    avg_profit = calc_avg_profit(companies_lst)
    above_average, below_average = classify_companies(companies_lst, avg_profit)
    return f"Прибыль {''.join(above_average)} выше среднего уровня. " \
           f"Прибыль {''.join(below_average)} ниже среднего уровня"


# РЕШЕНИЕ с recordclass:

@mem_time_prof
def rc_func():
    companies = recordclass('company', ['name', 'revenue'])
    companies_lst = []
    for i in range(2):
        company_name, revenue = COMPANY_DATA[i]
        add_to_companies_list(companies_lst, companies, company_name, sum(map(int, revenue.split())))
    avg_profit = calc_avg_profit(companies_lst)
    above_average, below_average = classify_companies(companies_lst, avg_profit)
    return f"Прибыль {''.join(above_average)} выше среднего уровня. " \
           f"Прибыль {''.join(below_average)} ниже среднего уровня"


if __name__ == '__main__':
    print(f'Решение с namedtuple: ')
    print(nt_func())
    print('###########################################################')
    print(f'Решение с recordclass: ')
    print(rc_func())

'''
Решение с namedtuple: 
Время выполнения: 0.2139108
Используемая память: 0.015625 MiB
###########################################################
Решение с recordclass: 
Время выполнения: 0.21959999999999996
Используемая память: 0.0234375 MiB

ВЫВОД: В данном варианте решения с точки зрения, скорости
оба инструмента сработали практически одинаково. С т. зр. затрат памяти 
замер показывает,  что разницы тоже практически нет.  
'''
