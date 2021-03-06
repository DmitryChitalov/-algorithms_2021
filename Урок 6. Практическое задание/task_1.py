from pympler import asizeof
from memory_profiler import profile
from functools import reduce
"""
Задание 1.

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


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Worker1:
    __slots__ = ('name', 'surname', 'position', 'wage', 'income')

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


@profile
def find_index(number):
    my_list = [x ** 2 for x in range(1, 100000, 2) if x % 2 != 0]
    for elements in my_list:
        if elements == number * number:
            value = my_list[elements]
            return value


@profile
def find_index1(number):
    my_list = [x ** 2 for x in range(1, 100000, 2) if x % 2 != 0]
    for elements in my_list:
        if elements == number * number:
            value = my_list[elements]
            del my_list
            return value


@profile
def new_list(my_list):
    n_list = [x ** 2 for x in my_list]
    return n_list


@profile
def new_list_opt(my_list):
    n_list = map(lambda x: x ** 2, my_list)
    return n_list


"""
1
В двух класс видно явное изменения занимаемой памяти, так как я использовал __slots__, чтобы вместо словаря был кортеж.
Это привело к снижению затрат памяти с 960 до 648. Здесь можно из использовать, так как добавление новых строк не нужно.
2
В двух функциях имеются различия в занимаемой памяти, так как во второй мы используем del для списка, что  снижает
затраты в памяти. Так же у нас в последнем инкременте появилось отрицательное число, видимо из-за удаления.
3
При использовании функций можно сильно снизить потребляемость памяти.

"""

if __name__ == "__main__":
    Egor = Worker("Ivan", 'Bubnov', "worker", 10000000, 500000)
    print(Egor.__dict__)
    print(asizeof.asizeof(Egor))

    Ivan = Worker1("Ivan", 'Bubnov', "worker", 10000000, 500000)
    print(Ivan.__slots__)
    print(asizeof.asizeof(Ivan))

    print(find_index(77))
    print(find_index1(77))

    m_list = [x for x in range(1, 100000, 2)]
    print(new_list(m_list))
    generator = new_list_opt(m_list)
    for elems in generator:
        print(elems)
