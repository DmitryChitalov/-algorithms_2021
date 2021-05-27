list1 = [1, 3, 4567, -4, 89, -1, 6]

#Функция сложность которой O(n) - линейная
def minimum1(x):
    return min(x)

#Функция сложность которой O(n**2) - квадратичная
def minimum2(y):
    minn = y[0]
    for i in y:
        if i < minn:
            minn = y[i]
    return minn

print(minimum1(list1))
print(minimum2(list1))


