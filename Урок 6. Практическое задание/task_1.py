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
from memory_profiler import memory_usage
from timeit import default_timer


def my_decor(func):
    def check_optimize(*args):
        t1 = default_timer()
        m1 = memory_usage()
        result = func(*args)
        m2 = memory_usage()
        t2 = default_timer()
        mem_res = m2[0] - m1[0]
        time_res = t2 - t1
        print(f'Память: {mem_res},\nВремя: {time_res}')
    return check_optimize


# 1

@my_decor
def get_nums_1(end_num):
    res_list = [i for i in range(end_num + 1) if i % 20 == 0 or i % 21 == 0]
    return res_list


@my_decor
def get_nums_2(end_num):
    num_list = list(range(end_num + 1))
    for i in num_list:
        if i % 21 == 0 or i % 20 == 0:
            yield i


get_nums_1(10000000)
get_nums_2(10000000)

'''
Память: 18.609375,
Время: 1.8953721000000001
Память: 0.0,
Время: 0.21397639999999996

Как видим, генератор занимает настолько мало памяти, что замеры выдают результат 0,
в то время как список занимает достаточно места (относительно 0), так что, если нам
необходимо получить этот результат только один раз без дальнейшего использования,
то генератор - наш выбор. При этом по времени эти скрипты выполняются одинаково
'''


# 2

@my_decor
def check_recur(check_num):
    def revers_number(numb):
        rest_numb, numeral = divmod(numb, 10)
        if rest_numb == 0:
            return str(numeral)
        else:
            return str(numeral) + str(revers_number(rest_numb))
    return revers_number(check_num)


@my_decor
def revers_num(numb):
    return str(numb)[::-1]


check_recur(12321432543986842591849312843537664567567563213213125432534557342423634453)
revers_num(12321432543986842591849312843537664567567563213213125432534557342423634453)

'''
Память: 0.015625,
Время: 0.21917980000000004,
Результат: 35443632424375543523452131231236576576546673534821394819524868934523412321
Память: 0.0,
Время: 0.22256410000000015,
Результат: 35443632424375543523452131231236576576546673534821394819524868934523412321

Здесь же видим, что, не смотря на рекурсию, занимает она немного места, раз, по сути
работаем мы со строкой, которые итак не затратны по памяти, но, так или иначе, рекурсия
проигрывает второму способу, пусть и незначительно
'''


# 3

class Worker1:

    def __init__(self, name, surname, city, age, position, income):
        self.name = name
        self.surname = surname
        self.city = city
        self.age = age
        self.position = position
        self.income = income

    def get_full_info(self):
        print(f"Worker's name: {self.name} {self.surname} \nWorkers position: {self.position}")

    def get_total_income(self):
        return {sum(self.income.values())}


def get_info_1(obj):
    return obj.get_total_income()


class Worker2:
    __slots__ = ['name', 'surname', 'city', 'age', 'position', 'income']

    def __init__(self, name, surname, city, age, position, income):
        self.name = name
        self.surname = surname
        self.city = city
        self.age = age
        self.position = position
        self.income = income

    def get_full_info(self):
        print(f"Worker's name: {self.name} {self.surname} \nWorkers position: {self.position}")

    def get_total_income(self):
        return sum(self.income.values())


def get_info_2(obj):
    return obj.get_total_income()


obj_1 = Worker1('Jack', 'Smith', 'Designer', 'New York', 28, {'wage': 150000, 'premium': 40000})
obj_2 = Worker2('Jack', 'Smith', 'Designer', 'New York', 28, {'wage': 150000, 'premium': 40000})

get_info_1(obj_1)
get_info_2(obj_2)

'''
Память: 0.0078125,
Время: 0.2182723000000002
Память: 0.0,
Время: 0.2170046000000001

Здесь мы можем увидеть, что действительно слоты занимают меньше памяти, пусть и разница
со словарем несущественна. Но, раз словарь уже занимает какое-то количество памяти при
таком небольшом количестве данных, мы можем сказать, что дальше будет больше и экономия
памяти за счет слотов будет существеннее.
'''