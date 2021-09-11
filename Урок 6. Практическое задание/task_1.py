"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

# ТЯЖЕЛО БЫЛО НАЙТИ ЗАДАЧИ "не модифицированные"


from random import choice
from sys import getsizeof
from timeit import timeit
from recordclass import recordclass

# Скрипт из основ Python'а


def get_jokes(n, flag=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []

    if flag:
        for idx in range(n):
            joke.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
    else:
        for idx in range(n):
            take_noun = choice(nouns)
            nouns.remove(take_noun)
            take_adverb = choice(adverbs)
            adverbs.remove(take_adverb)
            take_adjective = choice(adjectives)
            adjectives.remove(take_adjective)
            joke.append(f"{take_noun} {take_adverb} {take_adjective}")

    return joke


# score = int(input('Введите количество шуток: '))
score = 2

print(
    timeit(
        "get_jokes(score, False)",
        globals=globals()
        ), get_jokes(score, False))

print(getsizeof(get_jokes(score, False)))

# ПРОФИЛИРОВАНИЕ
# Здесь мы сделали профилирование только по времени - сделали list comprehensions,
# с памятью все так и остается ведь в функции мы возвращаем только joke
# (ТО ЧТО В #) Но если мы в функции не используем "лишние" переменные, а проводим методы со списками,
# то время работы программы будет больше и память не изменится :( хоть скрипт меньше...


def get_jokes(n, flag=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []

    if flag:
        joke = [idx for idx in range(n)]
    else:
        for idx in range(n):                # for idx in range(n):
            take_noun = choice(nouns)           # joke.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
            nouns.remove(take_noun)             # nouns.remove(joke[idx].split()[0])
            take_adverb = choice(adverbs)       # adverbs.remove(joke[idx].split()[1])
            adverbs.remove(take_adverb)         # adjectives.remove(joke[idx].split()[2])
            take_adjective = choice(adjectives)
            adjectives.remove(take_adjective)
            joke.append(f"{take_noun} {take_adverb} {take_adjective}")

    return joke


# score = int(input('Введите количество шуток: '))
score = 2

print(
    timeit(
        "get_jokes(score, False)",
        globals=globals()
        ), get_jokes(score, False))

print(getsizeof(get_jokes(score, False)))


# Скрипт из алгоритмов Python'а


def sum_elements(first_number, val_el, summ):
    if val_el == 0:
        return summ
    else:
        return sum_elements(first_number / (-2), val_el - 1, summ + first_number)


f_arg = 1
# s_arg = int(input('Введите количество элементов: '))
s_arg = 4
t_arg = 0

print(
    timeit(
        "sum_elements(f_arg, s_arg, t_arg)",
        globals=globals()
        ), sum_elements(f_arg, s_arg, t_arg))

print(getsizeof(sum_elements(1, s_arg, 0)))

# ПРОФИЛИРОВАНИЕ
# Здесь мы сделали профилирование только по времени - просто сделали цикл, он здесь будет смотреть выгоднее рекурсии,
# почти в 1.5 раза меньше(а чем больше val_el,тем больше разница), по памяти тут вроде все окей, без изменений.


def sum_elements(first_number, val_el, summ):
    for i in range(val_el):
        summ += first_number
        first_number = first_number / (-2)

    return summ


f_arg = 1
# s_arg = int(input('Введите количество элементов: '))
s_arg = 4
t_arg = 0

print(
    timeit(
        "sum_elements(f_arg, s_arg, t_arg)",
        globals=globals()
        ), sum_elements(f_arg, s_arg, t_arg))

print(getsizeof(sum_elements(1, s_arg, 0)))


# Скрипт из основ Python'а


def gen(massive):
    res = set()
    repeated_in_numbers = set()
    lst_ = []
    for name in massive:
        if name in repeated_in_numbers:
            continue
        if name in res:
            repeated_in_numbers.add(name)
            res.discard(name)
            continue
        res.add(name)

    for el in massive:
        if el in res:
            lst_.append(el)

    return lst_


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(
    timeit(
        "gen(src)",
        globals=globals()
        ), gen(src))

print(getsizeof(gen(src)))

# ПРОФИЛИРОВАНИЕ
# Здесь мы сделали профилирование по времени - сделали list comprehensions (хотя опять баг, что скрипт с
# list comprehensions работает медленне), следовательно и убрали лишнюю переменную lst_, что и по памяти
# должно быть меньше + воспользовались yield, ведь он как return, только вернет генератор + малозатратен по памяти.


def gen(massive):
    res = set()
    repeated_in_numbers = set()
    for name in massive:
        if name in repeated_in_numbers:
            continue
        if name in res:
            repeated_in_numbers.add(name)
            res.discard(name)
            continue
        res.add(name)

    yield [el for el in massive if el in res]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(
    timeit(
        "gen(src)",
        globals=globals()
        ), *gen(src))

print(getsizeof(gen(src)))

# Скрипт из основ Python'а


def game(player_name, enemy_name):

    player = {
        'name': player_name,
        'health': 100,
        'damage': 50,
        'armor': 1.2
    }

    enemy = {
        'name': enemy_name,
        'health': 70,
        'damage': 35,
        'armor': 1.2
    }

    def attack(person1, person2):
        person1['health'] = person1['health'] - defence(person1, person2)
        return person1['health']

    def defence(personwithdefence1, personwithdefence2):
        raznicadefence = (personwithdefence2['damage'] // personwithdefence1['armor'])
        return raznicadefence

    attack(player, enemy)
    return player, getsizeof(player), getsizeof(enemy)


# name_player = input("Vvedite Imya Igroka: ")
name_player = 'Egor'
# name_enemy = input("Vvedite Imya Vraga: ")
name_enemy = 'Makar'

print(
    timeit(
        "game(name_player, name_enemy)",
        globals=globals(),
        number=100
        ), game(name_player, name_enemy))


# ПРОФИЛИРОВАНИЕ
# Здесь мы сделали профилирование по памяти - воспользовшись модулем recordclass словарем recordclass,
# он лучше смотрится по памяти, но к сожалению по времени уступает обычному словарю.

def game(player_name, enemy_name):

    dic_1 = recordclass('player', ('name', 'health', 'damage', 'armor'))

    dic_player = dic_1(name=player_name, health=100, damage=50, armor=1.2)

    dic_2 = recordclass('enemy', ('name', 'health', 'damage', 'armor'))

    dic_enemy = dic_2(name=enemy_name, health=70, damage=35, armor=1.3)

    def attack(person1, person2):
        person1.health = person1.health - defence(person1.armor, person2.damage)
        return person1

    def defence(personwithdefence1, personwithdefence2):
        raznicadefence = (personwithdefence2 // personwithdefence1)
        return raznicadefence

    attack(dic_player, dic_enemy)
    return dic_player, getsizeof(dic_player), getsizeof(dic_enemy)


# name_player = input("Vvedite Imya Igroka: ")
name_player = 'Egor'
# name_enemy = input("Vvedite Imya Vraga: ")
name_enemy = 'Makar'

print(
    timeit(
        "game(name_player, name_enemy)",
        globals=globals(),
        number=10
        ), game(name_player, name_enemy))