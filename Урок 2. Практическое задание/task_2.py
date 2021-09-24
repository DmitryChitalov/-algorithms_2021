def counter(user_number, even=0, odd=0):
    """
    валидация str(user_number).isdigit специально хоть input - строка,
    так как далее я переназначил его в int
    """

    if not str(user_number).isdigit():  # валидация
        print("Нужно ввести число!")
        counter(input("Введите число: "))
    else:
        user_number = int(user_number)
        if user_number == 0:
            print(f"Количество четных и нечетных цифр в числе равно: {even},{odd}")
        else:
            if int(user_number) % 10 % 2 == 0:
                even += 1
                return counter(user_number // 10, even, odd)
            else:
                odd += 1
                return counter(user_number // 10, even, odd)


if __name__ == '__main__':
    counter(input("Введите число: "))
