# Задание из основ
# Исходная задача использовалась для расчета премии для сотрудников
# Мы взяли только кусок который можно оптимизировать
from pympler import asizeof

class BasicWorker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': income, 'bonus': income * 0.4}


class Worker:
    __slots__ = ['name', 'surname', 'position', 'income']

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': income, 'bonus': income * 0.4}



bw_obj = BasicWorker('Серж', "Абрамов", "рядовой", 15000)
print(f'Размер объекта BasicWorker =  {asizeof.asizeof(bw_obj)}')
w_obj = Worker('Серж', "Абрамов", "рядовой", 15000)
print(f'Размер объекта Worker = {asizeof.asizeof(w_obj)}')

# Размер объекта BasicWorker =  608
# Размер объекта Worker = 416
'''
В basic классе используется обычная инициализация, и все атрибуты класса при этом хранятся в словарях
Словари же имеют большой размер, так как в python они реализованы как хеш таблицы
Использовав конструкцию slots мы сокращаем затраты на хранение атрибутов, так как теперь мы будет хранить
свои атрибуты в словарях, а они требуют меньше памяти для хранения
'''
