"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

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


def shell(lst_obj, numb):
    inc = len(lst_obj) // 2
    while inc:
        for i, el in enumerate(lst_obj):
            while i >= inc and lst_obj[i - inc] > el:
                lst_obj[i] = lst_obj[i - inc]
                i -= inc
            lst_obj[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return lst_obj[numb]


def shell_1(lst_obj):
    i = 0
    a = len(lst_obj) // 2
    while i < a:
        lst_obj.remove(max(lst_obj))
        i += 1
    return max(lst_obj)


user_answer = int(input("Введите длину массива: "))
user_answer_massive = 2 * user_answer + 1
orig_list = [random.randint(0, 50) for _ in range(user_answer_massive)]

print(f"Медианна списка, проверка, через функцию медиану, составляет: {median(orig_list)}.")
print(f"Медианна списка, через сортировку, составляет: {shell(orig_list, user_answer)}.")
print(f"Медианна списка, без сортировки, составляет: {shell_1(orig_list)}.")



