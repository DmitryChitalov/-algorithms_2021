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
      DataGoods("телефон", 20000, "RUB"),
      DataGoods("телевизор", 45000, "RUB"),
      DataGoods("тостер", 2000, "RUB")
   ])
print("СОЗДАЕМ ТОВАРЫ НА PYTHON:", time.time()-t)
# СОЗДАЕМ ТОВАРЫ НА PYTHON: 44.49887752532959

telephoneSum, televizorSum, tosterSum = 0, 0, 0
t = time.time()
for goods in shop.listGoods:
   if goods.name == "телефон":
      telephoneSum += goods.price
   elif goods.name == "телевизор":
      televizorSum += goods.price
   elif goods.name == "тостер":
      tosterSum += goods.price
print("ВРЕМЯ НА ПОДСЧЁТ СУММ PYTHON:", time.time() - t)
# ВРЕМЯ НА ПОДСЧЁТ СУММ PYTHON: 13.135360717773438

'''
Cython
'''

from cython_npm.cythoncompile import export
from cython_npm.cythoncompile import install
import time
import cython_code.cython_data as cython_data

cdef class CythonDataGoods:
   cdef str name
   cdef int price
   cdef str unit
   def __init__(self, str name, int price, str unit):
       self.name = name
       self.price = price
       self.unit = unit
cdef int c_testFunc():
    cdef CythonShopClass shop
    cdef CythonDataGoods goods
    cdef int i, t, telephoneSum, televizorSum, tosterSum
    size, i, telephoneSum, televizorSum, tosterSum = 0, 0, 0, 0, 0
    shop = CythonShopClass("MyShop")
    t = time.time()
    for i in range(200*100000):
       shop.listGoods.extend([
           CythonDataGoods("телефон", 20000, "RUB"),
           CythonDataGoods("телевизор", 45000, "RUB"),
           CythonDataGoods("тостер", 2000, "RUB")
       ])
    print("СОЗДАЕМ ТОВАРЫ НА CYTHON:", time.time()-t)
    t = time.time()
    for goods in shop.listGoods:
        if goods.name == "телефон":
            telephoneSum += goods.price
        elif goods.name == "телевизор":
            televizorSum += goods.price
        elif goods.name == "тостер":
            tosterSum += goods.price
    print("ВРЕМЯ НА ПОДСЧЁТ СУММ CYTHON:", time.time() - t)
    return 0
def my_def():
    data = c_testFunc()
    return data

export('cython_code/cython_data.pyx')


if __name__ == "__main__":
   a = cython_data.my_def()


'''
Вывод:

PYTHON:
СОЗДАЕМ ТОВАРЫ НА PYTHON: 44.49887752532959
ВРЕМЯ НА ПОДСЧЁТ СУММ PYTHON: 13.135360717773438

CYTHON:
СОЗДАЕМ ТОВАРЫ НА CYTHON: 4.082242012023926
ВРЕМЯ НА ПОДСЧЁТ СУММ CYTHON: 1.0513946056365967

cython значительно ускоряет работу кода, в связи с 
заранее определенными (пользователем) типами данных.

'''