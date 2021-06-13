"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

#Сравнение времени заполнения словарей
simple_dict = {}
order_dict = OrderedDict()

def dict_fill(dict):
    dict = {i: i for i in range(10000)}
    return dict

time_1 = timeit("dict_fill(simple_dict)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_1}')

time_2 = timeit("dict_fill(order_dict)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_2}')

print(f'Относительная разница во времени составляет: {(time_1-time_2)/time_1*100} %')

#Время замера составило: 8.961
#Время замера составило: 5.8275
#Относительная разница во времени составляет: 34.97 %

#Получение пары ключ-значение
def dict_item(dict):
    for el in dict:
        dict.item(el)

time_5 = timeit("dict_item(simple_dict)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_5}')

time_6 = timeit("dict_item(order_dict)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_6}')

print(f'Относительная разница во времени составляет: {(time_5-time_6)/time_5*100} %')


#Время замера составило: 0.0009285000000005539
#Время замера составило: 0.0010907000000006661
#Относительная разница во времени составляет: -17.469036079700107 %

#Изменение значений словаря
def dict_update(dict):
    for el in dict:
        dict.update(el=1)

time_7 = timeit("dict_update(simple_dict)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_7}')

time_8 = timeit("dict_update(order_dict)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_8}')

print(f'Относительная разница во времени составляет: {(time_7-time_8)/time_7*100} %')

#Время замера составило: 0.0009430999999988643
#Время замера составило: 0.0011089999999995825
#Относительная разница во времени составляет: -17.590923550092043 %

#Удаление элемента
def dict_pop(dict):
    for el in dict:
        dict.popitem(el)


time_3 = timeit("dict_pop(simple_dict)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_3}')

time_4 = timeit("dict_pop(order_dict)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_4}')

print(f'Относительная разница во времени составляет: {(time_3-time_4)/time_3*100} %')


#Время замера составило: 0.0009464000000001249
#Время замера составило: 0.0011776999999995041
#Относительная разница во времени составляет: -24.43998309376043 %

#Фишки OrderedDict
#Применение метода move_to_end:
order_dict_0 = OrderedDict(a=1, b=2, c=3)
order_dict_0.move_to_end("a")
#Применение метода move_to_end, перемещение в начало:
order_dict_1 = OrderedDict(a=1, b=2, c=3)
order_dict_1.move_to_end("a", False)

#Удаление элементов с применением popitem() (удаление от начала):
order_dict_2 = OrderedDict(a=1, b=2, c=3)
order_dict_2.popitem(last=False)

#Сравнение словарей
order_dict_4 = OrderedDict(a=1, b=2, c=3, d=4)
order_dict_5 = OrderedDict(b=2, a=1, c=3, d=4)
order_dict_6 = OrderedDict(a=1, b=2, c=3, d=4)
print(order_dict_4 == order_dict_5)
#False
print(order_dict_4 == order_dict_6)
#True

dict_0 = dict(a=1, b=2, c=3, d=4)
dict_1 = dict(b=2, a=1, c=3, d=4)
dict_2 = dict(a=1, b=2, c=3, d=4)
print(dict_0 == dict_1)
#True
print(dict_0 == dict_2)
#True


#Выводы:
#Основные характеристики  отличные OrderedDict от обычного словаря:
#1. Возможность перестановки или переупорядочивания элементов с помощью методов move_to_end(), расширенного варианта
#popitem(), наличие аттрибута __dict__, который позволяет добавлять динамически настраиваемые аттрибуты экземпляра.
#2. Тестирование равенства словарей: если код сравнивает словари на предмет равенства и порядок элементов важен,
#то OrderedDict предпочтительнее использовать.
#3. Четкое обозначение программистом важности порядка расположения элементов в словаре.
#4. OrderedDict использует больше памяти и медленее выполняется (основные операции примерно на 20%). Единственное, что
# выполнялось быстрее - заполнение словаря. Так что если данные нужно просто хранить и изредка шевелить - использовать
# OrderedDict можно.

# Решение о применении обычного словаря или OrderedDict должно приниматься программистом в каждом отдельном случае
#в зависимости от исходных данных.