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

from memory_profiler import memory_usage
from timeit import default_timer
from pympler import asizeof
from sys import getsizeof
from recordclass import recordclass
from numpy import array


# Свой декоратор, используя ф-цию memory_usage из memory_profiler
# с одновременным замером времени (timeit.default_timer()), в т.ч. времени на замеры memory_usage
# (с ними результат нагляднее, а при необходимости, легко скорректировать внутри декоратора):
def memory_and_time(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        time_diff = default_timer() - start_time
        mem_diff = m2[0] - m1[0]
        res = func(*args)
        print(f"m1 = {m1} Mib, m2 = {m2} Mib\nВыполнение заняло {mem_diff} Mib, {time_diff} sec")
        return res

    return wrapper


# Задача 1. Вариант 1.
# Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего.
# [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
@memory_and_time
def smaller_big(lst):
    return [lst[i+1] for i in range(len(lst)-1) if lst[i] < lst[i+1]]


# Задача 1. Вариант 2.
@memory_and_time
def smaller_big2(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i+1]:
            yield lst[i + 1]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
v1 = smaller_big(src)
v2 = smaller_big2(src)
# for i in v2:
#     print(i)

# Задача 1. Выводы.
# m1 = [19.59375] Mib, m2 = [19.60546875] Mib
# Выполнение заняло 0.01171875 Mib, 0.21798489999999993 sec

# m1 = [19.61328125] Mib, m2 = [19.61328125] Mib
# Выполнение заняло 0.0 Mib, 0.21506179999999997 sec

# !!! Генераторы не возвращают любое количество элементов сразу вместе, как списки;
# они возвращают элементы один за другим. Соответственно, текущие затраты памяти
# сведены практически к нулю.


# Задача 2. Вариант 1.
# Переводчик с английского "1-10".
@memory_and_time
def num_translate_adv(word):
    dct = {"zero": "ноль",
           "one": "один",
           "two": "два",
           "three": "три",
           "four": "четыре",
           "five": "пять",
           "six": "шесть",
           "seven": "семь",
           "eight": "восемь",
           "nine": "девять",
           "ten": "десять"
           }
    w = word.lower()
    translate = dct.get(w)
    return f'Ответ на запрос: "{translate}"', \
           f'\nОбъём занимаемой объектом dict памяти: {getsizeof(dct)} байт(а)'


eng = input("Введите числительное от 0 до 10 прописью для перевода с английского: ")
print(*num_translate_adv(eng))


# Задача 2. Вариант 2.
@memory_and_time
def num_translate_adv(word):
    var = recordclass('var', ("zero", "one", "two", "three", "four", "five", "six",
                              "seven", "eight", "nine", "ten"))
    rec = var(zero="ноль",
              one="один",
              two="два",
              three="три",
              four="четыре",
              five="пять",
              six="шесть",
              seven="семь",
              eight="восемь",
              nine="девять",
              ten="десять")
    w = word.lower()
    translate = rec[w]
    return f'Ответ на запрос: "{translate}"', \
           f'\nОбъём занимаемой объектом recordclass памяти: {getsizeof(rec)} байт(а)'


eng = input("Введите числительное от 0 до 10 прописью для перевода с английского: ")
print(*num_translate_adv(eng))

# Задача 2. Выводы.
# Введите числительное от 0 до 10 прописью для перевода с английского: two
# m1 = [19.4375] Mib, m2 = [19.5078125] Mib
# Выполнение заняло 0.0703125 Mib, 0.2160434999999996 sec
# Ответ на запрос: "два"
# Объём занимаемой объектом dict памяти: 640 байт(а)

# Введите числительное от 0 до 10 прописью для перевода с английского: two
# m1 = [19.515625] Mib, m2 = [19.53515625] Mib
# Выполнение заняло 0.01953125 Mib, 0.21852540000000076 sec
# Ответ на запрос: "два"
# Объём занимаемой объектом recordclass памяти: 112 байт(а)

# !!! Переменные recordclass экономнее; в данном случае более чем в пять раз. Данный
# тип сохранил удобство использования словаря и не увеличивает потребление памяти.


# Задача 3. Вариант 1.
# Программа сложения и умножения двух шестнадцатиричных чисел (ООП).
class HexNumber:
    def __init__(self, a):
        self.lst = list(a)

    def __str__(self):
        return f'{self.lst}'

    def int_lst(self):
        d1 = []
        n = 0
        for d in reversed(list(map(lambda x: int(x, 16), self.lst))):
            d1.insert(0, d * 16 ** n)
            n += 1
        return d1

    def __add__(self, other):
        d1 = sum(self.int_lst())
        d2 = sum(other.int_lst())
        res = (hex(d1 + d2).upper())[2:]
        return HexNumber(res)

    def __mul__(self, other):
        d1 = sum(self.int_lst())
        d2 = sum(other.int_lst())
        res = (hex(d1 * d2).upper())[2:]
        return HexNumber(res)


HN_OBJ = HexNumber('A2')
print(HN_OBJ.__dict__)
print(f'Объём занимаемой списком атрибутов HexNumber памяти: {asizeof.asizeof(HN_OBJ)} байт(а)')


# Задача 3. Вариант 2.
class HexNumber2:
    __slots__ = ['lst']

    def __init__(self, a):
        self.lst = list(a)

    def __str__(self):
        return f'{self.lst}'

    def int_lst(self):
        d1 = []
        n = 0
        for d in reversed(list(map(lambda x: int(x, 16), self.lst))):
            d1.insert(0, d * 16 ** n)
            n += 1
        return d1

    def __add__(self, other):
        d1 = sum(self.int_lst())
        d2 = sum(other.int_lst())
        res = (hex(d1 + d2).upper())[2:]
        return HexNumber(res)

    def __mul__(self, other):
        d1 = sum(self.int_lst())
        d2 = sum(other.int_lst())
        res = (hex(d1 * d2).upper())[2:]
        return HexNumber(res)


HN_OBJ2 = HexNumber2('A2')
print(HN_OBJ2.__slots__)
print(f'Объём занимаемой списком атрибутов HexNumber2 памяти: {asizeof.asizeof(HN_OBJ2)} байт(а)')

# Задача 3. Выводы.
# {'lst': ['A', '2']}
# Объём занимаемой списком атрибутов HexNumber памяти: 392 байт(а)
# ['lst']
# Объём занимаемой списком атрибутов HexNumber2 памяти: 224 байт(а)

# !!! Использование слотов позволяет сохранить атрибуты в менее затратном по памяти контейнере,
# в данном случае – списке. Даже в примере с одним атрибутом, экономия почти в два раза!


# Задача 4. Вариант 1.
# Генератор нечётных чисел от 1 до 10000 (включительно), квадрат которых меньше 10000000 без использования
# ключевого слова yield. Полностью истощить генератор, сохранив результаты в список вида:
# ['next(gen1) 1', 'next(gen1) 3', 'next(gen1) 5', 'next(gen1) 7', 'next(gen1) 9', 'next(gen1) 11', 'next(gen1) 13',...]
@memory_and_time
def gen1():
    n = 10000
    lst = []
    gen1 = (i for i in range(1, n+1, 2) if i**2 < 10000000)
    for i in gen1:
        res = f"next(gen1) {i}"
        lst.append(res)
    return lst


# Задача 4. Вариант 2.
@memory_and_time
def gen2():
    n = 10000
    lst = []
    gen2 = (i for i in range(1, n+1, 2) if i**2 < 10000000)
    for i in gen2:
        res = f"next(gen2) {i}"
        lst.append(res)
    return array(lst)


print(f"gen1() -> lst: {asizeof.asizeof(gen1())} байт(а)")
print(f"gen2() -> array(lst): {asizeof.asizeof(gen2())} байт(а)")

# Задача 4. Выводы.
# m1 = [30.06640625] Mib, m2 = [30.1796875] Mib
# Выполнение заняло 0.11328125 Mib, 0.207523157999999 sec
# gen1() -> lst: 114184 байт(а)

# m1 = [30.37890625] Mib, m2 = [30.37890625] Mib
# Выполнение заняло 0.0 Mib, 0.20822104500000016 sec
# gen2() -> array(lst): 94984 байт(а)

# !!!Библиотека NumPy отлично оптимизирует большой объем данных и эффективно управляет ресурсами памяти.
# И замеры декоратором с memory_profiler.memory_usage, и замеры pympler.asizeof.asizeof() показывают
# снижение расхода ресурсов даже на относительно небольшом списке при использовании numpy.array().
