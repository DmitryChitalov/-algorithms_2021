"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""
import sys


dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6 }

class Point:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f


dictionary_class = Point(1, 2, 3, 4, 5, 6)

print(sys.getsizeof(dictionary))
print(sys.getsizeof(dictionary_class.__dict__))
print(f'Словарь экземпляра класса занимает в {sys.getsizeof(dictionary) / sys.getsizeof(dictionary_class.__dict__)} '
      f'раза меньше места в оперативной памяти, чем обычный словарь.')
'''
A class instance dictionary takes up less memory space than a regular dictionary.
'''
'''
C:\Users\79115\AppData\Local\Programs\Python\Python39\python.exe "C:/Users/79115/Desktop/2 Урок Алгоритмы/Урок 2. Коды примеров/Algorithm6.2.py"
360
144
Словарь экземпляра класса занимает в 2.5 раза меньше места в оперативной памяти, чем обычный словарь.

Process finished with exit code 0

'''
