list1 = [1, 3, 4567, -4, 89, -1, 6]

"""Функция 1. Cложность O(n) - линейная"""
def minimum1(lst):
    minn = lst[0]
    for i in lst:
        if i < minn:
            minn = lst[i]
    return minn

"""Функция 2. Cложность O(n**n) - квадратичная"""
def minimum2(lst):
    for i in lst:
        minn = True
        for j in lst:
            if i > j:
                minn = False
        if minn:
            return i

print(minimum1(list1))
print(minimum2(list1))