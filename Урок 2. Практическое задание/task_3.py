def reverse_number(user_number, result=""):
    if not str(user_number).isdigit():
        print("Введите число!")
        reverse_number(input("Введите число, которое требуется перевернуть: "))
    elif user_number == 0:
        print(f"Перевернутое число: {result}")
    else:
        result += str(int(user_number) % 10)
        reverse_number(int(user_number) // 10, result)


if __name__ == '__main__':
    reverse_number(input("Введите число, которое требуется перевернуть: "))
