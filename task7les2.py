def s(n):
    if n == 1:
        return 1, 1
    else:
        return s(n-1) + n

num = int(input("Введите число: "))
if s(num) == num*(num-1) / 2:
    print("Выражение доказано!")