def sum_check(n):
    if n == 1:
        return 1, 1
    else:
        return sum_check(n-1) + n

num = int(input("Введите число: "))
if sum_check(num) == num*(num-1) / 2:
    print("Выражение доказано!")