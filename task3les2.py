def inverted_number(num: int):
    if num != 0:
        return str(num % 10) + inverted_number(num // 10)
    else:
        return ''

while True:
    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Некорректный ввод!")
        continue
    inverted_number(n)

