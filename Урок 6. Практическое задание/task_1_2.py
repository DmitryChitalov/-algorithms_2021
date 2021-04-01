"""
Задание 1. Скрипт № 2

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import memory_usage
from pympler import asizeof


class WorkerSiple:
    """Класс Worker(Рабочий)"""

    def __init__(self, name, surname, position, wage, bonus):
        """
        Конструктор принимает
        :param name (str): имя
        :param surname (str): фамилия
        :param position (str): должность
        :param wage (int): оклад
        :param bonus (int): премия
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class PositionSimple(WorkerSiple):
    """
    Класс Position (Должность) наследующет атрибуты класса Worker
    """

    def get_full_name(self):
        """Метод для вывода имени и фамилии"""

        print(self.name, self.surname)

    def get_total_income(self):
        """Метод для вывода полного дохода"""

        profit = self._income['wage'] + self._income['bonus']
        return profit


class WorkerSlots:
    """Класс Worker(Рабочий)"""
    __slots__ = ('name', 'surname', 'position', 'wage', 'bonus', '_income')

    def __init__(self, name, surname, position, wage, bonus):
        """
        Конструктор принимает
        :param name (str): имя
        :param surname (str): фамилия
        :param position (str): должность
        :param wage (int): оклад
        :param bonus (int): премия
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class PositionSlots(WorkerSlots):
    """
    Класс Position (Должность) наследующет атрибуты класса Worker
    """

    def get_full_name(self):
        """Метод для вывода имени и фамилии"""

        print(self.name, self.surname)

    def get_total_income(self):
        """Метод для вывода полного дохода"""

        profit = self._income['wage'] + self._income['bonus']
        return profit


def mem_func_first():
    """
    Функция для проверки пиковой памяти при работе
    с объектами класса без __slots__
    """
    return first.get_total_income()


def mem_func_second():
    """
    Функция для проверки пиковой памяти при работе с
    объектами класса c использованием __slots__
    """
    return second.get_total_income()


if __name__ == '__main__':
    first = PositionSimple('Bob', 'Smith', 'manager', 50000, 5000)
    print(first.__dict__)
    print(f'Память {type(first)}: {asizeof.asizeof(first)}\n'
          f'{"-" * 40}')

    second = PositionSlots('Bob', 'Smith', 'manager', 50000, 5000)
    print(second.__slots__)
    print(f'Память {type(second)}: {asizeof.asizeof(second)}\n'
          f'{"-" * 40}')

    first.get_full_name()

    print(f'WorkerSiple {mem_func_first()}')
    mem = max(memory_usage(proc=mem_func_first))
    print(f'Максимальная память: {mem} MiB')

    second.get_full_name()

    print(f'WorkerSlots {mem_func_second()}')
    mem = max(memory_usage(proc=mem_func_second))
    print(f'Максимальная память: {mem} MiB')

"""
При опримизации данного скрипта были добавлены слоты в класс.
Результаты замеров:
{'name': 'Bob', 'surname': 'Smith', 'position': 'manager', '_income': {'wage': 50000, 'bonus': 5000}}
Память <class '__main__.PositionSimple'>: 960
----------------------------------------
('name', 'surname', 'position', 'wage', 'bonus', '_income')
Память <class '__main__.PositionSlots'>: 776
----------------------------------------
Bob Smith
WorkerSiple 55000
Максимальная память: 19.1875 MiB
WorkerSlots 55000
Максимальная память: 19.19921875 MiB

Результаты замеров подтверждают, что использование __slots__ в ООП дает хорошие результаты
по профилированию памяти занимаемой объектами класса. 
"""
