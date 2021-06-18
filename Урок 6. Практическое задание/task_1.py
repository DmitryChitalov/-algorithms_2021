from memory_profiler import memory_usage
from timeit import default_timer


def memory_time(func):
    def wrapper(*args):
        t_1 = default_timer()
        mem_1 = memory_usage()[0]
        result = func(*args)
        print(f'Время: {default_timer() - t_1}\nПамять: {memory_usage()[0] - mem_1}')
        return result

    return wrapper


class Worker:
    # __slots__ = ('name', 'surname', 'position', 'wage', 'bonus', '_income')
    @memory_time
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {'wage': wage, "bonus": bonus}


class Position(Worker):
    __slots__ = ('name', 'surname', 'position', 'wage', 'bonus', '_income')

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        try:
            return float(self._income["wage"]) + float(self._income["bonus"])
        except ValueError:
            return None


###################

class WorkerProf:
    # __slots__ = ('name', 'surname', 'position', 'wage', 'bonus', '_income')
    @memory_time
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {'wage': wage, "bonus": bonus}


class PositionProf(WorkerProf):
    __slots__ = ('name', 'surname', 'position', 'wage', 'bonus', '_income')

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        try:
            return float(self._income["wage"]) + float(self._income["bonus"])
        except ValueError:
            return None


worker = Position('Алена', 'Крива', 'нормировщик', 35000, 20000)

print(worker.name)
print(worker.position)

print(f'Доход сотрудника {worker.get_full_name()}: {worker.get_total_income()}')
print('-' * 100)
worker_prof = Position('Алена', 'Крива', 'нормировщик', 35000, 20000)

print(worker_prof.name)
print(worker_prof.position)

print(f'Доход сотрудника {worker_prof.get_full_name()}: {worker_prof.get_total_income()}')

'''
оригинальная функция
Время: 0.10087200000000002
Память: 0.015625

Измененная
Время: 0.11045510000000003
Память: 0.0

Вместо динамического словаря были введены слоты, к-ые и уменьшили занимаемую память.
'''