"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
import timeit
my = [1,2,3,4,5,6,7]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr



print('1 -- ', timeit.timeit('func_1(my)', 'from __main__ import func_1, my', number=1000))

def func_2(my):
    total = [i for j, i in enumerate(my) if not j % 2]
print('2 -- ', timeit.timeit('func_2(my)', 'from __main__ import func_2, my', number=1000))

def func_3(my):
   my[::2]
print('3 -- ', timeit.timeit('func_3(my)', 'from __main__ import func_3, my', number=1000))

def func_4(my):
    for i in range(0, len(my), 2):
        True
        

print('4 -- ', timeit.timeit('func_4(my)', 'from __main__ import func_4, my', number=1000))
func_2(my)


#4 вариант быстрее исходного варианта(№1) т.к. в первом варинте перебираем элементы и потом проверяем деление на остаток,
#в 4 варианте, мы просто перебираем элементы через один, т.е. перобор элементов в два раза меньше,
#в третьем варианте мы так же берем каждый второй элемент, не перебирая все, во втором варианте мы перебираем
#и проверяем на четность индекс, но это вариант быстрее исходного т.к. enumerate за нас уже перебирает индексы
#1 --  0.0010628000000000026
#2 --  0.0008226000000000067
#3 --  0.00017019999999999536
#4 --  0.0003171000000000007