import time
import sys

"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод."""


class TrafficLight:
    # __slots__ = ('color')

    def __init__(self, color):
        self.color = color

    def running(self):
        print(self.color)
        time.sleep(7)
        self.color = 'Yellow'
        print(self.color)
        time.sleep(3)
        self.color = 'Green'
        print(self.color)


class TrafficLight_opt:
    __slots__ = ('color')

    def __init__(self, color):
        self.color = color

    def running(self):
        print(self.color)
        time.sleep(7)
        self.color = 'Yellow'
        print(self.color)
        time.sleep(3)
        self.color = 'Green'
        print(self.color)

if __name__ == '__main__':
    trafficlight_1 = TrafficLight('Red')
    trafficlight_2 = TrafficLight_opt('Red')
    # trafficlight_1.running()
    print(sys.getsizeof(trafficlight_1))
    print(sys.getsizeof(trafficlight_2))

"""Используем __slots__ для оптимизации. Атребутов не много, поэтому цифры небольшие, но всё же удалось
    оптимизировать на 8 байт"""
