"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    
    left == right
    left.clear()
    right.clear()


"""


import random
from statistics import median
from timeit import timeit

m = int(input('Введите натуральное число - \n'))
lst_rand = [random.randint(0, 100) for i in range(2 * m + 1)]
print(lst_rand, '\n')
a = lst_rand.copy()
b = lst_rand.copy()


# сортировка по Шеллу
def shell(lst_rand):
    lst_rand_sup = []
    inc = len(lst_rand) // 2
    while inc:
        for i, el in enumerate(lst_rand):
            while i >= inc and lst_rand[i - inc] > el:
                lst_rand[i] = lst_rand[i - inc]
                i -= inc
            lst_rand[i] = el
        inc = int(inc / 2)
    print(f'Отсортированный список методом Шелла {lst_rand}')
    x = len(lst_rand) // 2
    while x:
        lst_rand.pop()
        x -= 1
    print(f'В отсортированным методом Шелла списке  \n'
          f'медианой будет число - {max(lst_rand)}')


def test(lst_rand):
    for i in range(int(len(lst_rand)) // 2):
        x = max(lst_rand)
        ind = lst_rand.index(x)
        lst_rand.pop(ind)
    print(f'Методом удаления половины списка с максимальными значениями \n'
          f'медианой будет число - {max(lst_rand)}')


test(b)
print(timeit('test', globals=globals()), '\n')
shell(a)
print(timeit('shell', globals=globals()), '\n')


# print(lst_rand)
def med(lst_rand):
    print(f'После проверки from statistics import median медианой является число -'
          f' {median(lst_rand)} с индексом - {m} (в отсортированном списке)')


med(lst_rand)
print(f"{timeit('med', globals=globals())}")

'''
при m = 100, 1000 быстрее то встроенный метод, то метод Шелла, при 10000
выигрывает метод удаления половины списка с максимальными значениями, вероятно 
за счет постепенного уменьшения самого списка в процессе работы. 
'''
