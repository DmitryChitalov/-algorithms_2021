"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from pympler import asizeof

'''
Для второго примера взяла задание из основ
Для оптимизации использовала конструкцию __slots__
конструкция не использует динамический словарь для хранения атрибутов и их значений, а хранит в кортеже
В результате мы не можем добавлять/ изменять  атрибуты, зато программа использует меньше памяти

Результаты замеров:

asizeof.asizeof(road_1) = 184 
asizeof.asizeof(road_2) = 56 - с конструкцией slots
'''


#  Реализовать класс Stationery (канцелярская принадлежность).
#  Определить в нем атрибут title (название) и метод draw (отрисовка).
#  Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
#  Pen (ручка), Pencil (карандаш), Handle (маркер).
#  В каждом из классов реализовать переопределение метода draw.
#  Для каждого из классов методы должен выводить уникальное сообщение.
#  Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asph_mass(self):
        mass_square = 25  # covering one square meter constant value
        bed_thickness = 5  # asphalt bed thickness constant value
        return self._length * self._width * mass_square * bed_thickness


road_1 = Road(20, 5000)


class Road_new:
    __slots__ = ['_length', '_width']

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asph_mass(self):
        mass_square = 25  # covering one square meter constant value
        bed_thickness = 5  # asphalt bed thickness constant value
        return self._length * self._width * mass_square * bed_thickness


road_2 = Road_new(20, 5000)
print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {road_1.asph_mass()} кг')
print(asizeof.asizeof(road_1))
print(asizeof.asizeof(road_2))
