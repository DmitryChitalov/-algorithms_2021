"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""
import time

'''
Создание класса стандартным методом с использованием class
'''


class ShopClass:
   __slots__ = ("name", "listGoods")
   def __init__(self, name=""):
      self.name = name
      self.listGoods = []
@dataclass
class DataGoods:
   __slots__ = ("name", "price", "unit")
   name: str
   price: int
   unit: str
shop = ShopClass("MyShop")
t = time.time()
for _ in range(200*100000):
   shop.listGoods.extend([
      DataGoods("холодильник", 35500, "RUB"),
      DataGoods("духовой шкаф", 42800, "RUB"),
      DataGoods("стиральная машина", 38200, "RUB")
   ])
print("СОЗДАЕМ ТОВАРЫ НА PYTHON:", time.time()-t)
# СОЗДАЕМ ТОВАРЫ НА PYTHON: 44.49887752532959

fridgeSum, ovenSum, washing_machineSum = 0, 0, 0
t = time.time()
for goods in shop.listGoods:
   if goods.name == "холодильник":
      fridgeSum += goods.price
   elif goods.name == "духовой шкаф":
      ovenSum += goods.price
   elif goods.name == "стиральная машина":
      washing_machineSum += goods.price
print("время подсчета сумм PYTHON:", time.time() - t)
# время подсчета сумм PYTHON 15.536017717773438

