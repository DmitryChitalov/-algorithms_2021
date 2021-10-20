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

from timeit import default_timer
from sys import getsizeof
from random import randint
from memory_profiler import memory_usage
import numpy


N = 10**7


def my_decor(func):
    is_evaluating = False

    def wrap(*argv):
        nonlocal is_evaluating
        if is_evaluating:
            return func(*argv)
        else:
            t_start = default_timer()
            m_start = memory_usage()
            is_evaluating = True
            try:
                res = func(*argv)
            finally:
                is_evaluating = False

            print(f'Время выполения : {default_timer() - t_start}, '
                  f'затраченно памяти: {memory_usage()[0] - m_start[0]}\n')
            return res
    return wrap


'''
Пример 1. Для примера взял функцию из урока 4, задание 1 курса Алгоритмы (чтоб не раздувать скрипт возьмем только
функцию с LC).
'''
print('Пример 1\n')


# Функция из примера:
@my_decor
def func_2(nums):
    return [i for i in nums if nums[i] % 2 == 0]


#
@my_decor
def new_func(nums):
    return numpy.array([i for i in nums if nums[i] % 2 == 0])


my_list = [i for i in range(N)]
func_2(my_list)
new_func(my_list)

'''
В данном случае мы заменили возвращаемый объект, класса list, на объект класса numpy. Это дало нам выйгрыш в памяти
примерно в 2-3 раза, но проигрываем по скорости, примерно на 20-30%.
'''


'''
Пример 2. Возьмем в качестве примера класс из урока 1, задание 5. Не будем брать все методы класса, а оставим только 
инициализацию класса и метод для заполнения элементами, но для нагладности изменим его. Изменим метод, чтоб он принимал
в качестве аргумента не число а генератор чисел (или массив чисел).
'''
print('Пример 2\n')


class Plate:
    def __init__(self):
        self.elem = [[]]

    @my_decor
    def push_in(self, el):
        for _ in el:
            if len(self.elem[-1]) >= 10:
                self.elem.append([_])
            else:
                self.elem[-1].append(_)


class NewPlate:
    def __init__(self):
        self.elem = numpy.array([[]])

    @my_decor
    def push_in(self, el):
        for _ in el:
            if len(self.elem[-1]) >= 10:
                numpy.append(self.elem, _)
            else:
                numpy.append(self.elem[-1], _)


# Создадим объект класса.
obj_1 = Plate()
obj_2 = NewPlate()

# Заплним стек цифрами
obj_1.push_in((i for i in range(N)))
obj_2.push_in((i for i in range(N)))
print(f'Размер массива элементов: {getsizeof(obj_1.elem)}, '
      f'Размера объекта NumPy с такими же элементами: {getsizeof(obj_2.elem)}')

'''
В новом классе мы храним элементы не в списке а в массиве numpy. Это дает при заполнении массива выйгрыш в памяти 
примерно в 10000 раз, но проигрываем по времени примерно в 15 раз. Так же при вызове функции getsizeof ма видим, 
что объект numpy занимает в разы меньше памяти (в моем случае: list = 8448728, NumPy = 120)
'''

'''
Пример 3. Возьмем пример из урока 2 задания 3.
'''
print('Пример 3\n')


@my_decor
def flip_digit(dig):
    if dig < 10:
        return str(dig)
    else:
        return f'{dig % 10}{flip_digit(dig // 10)}'


@my_decor
def new_flip(dig):
    return str(dig)[::-1]


num = randint(10**440, 10**450)
flip_digit(num)
new_flip(num)


'''
За счет того что в функции выполнялись минимальное количество вычислений, мы не видим большого выйгрыша в скорости, 
но видим выйгрыш по памяти. В данном примере мы только отказались от рекурсии и воспользовались, встроенной возможностью
Python, срезом.
'''
