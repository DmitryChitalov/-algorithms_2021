list1 = [1, 3, 4567, -4, 89, -1, 6]

#Функция сложность которой O(n) - линейная
def minimum1(y):
    m = y[0]
    for i in y:
        if i < m:
            m = i
    return m

#Функция сложность которой O(n) - линейная
def minimum2(y):
    minn = y[0]
    for i in y:
        if i < minn:
            minn = y[i]
    return minn

#Функция сложность которой O(n**n) - квадратичная
def minimum3(y):
    for i in y:
        minn = True
        for j in y:
            if i > j:
                minn = False
        if minn:
            return i

print(minimum1(list1))
print(minimum2(list1))
print(minimum3(list1))


