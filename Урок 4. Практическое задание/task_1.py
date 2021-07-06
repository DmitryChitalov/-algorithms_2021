"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" -
list comprehension.
"""
from random import randint
from timeit import timeit
import dis

# создание исходного списка из 100 целых чисел
my_rand_int_list = [randint(0, 50) for i in range(100)]


def func_1(nums):
    """Original function"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """Improvement №1 - enumerate() is used here"""
    new_arr = []
    for i, val in enumerate(nums):
        if val % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_3(nums):
    """Improvement №2 - list comprehension is involved here"""
    new_arr = [i for i, val in enumerate(nums) if val % 2 == 0]
    return new_arr


def func_4(nums):
    """Improvement №3 - if v %2 == 0 replaced by if not v % 2"""
    new_arr = [i for i, val in enumerate(nums) if not val % 2]
    return new_arr


'''Для замеров каждой функции (и дальнейших действий в дополнение к домашнему заданию) я поместила
их в словарь. На моей машине хорошо видно, что каждая последующая - с меньшим временем
выполнения.
Анализ:
1. Улучшение 1 - использование enumerate(), которая добавляет счетчик к каждому элементу
итерируемого объекта, таким образом в коде функции не требуется отдельно обращаться
к элементу списка по индексу
2. Улучшение 2 - list comprehensions быстрее, чем цикл for.
3. Улучшение 3 - if not val % 2 лучше, чем if val % 2 == 0 потому, что val % 2 == 0
эквивалентно not (val % 2 != 0), то есть выполняются лишние действия отрицания.

'''

my_functions = dict(
    func_1="""
new_arr = []
for i in range(len(my_rand_int_list)):
    if my_rand_int_list[i] % 2 == 0:
        new_arr.append(i)""",
    func_2="""
new_arr = []
for i, val in enumerate(my_rand_int_list):
        if val % 2 == 0:
            new_arr.append(i)""",
    func_3='new_arr = [i for i, v in enumerate(my_rand_int_list) if v %2 == 0]',
    func_4='new_arr = [i for i, v in enumerate(my_rand_int_list) if not v % 2]',
)

for name, text in my_functions.items():
    print(name, timeit(stmt=text, number=1000, globals=globals()))


'''
Далее мне стало интересно разобраться, почему же на самом деле list comprehensions быстрее,
чем цикл for.
Я использовала модуль dis для того, чтобы получить доступ к байт-коду и сравнила отличия.
Мне кажется, lc быстрее for благодаря тому, что при использовании for выполняются загрузка
метода и его вызов:
38 LOAD_METHOD(append) и 42 CALL_METHOD для func_01 и
34 LOAD_METHOD(append) и 38 CALL_METHOD для func_02 соответственно.
А для lc такой необходимости нет.
'''

for name, text in my_functions.items():
    print(name)
    code = compile(text, '<string>', 'exec')
    dis.disassemble(code)

'''
Также я проверила if val % 2 == 0 и if not val % 2, у первого варианта ожидаемо
оказалось 2 лишних операции:
6 LOAD_CONST и 8 COMPARE_OP
Отсюда 4 вариант заданной функции быстрее, чем 3.
'''


def not_not(val):
    if val % 2 == 0:
        return True


def one_not(val):
    if not val % 2:
        return True


dis.dis(not_not)
dis.dis(one_not)
