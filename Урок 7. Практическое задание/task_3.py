"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
"""

import random
import statistics
import timeit

number_cycles = 100000
user_number = int(input("Введите количество элементов в массиве: "))


def gener_numb(us_num):    # тут сгенерируем массив
    if us_num % 2 == 0:
        us_num += 1    # нам нужен нечётный массив, поэтому + 1
    else:
        us_num = us_num
    gen_number = [random.randint(0, 100) for i in range(us_num)]
    return gen_number


list_number = gener_numb(user_number)


# поиск медианы списка.  Время работы: 2.092643700001645
def search_m(num):    # решение без сортировки.
    counter_stop = 0
    len_list = (len(num) // 2)
    while counter_stop != len_list:    # тут удалим все макс значения, проходы до половины длины списка
        num.pop(num.index(max(num, key=lambda i: int(i))))
        counter_stop += 1
    return f'В неотсортированном массиве: \n{list_number} \n' \
           f'Медиана равна: {max(num, key=lambda i: int(i))}\n'


print(f'Время работы: {timeit.timeit("search_m(list_number[:])", globals=globals(), number=number_cycles)}'
      f'\n{search_m(list_number[:])}')


# поиск медианы списка. Время работы: 3.6379515000007814
def shell(seq):  # сортировка. Можно и sorted, но так интереснее (хотя и медленнее)
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)

    def search_m_sort(num):    # поиск медианы
        counter_stop = 0
        len_list = (len(num) // 2)
        while counter_stop != len_list:  # тут удалим все макс значения, проходы до половины длины списка
            num.pop(num.index(max(num, key=lambda i: int(i))))
            counter_stop += 1
        return f'В отсортированном массиве: \n{seq} \n' \
               f'Медиана равна: {max(num, key=lambda i: int(i))}\n'

    return search_m_sort(seq[:])


print(f'Время работы: {timeit.timeit("shell(list_number[:])", globals=globals(), number=number_cycles)}'
      f'\n{shell(list_number[:])}')


# поиск медианы списка встроенной функцией. Время работы: 0.36155499999586027
def search_m_statistics(list_numb):
    return f'В неотсортированном массиве: \n{list_numb}\n' \
           f'Медиана равна: {statistics.median(list_numb)}'


print(f'Время работы: '
      f'{timeit.timeit("search_m_statistics(list_number[:])", globals=globals(), number=number_cycles)}'
      f'\n{search_m_statistics(list_number[:])}')


"""
время работы (по порядку) если брать 10 символов на входе:
2.092643700001645
3.6379515000007814
0.36155499999586027

вывод: втроенная функция median работает конечно же быстрее
"""
