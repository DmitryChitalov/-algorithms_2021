from pympler import asizeof

class Road:

    def __init__(self, length, width):
        self._l = length
        self._w = width

    def calc(self, sm, kg):
        weight = self._l * self._w * sm * kg // 1000
        print(f"Для дороги длинной {self._l} м. и шириной {self._w} м. нужно {weight} т. асфальта")

class Road_2:

    __slots__ = ['_l', '_w']
    def __init__(self, length, width):
        self._l = length
        self._w = width

    def calc(self, sm, kg):
        weight = self._l * self._w * sm * kg // 1000
        print(f"Для дороги длинной {self._l} м. и шириной {self._w} м. нужно {weight} т. асфальта")

road_1 = Road(1000, 5)
road_1.calc(5, 25)
print(asizeof.asizeof(road_1))
road_2 = Road_2(1000, 5)
road_2.calc(5, 25)
print(asizeof.asizeof(road_2))

""" Использование слотов экономит память, за счет более экономичного контейнера. Список вместо словаря."""