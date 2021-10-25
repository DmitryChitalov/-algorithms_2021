from collections import namedtuple


def calculation_function():
    entering_quantity = int(input('Введите количество предприятий для расчета: '))
    compilation = namedtuple('company', 'company_name quarter_1 quarter_2 quarter_3 quarter_4')
    data_storage = {}
    the_amount = 0

    for _ in range(entering_quantity):
        conclusion = compilation(company_name=input('введите название '),
                                 quarter_1=int(input('введите прибыль за 1 квартал ')),
                                 quarter_2=int(input('введите прибыль за 2 квартал ')),
                                 quarter_3=int(input('введите прибыль за 3 квартатла ')),
                                 quarter_4=int(input('введите прибыль за 4 квартатла ')))

        data_storage[conclusion.company_name] = (conclusion.quarter_1 + conclusion.quarter_2 +
                                                 conclusion.quarter_3 + conclusion.quarter_4) / 4

    for meaning in data_storage.values():
        the_amount += meaning
    the_amount /= entering_quantity

    for k_company, v_amount in data_storage.items():
        if v_amount > the_amount:
            print(f'фирма {k_company} выше среднего')
        else:
            print(f'фирма {k_company} ниже среднего')
    print(f'Общая среднегодовая прибыль всех фирм составила {the_amount} рублей')


calculation_function()

"""
    Введите количество предприятий для расчета: 2
    
    введите название SAMSUNG
    введите прибыль за 1 квартал 258000
    введите прибыль за 2 квартал 11000
    введите прибыль за 3 квартатла 432000
    введите прибыль за 4 квартатла 9000
    
    введите название APPLE
    введите прибыль за 1 квартал 362000
    введите прибыль за 2 квартал 8020
    введите прибыль за 3 квартатла 264000
    введите прибыль за 4 квартатла 22000
    
    фирма SAMSUNG выше среднего
    фирма APPLE ниже среднего
    
    Общая среднегодовая прибыль всех фирм составила 170752.5 рублей
"""
