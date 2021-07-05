from pympler import asizeof

"""
Задачи из Основ питона
Задача №2 из 7 урока
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
"""


# Изначальный вариант

class Coat:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def coat(self):
        self.width = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на плащ, равняется: {self.width}.'


class Suit:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def suit(self):
        self.height = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм, равняется: {self.height}.'


class Textile(Coat, Suit):
    def __init__(self, width, height):
        super().__init__(width, height)

    @property
    def fabric_consumption(self):
        return str(f'Общий расход ткани, равняется: {round(self.width + self.height)}')


coat = Coat(5, 8)
suit = Suit(5, 8)
textile = Textile(5, 8)

print(coat.__str__())
print(suit.__str__())
print(textile.fabric_consumption)
print(f"Количество занимаемого места: {asizeof.asizeof(coat)}, классом {Coat.__name__}.")
print(f"Количество занимаемого места: {asizeof.asizeof(suit)}, классом {Suit.__name__}.")
print(f"Количество занимаемого места: {asizeof.asizeof(textile)}, классом {Textile.__name__}.")


# Оптимизированый вариант
class Coat_1:
    __slots__ = ["width", "height"]

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def coat(self):
        self.width = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на плащ, равняется: {self.width}.'


class Suit_1:
    __slots__ = ["width", "height"]

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def suit(self):
        self.height = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм, равняется: {self.height}.'


class Textile_1(Coat, Suit):
    __slots__ = ["width", "height"]

    def __init__(self, width, height):
        super().__init__(width, height)

    @property
    def fabric_consumption(self):
        return str(f'Общий расход ткани, равняется: {round(self.width + self.height)}')


coat_1 = Coat_1(5, 8)
suit_1 = Suit_1(5, 8)
textile_1 = Textile_1(5, 8)

print(coat_1.__str__())
print(suit_1.__str__())
print(textile_1.fabric_consumption)
print(f"Количество занимаемого места: {asizeof.asizeof(coat_1)}, классом {Coat_1.__name__}.")
print(f"Количество занимаемого места: {asizeof.asizeof(suit_1)}, классом {Suit_1.__name__}.")
print(f"Количество занимаемого места: {asizeof.asizeof(textile_1)}, классом {Textile_1.__name__}.")
"""
Количество занимаемого места: 328, классом Coat.
Количество занимаемого места: 328, классом Suit.
Количество занимаемого места: 328, классом Textile.
Количество занимаемого места: 112, классом Coat_1.
Количество занимаемого места: 112, классом Suit_1.
Количество занимаемого места: 232, классом Textile_1.
Выводы: исходя из данных отчета, видно, что испоьзование слотов,
уменьшило в 3 раза, занимаемое место.
"""