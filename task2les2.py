def numbers(num, chet = 0, nechet = 0):
    if num == 0:
        return "Количество четных и нечетных чисел: ", chet, nechet
    else:
        figure = num % 10
        num = num//10
        if figure % 2 == 0:
            chet+=1
        else:
            nechet+=1
        return numbers(num, chet, nechet)

try:
    k = int(input("Введите натуральное число: "))
    print(f"Количество четных и нечетных цифр в числе: {numbers(k)}")
except ValueError:
    print("Вы вместо числа ввели строку. Исправьтесь")