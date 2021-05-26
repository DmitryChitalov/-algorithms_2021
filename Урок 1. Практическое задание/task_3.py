"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class CompaniesInfo:
    def __init__ (self, p_dict):
        self.profit_dict = p_dict

    def get_most_profitable_1(self):
        """
        Вариант 1
        Создать два списка: один с названиями, другой с доходом. Отсортировать список с доходом
        и получить перестановки, потом применить их для списка с именами.
        Сложность O(N*logN)
        """
        names = list(self.profit_dict.keys())  # O(N)
        profit_list = []  # O(1)
        for name in names:  # O(N)
            profit_list.append(self.profit_dict[name])  # O(1)
        permutations = sorted(range(len(profit_list)), key=lambda k: profit_list[k], reverse=True)  # O(N*logN)
        most_profitable = {}  # O(1)
        for permutation in permutations[:3]:  # O(1)
            most_profitable[names[permutation]] = profit_list[permutation]  # O(1)
        return most_profitable

    def get_most_profitable_2(self):
        """
        Вариант 2
        Найти максисум, потом максимум из оставшихся значений и затем ещё раз.
        Cложность O(N)
        """
        names = list(self.profit_dict.keys())   #O(N)
        most_profitable = {}                    #O(1)
        for _ in range(3):                      #O(1)
            max_value = 0
            max_name = ''
            for name in names:                  # O(N)
                if name not in most_profitable and self.profit_dict[name] > max_value:  #O(1)
                    max_value = self.profit_dict[name]  #O(1)
                    max_name = name                     #O(1)
            most_profitable[max_name] = max_value       #O(1)
        return most_profitable

    def get_most_profitable_3(self):
        """
        Вариант 3
        Создать два списка с ключами и значениями из словаря.
        Найти три раза максисум при помощи стандартных функций, каждый раз удаляя найденное значение из списков.
        Сложность O(N)
        """
        names = list(self.profit_dict.keys())           # O(N)
        profit_list = []                                # O(1)
        for name in names:                              # O(N)
            profit_list.append(self.profit_dict[name])  # O(1)
        most_profitable = {}                            # O(1)
        for _ in range(3):                              #O(1)
            max_index = profit_list.index(max(profit_list))     #O(N)
            most_profitable[names[max_index]] = profit_list[max_index] #O(1)
            del profit_list[max_index]                  #O(N)
            del names[max_index]                        #O(N)
        return most_profitable

"""    
    Оптимальный второй вариант. Не смотря на то, что 2 и 3 варианты имеют одинаковую сложность O(N), 
    второй вариант потребует в 3 раза меньше времени на выполнение (удаление в третьем варианте очень 
    затратная процедура) - при большом количестве данных разница будет существенна.
    
    Вариант 1 более медленный, но более универсальный. Например, если потребуется выдать 5, 10 или 100 наиболее 
    прибыльных компаний. Правда он также потребует больше затрат по памяти на хранение дополнительных списков.
"""
from random import randint

test_profit_dict = {'name1': 100000, 'name2': 230000, 'name3': 115000, 'name4': 200000, 'name5': 174000}

companies = CompaniesInfo(test_profit_dict)
print('Option1: ', companies.get_most_profitable_1())
print('Option2: ', companies.get_most_profitable_2())
print('Option3: ', companies.get_most_profitable_3())