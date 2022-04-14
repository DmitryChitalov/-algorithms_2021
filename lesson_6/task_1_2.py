"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
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
from memory_profiler import profile
from pympler import asizeof


class RoadOne:
    @profile
    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def calculation(self):
        __weight = 25
        __thickness = 5
        __result = self._lenght * self._width * __weight * __thickness // 1000
        return f'{self._lenght}м * {self._width}м * {__weight}кг * {__thickness}см = {__result}т'


class RoadTwo:
    __slots__ = '_lenght', '_width'

    @profile
    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def calculation(self):
        __weight = 25
        __thickness = 5
        __result = self._lenght * self._width * __weight * __thickness // 1000
        return f'{self._lenght}м * {self._width}м * {__weight}кг * {__thickness}см = {__result}т'


my_road_1 = RoadOne(4000, 15)
my_road_2 = RoadTwo(4000, 15)
print(asizeof.asizeof(my_road_1))  # Без использования слотов: 328
print(asizeof.asizeof(my_road_2))  # С использованием слотов: 112

# Оптимизация класса использованием слотов
# Снижение затрат памяти в 3 раза
