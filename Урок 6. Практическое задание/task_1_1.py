from memory_profiler import memory_usage
from timeit import default_timer


def memory_time_profiler(func):
    def wrapper(*args, **kwargs):
        time1 = default_timer()
        m1 = memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        time2 = default_timer()
        print(f'Время выполнения: {time2 - time1}\nИспользуемая память: {m2[0] - m1[0]} MiB')
        return res
    return wrapper


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'


@memory_time_profiler
def main():
    print('Базовый код')
    car = Car(80, 'красный', 'Mini Cooper', True)
    print(car.go())
    return car


class CarNew:
    __slots__ = ('speed', 'color', 'name', 'is_police')

    def __init__(self, speed, color, name, is_police=False):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        return 'Машина поехала'


@memory_time_profiler
def main_new():
    print('Рефакторинг')
    car = CarNew(80, 'красный', 'Mini Cooper', True)
    print(car.go())
    return car


if __name__ == '__main__':
    main()
    main_new()

"""
Базовый код
Машина поехала
Время выполнения: 0.2093591
Используемая память: 0.00390625 MiB

Рефакторинг
Машина поехала
Время выполнения: 0.21658199999999994
Используемая память: 0.0 MiB
Отредактированный код выполняется чуть медленее, поскольку __slots__ отрабатывает с меньшей скоростью, чем __dict__,
так как создается дескриптор для каждого имени переменной.
Однако использование slots и статичных методов дает выигрыш в памяти, что может быть существенней, учитывая современные
можности машин.
"""
