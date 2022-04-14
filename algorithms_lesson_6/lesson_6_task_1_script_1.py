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


class Stationery:
    def __init__(self, title, color, name):
        self.title = title
        self.color = color
        self.name = name

    def start(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def drawing(self):
        return f'Ручка {self.color} {self.name} рисует'


@mem_time_prof
def main():
    print(f'Код без оптимизации памяти: ')
    pen = Pen('ручка', 'синяя', 'Parker')
    pen.start()
    print(pen.drawing())


class StatOptimized:
    __slots__ = ('title', 'color', 'name')

    def __init__(self, title, color, name):
        self.title = title
        self.color = color
        self.name = name

    @staticmethod
    def start():
        print('Запуск отрисовки')


class PenNew(StatOptimized):
    def drawing(self):
        return f'Ручка {self.color} {self.name} рисует'


@mem_time_prof
def main_optimized():
    print(f'Код с оптимизацией памяти: ')
    pen = PenNew('ручка', 'красная', 'ErichKrause')
    pen.start()
    print(pen.drawing())


if __name__ == '__main__':
    main()
    print('###############################################################################')
    main_optimized()

'''
Ручка синяя Parker рисует
Время выполнения: 0.2096623
Используемая память: 0.01171875 MiB
###############################################################################
Код с оптимизацией памяти: 
Запуск отрисовки
Ручка красная ErichKrause рисует
Время выполнения: 0.2113503
Используемая память: 0.0 MiB
ВЫВОД: оптимизация кода (использование слотов и статичных методов)дала некоторую экономию памяти, 
однако привела к небольшому росту времени исполнения. Возможно, это связано с работой слотов - кортежи 
работают медленнее словарей. 
'''
