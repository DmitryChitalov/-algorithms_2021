"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

# ВТОРОЙ СКРИПТ

'''
Дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
Или эквивалентно записи:
class Class1(Class2, Class3 ... ClassK):
    pass

Формат входных данных
В первой строке входных данных содержится целое число n - число классов.
В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.
В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Вам необходимо отвечать на запросы, является ли один класс предком другого класса
Sample Input:
4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:
Yes
Yes
Yes
'''

import memory_profiler
from recordclass import recordclass
from pympler import asizeof
# import time
# from numpy import array  # !!!
# from collections import namedtuple

import sys


class NameClass:
    def __init__(self):
        self.name_class = {}

    def add(self, child, parent):
        if child in self.name_class:
            print('Повторное определение класса!!!')
            return
        self.name_class[child] = parent

    def is_parent(self, child, parent):
        parents_list = self.__find_parents([child])
        parents_list.append(child)
        if parent in parents_list and child in self.name_class:
            return True
        else:
            return False

    def __find_parents(self, child):
        if child == []:
            return []
        parent_list = []
        for el in child:
            if el in self.name_class:
                parent_list.extend(self.name_class[el])
                for x in self.name_class[el]:
                    parent_list.extend(self.__find_parents([x]))
        return parent_list

class NameClassOpt:
    __slots__ = ('name_class', 'cls_record')
    def __init__(self):
        self.name_class = []
        self.cls_record = recordclass('cls', ('child', 'parent'))

    def add(self, child, parent):
        if child in self.name_class:
            print('Повторное определение класса!!!')
            return
        self.name_class.append(self.cls_record(child, parent))

    def is_parent(self, child, parent):
        parents_list = self.__find_parents([child])
        parents_list.append(child)
        if parent in parents_list and child in [x.child for x in self.name_class]:
            return True
        else:
            return False

    def __find_parents(self, child):
        if child == []:
            return []
        parent_list = []
        for el_child in child:
            for el in self.name_class:
                if el_child == el.child:
                    parent_list.extend(el.parent)
                    for x in el.parent:
                        parent_list.extend(self.__find_parents([x]))
        return parent_list


sys.stdin = open("input_1_2.txt", "r")

my_class1 = NameClass()
my_class2 = NameClassOpt()

print(f'Незаполненный класс занимает ({asizeof.asizeof(my_class1)}) и содержит: \n', my_class1.__dict__)
print(f'Незаполненный класс после оптимизации занимает ({asizeof.asizeof(my_class2)}) и содержит: \n', my_class2.__slots__)

n = int(input())  # число запросов
for i in range(n):
    my_list = input().split()
    child = my_list[0]
    if len(my_list) > 1 and my_list[1] == ':':
        parent = my_list[2:]
    else:
        parent = []
    my_class1.add(child, parent)
    my_class2.add(child, parent)
# print(my_class1.name_class)

print(f'После заполнения, класс занимает ({asizeof.asizeof(my_class1.name_class)}) и содержит:')
for el in my_class1.name_class:
    print(el, my_class1.name_class[el])
print(f'После заполнения, оптимизированный класс занимает ({asizeof.asizeof(my_class2.name_class)}) и содержит:')
for el in my_class2.name_class:
    print(el.child, el.parent)

# exit()
n = int(input())  # число запросов
for i in range(n):
    parent, child = input().split()
    answer1 = ('Yes' if my_class1.is_parent(child, parent) else 'No')
    answer2 = ('Yes' if my_class2.is_parent(child, parent) else 'No')
    print(f'{child} является предком: {answer1} (оптимизированный метод: {answer2})')

'''
Для оптимизации по памяти имеющегося варианта решения задачи, не очень эффективен метод перевода хранения методов
класса из словаря в слот __slots__ = ('name_class', 'cls_record'). Это нам сократит первоначальный объем с 280 до 104.
Но, вот замена метода хранения словаря "Эмуляции наследования классов" на recordclass более существенно повлиял на
требования по памяти с 3208 до 1552. Естественно, пришлось подкорректировать методы работы с классом 
(add, is_parent и __find_parents). Результаты работы оптимизированного кода проверены - все Ок.

Аналитика:
Незаполненный класс занимает (280) и содержит: 
 {'name_class': {}}
Незаполненный класс после оптимизации занимает (104) и содержит: 
 ('name_class', 'cls_record')
После заполнения, класс занимает (3208):
После заполнения, оптимизированный класс занимает (1552) и содержит:
classA ['classB', 'classC', 'classD', 'classG', 'classH']
classB ['classC', 'classE', 'classG', 'classH', 'classK', 'classL']
classC ['classE', 'classD', 'classH', 'classK', 'classL']
classE ['classD', 'classF', 'classK', 'classL']
classD ['classG', 'classH']
classF ['classK']
classG ['classF']
classH ['classL']
classK ['classH', 'classL']
classL []

'''

