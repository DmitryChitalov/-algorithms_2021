"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
import cProfile
from collections import OrderedDict


def dict_input(number):
    my_dict = {}
    for i in number:
        my_dict[i] = i


def ordrdict_input(number):
    my_dict = OrderedDict(number)


def dict_output(dictt):
    for i in dictt.items():
        a = i[0]
        b = i[1]


def ordrdict_output(dictt):
    for i in dictt.items():
        a = i[0]
        b = i[1]


def main():
    my_dict = {}
    nums = [i for i in range(1500000)]
    for i in nums:
        my_dict[i] = i
    dict_input(nums)
    ordrdict_input(my_dict)
    dict_output(my_dict)
    ordrdict_output(my_dict)

cProfile.run('main()')

'''
C:\Users\79115\AppData\Local\Programs\Python\Python39\python.exe "C:/Users/79115/Desktop/2 Урок Алгоритмы/Урок 2. Коды примеров/Algorithm5.4.py"
         11 function calls in 1.312 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.029    0.029    1.312    1.312 <string>:1(<module>)
        1    0.851    0.851    0.851    0.851 Algorithm5.4.py:11(ordrdict_input)
        1    0.068    0.068    0.068    0.068 Algorithm5.4.py:15(dict_output)
        1    0.065    0.065    0.065    0.065 Algorithm5.4.py:21(ordrdict_output)
        1    0.147    0.147    1.282    1.282 Algorithm5.4.py:27(main)
        1    0.064    0.064    0.064    0.064 Algorithm5.4.py:29(<listcomp>)
        1    0.088    0.088    0.088    0.088 Algorithm5.4.py:5(dict_input)
        1    0.000    0.000    1.312    1.312 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}



Process finished with exit code 0

The results of measurements showed that the difference in the work of the dictionary and OrderedDict 
is approximately the same.Using OrderedDict has no advantage in newer Python versions.

Результаты замеров показали, что работа словаря и OrderedDict примерно одинакова.
Использование OrderedDict не имеет преимуществ в новых версиях Python.


'''






