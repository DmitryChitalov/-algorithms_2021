"""

По введенным пользователем координатам двух точек вывести уравнение прямой вида
y = kx + b, проходящей через эти точки.

"""
try:
    X1 = float(input("X1 = "))
    Y1 = float(input("Y1 = "))
    X2 = float(input("X2 = "))
    Y2 = float(input("Y2 = "))
    k = (Y1 - Y2) / (X1 - X2)
    b = Y2 - k * X2
    print(f'y = {k:.2f}x+{b:.2f}')

except ValueError:
    print("Вы ввели не числа")
