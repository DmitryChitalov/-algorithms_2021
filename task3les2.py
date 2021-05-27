def number(n):
    return str(n) if n<10 else str(n%10) + number(n//10)

n = int(input("Введите число, которое требуется перевернуть:"))
print("Перевернутое число:", number(n))

