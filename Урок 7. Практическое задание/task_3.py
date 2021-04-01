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
from timeit import timeit
from memory_profiler import profile
from statistics import median


# решение с использованием гномьей сортировки

# итоговая сложность O(n^2)
def gnome_sort(list_to_sort):
    i = 1
    while i < len(list_to_sort):
        if list_to_sort[i - 1] > list_to_sort[i]:
            list_to_sort[i - 1], list_to_sort[i] = list_to_sort[i], list_to_sort[i - 1]

            if i > 1:
                i -= 1
        else:
            i += 1

    return list_to_sort


# итоговая сложность O(n^2), хотя и присутствует усовершенствование:
# запоминаем позицию, с которой начались обмены, затем сразу же перепрыгнуть в эту позицию при завершении обменов
def upgrade_gnome_sort(list_to_sort):
    i = 1
    j = 2
    while i < len(list_to_sort):
        if list_to_sort[i - 1] > list_to_sort[i]:
            list_to_sort[i - 1], list_to_sort[i] = list_to_sort[i], list_to_sort[i - 1]
            i -= 1

            if i == 0:
                i, j = j, j + 1
        else:
            i, j = j, j + 1

    return list_to_sort


@profile
def gnome_sort_mem_prof(list_to_sort):
    gnome_sort(list_to_sort)


@profile
def upgr_gnome_sort_mem_prof(list_to_sort):
    upgrade_gnome_sort(list_to_sort)


# решение без использования сортировки, итоговая сложность O(n^2)
def get_median_variant_1(numbers_list):
    left = []
    right = []
    for i in range(len(numbers_list)):
        for j in range(len(numbers_list)):
            if j == i:
                continue
            elif numbers_list[j] == numbers_list[i]:
                if j < i:
                    left.append(numbers_list[j])
                else:
                    right.append(numbers_list[j])
            elif numbers_list[j] < numbers_list[i]:
                left.append(numbers_list[j])
            else:
                right.append(numbers_list[j])

        if len(left) == len(right):
            return numbers_list[i]
        else:
            left.clear()
            right.clear()


@profile
def get_med_var_1_mem_prof(numbers_list):
    get_median_variant_1(numbers_list)


# итоговая сложность O(n^2)
def get_median_variant_2(numbers_list):
    for i in range(len(numbers_list) // 2):     # сложность цикла O(n)
        numbers_list.remove(max(numbers_list))  # сложность remove() - O(n), max() - O(n) => итоговая O(2n) = (n)

    return max(numbers_list)                    # O(n)


@profile
def get_med_var_2_mem_prof(numbers_list):
    get_median_variant_2(numbers_list)


while True:
    try:
        list_len = int(input('введите желаемую длину списка: '))

        if list_len % 2 == 0:
            raise Exception
        else:
            break

    except ValueError:
        print('длина списка должна быть целым числом!')
    except Exception:
        print('список может быть лишь нечетной длины!')


list_numbers = [randint(1, 100) for _ in range(list_len)]
print(f'исходный список: {list_numbers}')

list_numbers_sorted = gnome_sort(list_numbers[:])
print(f'отсортированный список: {list_numbers_sorted}')
print(f'медиана списка: {list_numbers_sorted[(len(list_numbers) - 1) // 2]}')  # 2m+1 = len() => m = (len()-1)/2

print(f'медиана списка, найденная с помощью get_median_variant_1: {get_median_variant_1(list_numbers)}')
print(f'медиана списка, найденная с помощью get_median_variant_2: {get_median_variant_2(list_numbers[:])}')
print(f'медиана, найденная с помощью модуля statistics: {median(list_numbers)}')

list_numbers = [randint(1, 100) for _ in range(11)]

# время - 0.015 c, память - 19.7 MiB
print(f"обычный вариант: {timeit('gnome_sort(list_numbers[:])', number=1000, globals=globals())}")
gnome_sort_mem_prof(list_numbers[:])

# время - 0.01 c, память - 19.7 MiB
print(f"улучшенный вариант: {timeit('upgrade_gnome_sort(list_numbers[:])', number=1000, globals=globals())}")
upgr_gnome_sort_mem_prof(list_numbers[:])

# время - 0.015 c, память - 20.2 MiB
print(f"get_med_var_1: {timeit('get_median_variant_1(list_numbers)', number=1000, globals=globals())}")
get_med_var_1_mem_prof(list_numbers)

# время - 0.0025 c, память - 20.2 MiB
print(f"get_med_var_2: {timeit('get_median_variant_2(list_numbers[:])', number=1000, globals=globals())}")
get_med_var_2_mem_prof(list_numbers[:])

# время - 0.00053 с
print(f"встроенная функция median(): {timeit('median(list_numbers)', number=1000, globals=globals())}")

list_numbers = [randint(1, 100) for _ in range(101)]

# время - 1.31 c, память - 19.7 MiB
print(f"обычный вариант: {timeit('gnome_sort(list_numbers[:])', number=1000, globals=globals())}")
gnome_sort_mem_prof(list_numbers[:])

# время - 0.85 c, память - 19.7 MiB
print(f"улучшенный вариант: {timeit('upgrade_gnome_sort(list_numbers[:])', number=1000, globals=globals())}")
upgr_gnome_sort_mem_prof(list_numbers[:])

# время - 1.26 c, память - 20.2 MiB
print(f"get_med_var_1: {timeit('get_median_variant_1(list_numbers)', number=1000, globals=globals())}")
get_med_var_1_mem_prof(list_numbers)

# время - 0.083 c, память - 20.2 MiB
print(f"get_med_var_2: {timeit('get_median_variant_2(list_numbers[:])', number=1000, globals=globals())}")
get_med_var_2_mem_prof(list_numbers[:])

# время - 0.0039 с
print(f"встроенная функция median(): {timeit('median(list_numbers)', number=1000, globals=globals())}")

list_numbers = [randint(1, 100) for _ in range(1001)]

# время - 146.25 c, память - 19.7 MiB
print(f"обычный вариант: {timeit('gnome_sort(list_numbers[:])', number=1000, globals=globals())}")
gnome_sort_mem_prof(list_numbers[:])

# время - 95.33 c, память - 19.7 MiB
print(f"улучшенный вариант: {timeit('upgrade_gnome_sort(list_numbers[:])', number=1000, globals=globals())}")
upgr_gnome_sort_mem_prof(list_numbers[:])

# время - 167.26 c, память - 20.7 MiB
print(f"get_med_var_1: {timeit('get_median_variant_1(list_numbers)', number=1000, globals=globals())}")
get_med_var_1_mem_prof(list_numbers)

# время - 7.17 c, память - 20.7 MiB
print(f"get_med_var_2: {timeit('get_median_variant_2(list_numbers[:])', number=1000, globals=globals())}")
get_med_var_2_mem_prof(list_numbers[:])

# время - 0.071 с
print(f"встроенная функция median(): {timeit('median(list_numbers)', number=1000, globals=globals())}")

'''
поскольку сложность получения конкретного элемента в списке O(1), будем считать, что данным временем выполнения 
можно пренебречь => у варианта решения через сортировку замеры проводились лишь для реализаций самой сортировки. 
результаты проведения временных замеров подтвердили тот факт, что теоретическая сложность алгоритма гномьей 
сортировки O(n^2). однако, несмотря на это, улучшенный алгоритм показал существенно лучшую скорость выполнения в 
сравнении с исходным алгоритмом сортировки. объем занимаемой памяти у обоих алгоритмов одинаков, это связано с тем, 
что на вход обоих алгоритмов передаются копии различной длины одного и того же массива

также было приведено 2 решения без использования сортировки. результаты замеров показали, что на массивах небольшой 
длины (а именно, 11) скорость выполнения, примерно, одинакова. на массивах длины 101 появляется разница во времени 
выполнения, на массивах большой длины вариант решения get_median_variant_2 через функции max() и remove() существенно 
быстрее, чем вариант решения get_median_variant_1, также существенно быстрее любого из варианта сортировки. это 
связано с тем, что происходит постоянное сокращение длины переданного в функцию массива. замеры памяти показали, 
что оба варианта расходуют одинаковое количество памяти, это связано с тем, что в них передаются массивы одной и той 
же длины, состоящие из одних и тех же типов данных 

результаты временных замеров времени для встроенной функции median() показали, что она работает существенно быстрее
всех приведенных вариантов решений во всех случаях
'''
