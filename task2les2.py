def numbers(num):
    if num == 0:
        return "Количество четных и нечетных чисел: ", 0, 0
    else:
        chet, nechet = numbers(num // 10)
        if num % 2 == 0:
            chet+=1
        else:
            nechet+=1
        return chet, nechet

try:
    k = int(input("Введите натуральное число: "))
    print(f"Количество четных и нечетных цифр в числе: {numbers(k)}")
except ValueError:
    print("Вы вместо числа ввели строку. Исправьтесь")