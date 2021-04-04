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


# гномья сортировка
def gnome(nums):
    i, size = 1, len(nums)
    while i < size:
        if nums[i - 1] <= nums[i]:
            i += 1
        else:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            if i > 1:
                i -= 1
    return nums


# решение без использования сортировки
def get_median(nums):
    left = []
    right = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i:
                continue
            elif nums[j] == nums[i]:
                if j < i:
                    left.append(nums[j])
                else:
                    right.append(nums[j])
            elif nums[j] < nums[i]:
                left.append(nums[j])
            else:
                right.append(nums[j])
        if len(left) == len(right):
            return nums[i]
        else:
            left.clear()
            right.clear()


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


list_of_nums = [randint(1, 100) for _ in range(list_len)]
print(f'исходный список: {list_of_nums}')
sorted_list_of_nums = gnome(list_of_nums[:])
print(f'гномья сортировка: {sorted_list_of_nums} '
      f'и медиана после нее: {sorted_list_of_nums[(len(list_of_nums) - 1) // 2]}')
print(f'медиана: {get_median(list_of_nums[:])}')
