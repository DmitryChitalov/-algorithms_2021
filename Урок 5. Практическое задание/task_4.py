"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
import timeit

cities_in_france_by_region_1 = {
    'Paris': 'Île-de-France',
    'Marseille': "Provence-Alpes-Côte d'Azur",
    'Lyon': 'Auvergne-Rhône-Alpes',
    'Toulouse': 'Occitanie',
    'Nice': "Provence-Alpes-Côte d'Azur",
    'Nantes': 'Pays de la Loire',
    'Strasbourg': 'Grand Est',
    'Montpellier': 'Occitanie',
    'Bordeaux': 'Nouvelle-Aquitaine',
    'Lille': 'Hauts-de-France',
    'Rennes': 'Brittany',
    'Reims': 'Grand Est',
    'Le Havre': 'Normandy',
    'Saint-Étienne': 'Auvergne-Rhône-Alpes',
    'Toulon': "Provence-Alpes-Côte d'Azur",
    'Grenoble': 'Auvergne-Rhône-Alpes',
    'Dijon': 'Bourgogne-Franche-Comté',
    'Nîmes': 'Occitanie',
    'Angers': 'Pays de la Loire',
    'Villeurbanne': 'Auvergne-Rhône-Alpes',
    'Le Mans': 'Pays de la Loire',
    'Saint-Denis': 'Réunion',
    'Aix-en-Provence': "Provence-Alpes-Côte d'Azur",
    'Clermont-Ferrand': 'Auvergne-Rhône-Alpes',
    'Brest': 'Brittany',
    'Limoges': 'Nouvelle-Aquitaine',
    'Tours': 'Centre-Val de Loire',
    'Amiens': 'Hauts-de-France',
    'Perpignan': 'Occitanie',
    'Metz': 'Grand Est'
}

cities_in_france_by_region_2 = collections.OrderedDict([
    ('Paris', 'Île-de-France'),
    ('Marseille', "Provence-Alpes-Côte d'Azur"),
    ('Lyon', 'Auvergne-Rhône-Alpes'),
    ('Toulouse', 'Occitanie'),
    ('Nice', "Provence-Alpes-Côte d'Azur"),
    ('Nantes', 'Pays de la Loire'),
    ('Strasbourg', 'Grand Est'),
    ('Montpellier', 'Occitanie'),
    ('Bordeaux', 'Nouvelle-Aquitaine'),
    ('Lille', 'Hauts-de-France'),
    ('Rennes', 'Brittany'),
    ('Reims', 'Grand Est'),
    ('Le Havre', 'Normandy'),
    ('Saint-Étienne', 'Auvergne-Rhône-Alpes'),
    ('Toulon', "Provence-Alpes-Côte d'Azur"),
    ('Grenoble', 'Auvergne-Rhône-Alpes'),
    ('Dijon', 'Bourgogne-Franche-Comté'),
    ('Nîmes', 'Occitanie'),
    ('Angers', 'Pays de la Loire'),
    ('Villeurbanne','Auvergne-Rhône-Alpes'),
    ('Le Mans', 'Pays de la Loire'),
    ('Saint-Denis', 'Réunion'),
    ('Aix-en-Provence', "Provence-Alpes-Côte d'Azur"),
    ('Clermont-Ferrand', 'Auvergne-Rhône-Alpes'),
    ('Brest', 'Brittany'),
    ('Limoges', 'Nouvelle-Aquitaine'),
    ('Tours', 'Centre-Val de Loire'),
    ('Amiens', 'Hauts-de-France'),
    ('Perpignan', 'Occitanie'),
    ('Metz', 'Grand Est')
])

print(cities_in_france_by_region_1.values())
print(cities_in_france_by_region_2.values())

def cities_func_1_1():
    for cities in cities_in_france_by_region_1:
        print(cities)

def cities_func_2_1():
    for cities in cities_in_france_by_region_2:
        print(cities)

def cities_func_1_2():
    for key, value in cities_in_france_by_region_1.items():
        print(value)

def cities_func_2_2():
    for key, value in cities_in_france_by_region_2.items():
        print(value)

print('cities_func_1_1 (обычный):')
print(timeit.timeit("""def cities_func_1_1():
    for cities in cities_in_france_by_region_1:
        print(cities)""", number=20000))

print('cities_func_2_1 (OrderedDict):')
print(timeit.timeit("""def cities_func_2_1():
    for cities in cities_in_france_by_region_2:
        print(cities)""", number=20000))

print('cities_func_1_2 (обычный):')
print(timeit.timeit("""def cities_func_1_2():
    for key, value in cities_in_france_by_region_1.items():
        print(value)""", number=20000))

print('cities_func_2_2 (OrderedDict):')
print(timeit.timeit("""def cities_func_2_2():
    for key, value in cities_in_france_by_region_2.items():
        print(value)""", number=20000))

""""
ВЫВОД: я так понимаю, что OrderedDict нам нужен по двум причинам: во-первых, 
чтобы работать с легаси кодом, во-вторых, иногда где-то
OrderedDict быстрее работает, а где стандартный dict(). Судя по всему,
смысл в использовании OrderedDict в Python 3.6 и более поздних версиях в целом
 есть, но не всегда и не везде, а больше зависит от решаемой задачи.
"""