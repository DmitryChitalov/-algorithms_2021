"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
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
from timeit import timeit


def shell_sort(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data                     # вернет отсортированный массив

def median_shell_sort(data):
    shell_sort(data)
    return data[(len(data)-1)//2]

def median_left_right(data):
    left = []
    right = []
    for el1 in data:
        for el2 in data:
            if el1 > el2:
                left.append(el2)
            elif el1 < el2:
                right.append(el2)
        # аналог len(left)==len(right), учитывающий вариант, когда несколько значений в массиве = медиане
        if abs(len(left) - len(right)) < len(data)-len(left)-len(right):
            return el1
        else:
            left.clear()
            right.clear()

def median_del_max(data):
    for i in range(len(data)//2):
        data.remove(max(data))
    return max(data)

def median_internal_sort(data):
    data.sort()
    return data[(len(data)-1)//2]


list_param = [10, 100, 1000]
func_list = ['median_shell_sort', 'median_left_right', 'median_del_max', 'median_internal_sort', 'median']
max_len = len(max(func_list, key=len))

for param in list_param:
    print(f'Сравним временные затраты вариантов для массива из ({param*2+1}) элемента(ов):')
    orig_list = [randint(0, param * 10) for _ in range(param * 2 + 1)]
    for el in func_list:
        print(f'Функция {el}:'.ljust(max_len + 10, '_'),
              timeit(el + '(orig_list[:])', number=100, globals=globals()))

exit()

m = 10
orig_list = [randint(0, m*10) for _ in range(m*2+1)]
print(orig_list)
print(shell_sort(orig_list[:]))
print(median_shell_sort(orig_list[:]))
print(median_left_right(orig_list[:]))
print(median_del_max(orig_list[:]))
print(median_internal_sort(orig_list[:]))
print(median(orig_list[:]))

exit()

'''
Согласно поставленной задаче, нахождение медианы реализовано несколькими методами:

(median_shell_sort) - предварительно отсортировав массив методом Шелла (shell_sort) и вернув средний элемент.
Эта сортировка является усовершенствованной модификацией сортировки "вставкой".
Согласно проведенной аналитике, этот вариант "проигрывает" только встроенным специализированному 
методу median из statistics и встроенной сортировке (median_internal_sort).

(median_left_right) - самый "медленный" алгоритм на больших множествах. 
Стоит отметить нюанс, который проявляется при совпадении нескольких элементов с медианой.
В этом случае, не работат проверка (len(left)==len(right)). Поэтому, учитывается коридор отклонения.  

(median_del_max) - принимая во внимание использование встроенной функции (max), алгоритм в разы лучше 
(median_left_right) справляется с поиском. Но, если "по-честному" искать максимальный эл. это преимущетсво 
будет утрачено.

Аналитика:
Функция median_shell_sort:____ 0.002427669000000021
Функция median_left_right:____ 0.003062207999999955
Функция median_del_max:_______ 0.001171270000000002
Функция median_internal_sort:_ 0.00013523999999998093
Функция median:_______________ 0.00024391400000001173
Сравним временные затраты вариантов для массива из (201) элемента(ов):
Функция median_shell_sort:____ 0.053261415000000034
Функция median_left_right:____ 0.19034414300000002
Функция median_del_max:_______ 0.07446020399999997
Функция median_internal_sort:_ 0.0015884600000000137
Функция median:_______________ 0.0015908749999999916
Сравним временные затраты вариантов для массива из (2001) элемента(ов):
Функция median_shell_sort:____ 1.115009107
Функция median_left_right:____ 17.271851289999997
Функция median_del_max:_______ 5.8526312229999995
Функция median_internal_sort:_ 0.04100352600000079
Функция median:_______________ 0.040364155999998985
'''



