from dataclasses import dataclass
from memory_profiler import profile

"""Первый вариант. 2 класса и 1 функция. Создание магазина, его характеристика и заполнение."""
class GroceryStores1:
    def __init__(self, name1=""):
        self.name1 = name1
        self.goods1 = []

@dataclass
class GroceryGoods1:
    name1: str
    weight1: int
    price1: int
    currency1: str

@profile
def f1():
    store1 = GroceryStores1("Vegetables&Fruits")
    for _ in range(20000):
        store1.goods1.extend([
            GroceryGoods1("сливы", 0.300, 75, "RUB"),
            GroceryGoods1("картошка", 2.780, 97, "RUB"),
            GroceryGoods1("яблоки", 0.550, 130, "RUB")
        ])







"""Второй вариант. 2 класса и 1 функция. Создание магазина, его характеристика и заполнение. Использование слотов"""
class GroceryStores2:
    __slots__ = ("name2", "goods2")
    def __init__(self, name2=""):
        self.name2 = name2
        self.goods2 = []

@dataclass
class GroceryGoods2:
    __slots__ = ("name2", "weight2", "price2", "currency2")
    name2: str
    weight2: int
    price2: int
    currency2: str

@profile
def f2():
    store2 = GroceryStores2("Vegetables&Fruits")
    for _ in range(2000):
        store2.goods2.extend([
            GroceryGoods2("лук", 0.450, 25, "RUB"),
            GroceryGoods2("персики", 1.100, 210, "RUB"),
            GroceryGoods2("кабачки", 0.200, 45, "RUB")
        ])


if __name__ == '__main__':
    f1()
    f2()


"""Профилирование первого варианта:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     19.8 MiB     19.8 MiB           1   @profile
    18                                         def f1():
    19     19.8 MiB      0.0 MiB           1       store1 = GroceryStores1("Vegetables&Fruits")
    20     30.1 MiB      0.0 MiB       20001       for _ in range(20000):
    21     30.1 MiB      1.0 MiB       40000           store1.goods1.extend([
    22     30.1 MiB      4.7 MiB       20000               GroceryGoods1("сливы", 0.300, 75, "RUB"),
    23     30.1 MiB      2.6 MiB       20000               GroceryGoods1("картошка", 2.780, 97, "RUB"),
    24     30.1 MiB      1.9 MiB       20000               GroceryGoods1("яблоки", 0.550, 130, "RUB")
    25                                                 ])



Профилирование второго варианта: 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    48     20.5 MiB     20.5 MiB           1   @profile
    49                                         def f2():
    50     20.5 MiB      0.0 MiB           1       store2 = GroceryStores2("Vegetables&Fruits")
    51     20.6 MiB      0.0 MiB        2001       for _ in range(2000):
    52     20.6 MiB      0.1 MiB        4000           store2.goods2.extend([
    53     20.6 MiB      0.0 MiB        2000               GroceryGoods2("лук", 0.450, 25, "RUB"),
    54     20.6 MiB      0.0 MiB        2000               GroceryGoods2("персики", 1.100, 210, "RUB"),
    55     20.6 MiB      0.0 MiB        2000               GroceryGoods2("кабачки", 0.200, 45, "RUB")
    56                                                 ])



То есть благодаря использованию слотов получилось значительно уменьшить размер памяти, ктторый тратится для данных программ. 
Получается в первом варианте создавался словарь __dict__ внутри класса для того чтобы пользователю можно было добавлять,
менять и удалять элементы. Но мы заранее знаем какие атрибуты должны быть. И поэтому во втором варианте мы используем 
метод __slots__. Это приводит к тому, что для новых классов не будет создаваться словарь со всеми 
атрибутами и хранимым в них данными.
И в итоге можно заметить, что данный метод действительно помог уменьшить объем занимаемой памяти.
"""