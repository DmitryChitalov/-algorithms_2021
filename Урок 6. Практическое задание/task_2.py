"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""

from dataclasses import dataclass
from memory_profiler import profile

class ShopClass:
    def __init__(self, name=""):
        self.name = name
        self.listGoods = []

@dataclass
class DataGoods:
    name:str
    price:int
    unit:str


@profile
def my_func_1():
    """Профилирование функции без оптимизации

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    23     13.9 MiB     13.9 MiB           1   @profile
    24                                         def my_func_1():
    25     13.9 MiB      0.0 MiB           1       shop = ShopClass("MyShop")
    26     24.6 MiB      0.0 MiB       20001       for _ in range(20000):
    27     24.6 MiB      2.7 MiB       40000           shop.listGoods.extend([
    28     24.6 MiB      3.2 MiB       20000               DataGoods("телефон", 20000, "RUB"),
    29     24.6 MiB      0.0 MiB       20000               DataGoods("телевизор", 45000, "RUB"),
    30     24.6 MiB      4.8 MiB       20000               DataGoods("тостер", 2000, "RUB")
    31                                                 ])
    """

    shop = ShopClass("MyShop")
    for _ in range(20000):
        shop.listGoods.extend([
            DataGoods("телефон", 20000, "RUB"),
            DataGoods("телевизор", 45000, "RUB"),
            DataGoods("тостер", 2000, "RUB")
        ])

@profile
def my_func_2():
    """Профилирование функции с оптимизацией
    (использование лямбда функции и спискового включения)

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    33     19.0 MiB     19.0 MiB           1   @profile
    34                                         def my_func_2():
    35     19.0 MiB      0.0 MiB           1       shop = ShopClass("MyShop")
    36     19.3 MiB      0.0 MiB       80001       getGoods = lambda index: {0: ("телефон", 20000, "RUB"),
    37     19.3 MiB      0.0 MiB       20000                             1: ("телевизор", 45000, "RUB"),
    38     19.3 MiB      0.0 MiB       40000                             2:("тостер", 2000, "RUB")}.get(index)
    39     19.3 MiB      0.3 MiB       20003       shop.listGoods = [DataGoods(*getGoods(i%3)) for i in range(20000)]
    """

    shop = ShopClass("MyShop")
    getGoods = lambda index: {0: ("телефон", 20000, "RUB"),
                          1: ("телевизор", 45000, "RUB"),
                          2:("тостер", 2000, "RUB")}.get(index)
    shop.listGoods = [DataGoods(*getGoods(i%3)) for i in range(20000)]

if __name__ == '__main__':
    my_func_1()
    my_func_2()


"""
Конечно, использование сторонних надстроек или модулей для ускорения - это хорошо,
но также стоит оптимизировать свои алгоритмы.
Например, ускорим часть кода, где идет добавление новых товаров в список магазина.
Для этого напишем лямбда функцию, которая будет возвращать список параметров,
которые нужны для нового товара. Также будем пользоваться списковым включением.
Списковые включения в python - очень удобная вещь, они позволяют не только ускорить наш код,
но и оптимизировать его по используемой памяти.
"""

