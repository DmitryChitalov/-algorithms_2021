from pympler.asizeof import asizeof
"""
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. 
метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road1:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weight = 25
        self.thickness = 5

    def total_weight(self):
        tw = (self.length * self.width * self.weight * self.thickness) / 1000
        print(f'Общий вес асфальта необходимово для покрытия дороги {tw}'
              f' тонн(ы).')


# оригинал
class Road2:
    __slots__ = ['length', 'width', 'weight', 'thickness']

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weight = 25
        self.thickness = 5

    def total_weight(self):
        tw = (self.length * self.width * self.weight * self.thickness) / 1000
        print(f'Общий вес асфальта необходимово для покрытия дороги {tw}'
              f' тонн(ы).')


# Профилировка по памяти с помощью __slots__
road_1 = Road1(5000, 25)
road_2 = Road2(5000, 25)
print(asizeof(road_1))
print(asizeof(road_2))
"""
Использование __slots__ привело к уменьшению размера экземпляра класса
road_1 = 480
road_2 = 160
"""