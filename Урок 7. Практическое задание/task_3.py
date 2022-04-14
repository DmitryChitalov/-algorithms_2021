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
from random import randint
from statistics import median
from heapq import heappop, heappush
from timeit import timeit


# Метод кучи
def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)
    ordered = []

    while heap:
        ordered.append(heappop(heap))

    return ordered


# Метод без сортировки
def median_not_sort(array):
    while len(array) > 1:
        array.pop(array.index(max(array)))
        array.pop(array.index(min(array)))
    return array


m = int(input('Введите число: '))
my_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(f'Исходный массив: {my_list}')
print(f'Применим функцию median для нахождения медианы массива: {median(my_list[:])}')
print(f'Найдем медиану без сортировки: {median_not_sort(my_list[:])}')
res = heap_sort(my_list[:])
print(f'Отсортированный массив методом кучи: {res}, медиана: {res[m]}')

n = 1000000
print(f'Замер встроенной функции median: {timeit("median(my_list[:])", globals=globals(), number=n)}')
print(f'Замер пользовательской функции без сортировки: '
      f'{timeit("median_not_sort(my_list[:])", globals=globals(), number=n)}')
print(f'Замер пользовательской функции c сортировкой: {timeit("median(my_list[:])", globals=globals(), number=n)}')

'''
Ваш вопрос а ПР: но не проведены замеры и не оценено, что в итоге выполняется быстрее
нет сравнения со встроенной ф-цией

Ответ: Функция без сортировкой выполняется, примерно в 5 раз, дольше, чем встроенная и с сортировкой. Так получется 
из-за того что в функции без сортировки применятеся сдаление эдементов по индексу.
Встроенная функция и функция с сортировкой выполняются примерно за одинаковое время.

Прошу обратить внимание что в условии нет задачи проводить аналитику!
'''