"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""
import collections
from timeit import timeit
from random import randint

list_of_cities_in_france = [
    'Paris', 'Marseille' 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg',
    'Montpellier', 'Bordeaux', 'Lille', 'Rennes', 'Reims', 'Le Havre',
    'Saint-Étienne', 'Toulon', 'Grenoble', 'Dijon', 'Nîmes', 'Angers',
    'Villeurbanne', 'Le Mans', 'Saint-Denis', 'Aix-en-Provence',
    'Clermont-Ferrand', 'Brest', 'Limoges', 'Tours', 'Amiens',
    'Perpignan', 'Metz']

deque_of_cities_in_france = collections.deque([
    'Paris', 'Marseille' 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg',
    'Montpellier', 'Bordeaux', 'Lille', 'Rennes', 'Reims', 'Le Havre',
    'Saint-Étienne', 'Toulon', 'Grenoble', 'Dijon', 'Nîmes', 'Angers',
    'Villeurbanne', 'Le Mans', 'Saint-Denis', 'Aix-en-Provence',
    'Clermont-Ferrand', 'Brest', 'Limoges', 'Tours', 'Amiens',
    'Perpignan', 'Metz'])

# ЗАДАЧА 1

counter = 50

def filling_list(counter):
    for i in range(counter):
        list_of_cities_in_france.append(i)
        return list_of_cities_in_france

def filling_deque(counter):
    for i in range(counter):
        deque_of_cities_in_france.append(i)
    return deque_of_cities_in_france

print('Заполнение списка:')
print(timeit('filling_list(counter)', globals=globals(), number=20000))

print('Заполнение дека:')
print(timeit('filling_deque(counter)', globals=globals(), number=20000))

# ЗАДАЧА 2

#def appending_to_left_to_deque(counter):
#    for i in range(counter):
#        deque_of_cities_in_france.appendleft(i)
#    return deque_of_cities_in_france

#def popping_from_left_to_deque(counter):
#    while deque_of_cities_in_france:
#        deque_of_cities_in_france.popleft()
#        if len(deque_of_cities_in_france) % 100 == 0
#             print(len(deque_of_cities_in_france))