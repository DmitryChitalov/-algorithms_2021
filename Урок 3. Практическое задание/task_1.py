"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

import time
import random as rnd

#заполнение списка, словаря
def dict_start(n):
    dict_trash = {}
    for el in range(n):
        dict_trash[el] = int(rnd.random() * 10000)
    return dict_trash


def list_start(n):
    list_trash = []
    for el in range(n):
        #list_trash.append(el)
        list_trash.append(int(rnd.random() * 100000))
    return list_trash



start_timer1 = time.time()
d_2 = dict_start(1000000)
end_timer1 = time.time()
print(f' timer for dict: {end_timer1 - start_timer1}\n')

start_timer2 = time.time()
l_2 = list_start(1000000)
end_timer2 = time.time()
print(f' timer for list: {end_timer2 - start_timer2}')

#----------------------------------------------------------------2ая часть

def dict_ope2(dict_2):
    for i in range(len(dict_2)):
        if dict_2[i] == 10000:
            return f'{dict_2[i]}'

def list_ope2(lst_2):
    for i in range(len(lst_2)):
        if lst_2[i] == 10000:
            return f'{lst_2[i]}'

start_timer4 = time.time()
dict_ope2(d_2)
end_timer4 = time.time()
print(f' timer for dict: {end_timer4 - start_timer4}\n')

start_timer3 = time.time()
list_ope2(l_2)
end_timer3 = time.time()
print(f' timer for list: {end_timer3 - start_timer3}')


'''
1ый блок замеры - заполнение списка
 timer for dict: 0.3390214443206787
 timer for list: 0.2700183391571045
2ой блок замеры - поиск элемента:
 timer for dict: 0.08400726318359375
 timer for list: 0.006000041961669922
Вывод для обоих блоков: 
Из указанных данных мы видим что операции связанные со списками выполняются быстрее за счет того что происходит 
хэширование.
'''