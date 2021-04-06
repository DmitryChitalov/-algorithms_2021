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

m = int(input("Введите целое значение m: "))

#--- Gnome 
def gnm_sort(lst):
    i=1
    vol = len(lst)
    while i < vol:
        if lst[i-1] <= lst[i]:
            i += 1
        else:
            lst[i-1],lst[i] = lst[i],lst[i-1]
            if i > 1:
                i -= 1
    return lst
#--- Shell
def shl_sort(lst):
    hlf = int(len(lst)/2)
    while hlf:
        for i, el in enumerate(lst):
            while i >= hlf and lst[i - hlf] > el:
                lst[i] = lst[i - hlf]
                i -= inc
            lst[i] = el
        hlf = 1 if hlf == 2 else int(hlf*5.0/11)
    return lst

lst = [randint(0,100) for i in range(2*m+1)]

#-------------------------------------------------------------------
print(f"test list: {lst}")
slst = gnm_sort(lst)
print(f"sorted Gnome list: {slst}")
print(f"Gnome median: {slst[m]}")
slst = shl_sort(lst)
print(f"sorted Shell list: {slst}")
print(f"Shell median: {slst[m]}")