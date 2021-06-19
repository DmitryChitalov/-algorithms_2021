from timeit import timeit
from random import randint

def median_half(lst):
    left, right, medium = [], [], 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            else:
                if lst[j] < lst[i]:
                    left.append(lst[j])
                elif lst[j] > lst[i]:
                    right.append(lst[j])
                else:
                    medium += 1
        if medium != 0:
            dif = len(left) - len(right)
            if dif < 0:
                for _ in range(-dif):
                    left.append(lst[i])
                    medium -= 1
                    if medium == 0:
                        break
                if medium != 0:
                    if medium // 2 == 0:
                        return lst[i]
                        break
            elif dif > 0:
                for _ in range(dif):
                    right.append(lst[i])
                    medium -= 1
                    if medium == 0:
                        break
                if medium != 0:
                    if medium // 2 == 0:
                        break
            else:
                for _ in range(medium // 2):
                    left.append(lst[i])
                for _ in range(medium // 2):
                    right.append(lst[i])
        if len(left) == len(right):
            return lst[i]
            break
        else:
            left.clear()
            right.clear()
            medium = 0


m = int(input('Введите значение m: '))
unsort_lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(unsort_lst)
print(median_half(unsort_lst))
print(timeit("median_half(unsort_lst[:])", globals=globals(), number=1000))
