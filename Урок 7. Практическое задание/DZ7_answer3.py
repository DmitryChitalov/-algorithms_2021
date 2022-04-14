"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
"""
from random import randint
from statistics import median


def array_gen(m=10):
    return [randint(1, 300) for i in range(2 * m + 1)]

#вариант с поиском максимального значения и выбраковки его
def mediana(user_seq):
    '''
    вариант с поиском максимального значения и выбраковки его
    '''
    user_seq = user_seq[:]
    half_len_seq = len(user_seq) // 2 + 1
    while True:
        if len(user_seq) > half_len_seq:
            user_seq.remove(max(user_seq))
        else:
            break
    return max(user_seq), half_len_seq - 1


def mediana2(user_seq):
    '''
    вариант с левым и правым списком. Также введен средний список, в который
    собираются одинкаовые значения, которые могут встречатся в списках.
    Разработан механизм распределения накопленных в нем значений.
    '''
    for i in range(len(user_seq)):
        left_side = []
        right_side = []
        centre = []
        current_median = user_seq[i]
        for j in range(len(user_seq)):
            if i == j:
                continue
            if user_seq[j] > current_median:
                right_side.append(user_seq[j])
            elif user_seq[j] < current_median:
                left_side.append(user_seq[j])
            else:
                centre.append(user_seq[j])

        if len(left_side) == len(right_side):
            if len(centre) % 2 == 0:
                return seq[i], int(len(left_side) + len(centre) / 2)
        elif len(centre) != 0 and abs(len(right_side) - len(left_side)) <= len(centre):
            if (abs(len(right_side) - len(left_side)) % 2 == 0 and len(centre) % 2 == 0) \
                    or (abs(len(right_side) - len(left_side)) % 2 != 0 and len(centre) % 2 != 0):
                return user_seq[i], len(user_seq) // 2


seq = array_gen(m=3)
print(seq)
print(median(seq))
print(mediana(seq))
print(mediana2(seq))
