def summa(n):
    if n == 1:
        return n
    else:
        return summa(n-1) + n

num = int(input("Введите число: "))
if summa(num) == num*(num-1) / 2:
    print("Выражение доказано!")