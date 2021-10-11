from pympler import asizeof

# Курс основ


class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc_weight(self):
        m = (self.__length * self.__width * 25 * 5) / 1000
        return round(m, 2)


class NewRoad:
    __slots__ = ('length', 'width')

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_weight(self):
        m = (self.length * self.width * 25 * 5) / 1000
        return round(m, 2)


if __name__ == '__main__':
    road = Road(30, 6000)
    print(f"Размер объекта: {asizeof.asizeof(road)}")
    print(f"Необходимо {road.calc_weight()} тонн")
    road2 = NewRoad(30, 6000)
    print(f"Размер объекта: {asizeof.asizeof(road2)}")
    print(f"Необходимо {road2.calc_weight()} тонн")

    """
        Размер объекта: 344
        Необходимо 22500.0 тонн
        Размер объекта: 112
        Необходимо 22500.0 тонн
        
        __slots__, позволяет не использовать динамический словарь для атрибутов и их значений, 
        заменив его на кортеж,  мы экономим память. 
        
    """