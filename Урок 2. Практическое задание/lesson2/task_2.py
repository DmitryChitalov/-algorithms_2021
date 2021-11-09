"""
Рекурсивный подсчёт четных и нечетных чисел в числе.
"""


def get_even_odd_from_number(input_number, even=0, odd=0):

    if input_number == 0:
        return even, odd
    else:
        if input_number % 2 == 0:
            even += 1
        else:
            odd += 1
        input_number = input_number // 10

        return get_even_odd_from_number(input_number, even, odd)


number = int(input("Введите число: \n"))
print("Вы ввели: ", number)
x = get_even_odd_from_number(number)
print(f"Количество четных и нечетных цифр в числе равно: {x}\n")
