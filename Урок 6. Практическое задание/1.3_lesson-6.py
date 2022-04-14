import json
from pympler import asizeof


companies_profits = {
    "Enigma": 1150,
    "ZORO": 980,
    "ABC-advance": 2470,
    "IT space": 740,
    "Constalletion": 78,
    "ONB": 9871,
    "Easy move": 190,
    "GDD": 999,
    "IT-karma": 0,
    "SUP": 8496
}

# Решение 1:
def get_top_three_1(dict_obj):
    top_three = {}
    transit_dict = dict_obj.copy()
    while len(dict_obj) - len(transit_dict) < 3:
        max_profit = 0
        for c, p in transit_dict.items():
            if p > max_profit:
                max_profit = p
                company = c
        top_three[company] = max_profit
        del transit_dict[company]
    del max_profit # удаляю ненужный объект
    del transit_dict # удаляю ненужный объект
    print('Размер dict: ', asizeof.asizeof(top_three))
    dumped_top_three = json.dumps(top_three) # сериализация словаря в json-формат
    print('Размер json: ', asizeof.asizeof(dumped_top_three))
    print(type(dumped_top_three))
    del top_three # удаляю словарь, top_three = json.loads(get_top_three_1(dict_obj) - при необходимости
    return dumped_top_three


print(f'top three companies ranged by year profit: {get_top_three_1(companies_profits)}')

# Размер dict:  504
# Размер json:  96
# <class 'str'> - класс строка!!!
# top three companies ranged by year profit: {"ONB": 9871, "SUP": 8496, "ABC-advance": 2470}

# Вывод: использование json-формата для преобразования словаря в строку позволило сократить
# размер хранимых данных в 5 раз (в данном конкретном случае), при увеличении размера данных в словаре
# этот коэфи-т увеличивается, соответственно, достигается оптимизация занятой памяти