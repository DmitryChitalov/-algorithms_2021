def calc():

    user_input = input(" Введите операцию (+, -, *, / или 0 для выхода): ")

    operations = ["+", "-", "*", "/", "0"]

    if user_input == "0":
        print("Вы завершили работу скрипта!")

    elif user_input not in operations:
        print("Нужно ввести операцию из списка! Попробуйте еще раз.")
        calc()
    else:
        first_number = input("Введите первое число: ")
        second_number = input("Введите второе число: ")

        # чтобы не дублировать для каждого (чуть изменил это условие)
        if not first_number.isdigit() or not second_number.isdigit():
            print("Вы вместо числа ввели строку (((. Исправьтесь.")
            calc()

        if user_input == "/" and second_number == "0":
            print("На ноль делить нельзя!")
            calc()

        elif user_input == "+":
            print(f"Ваш результат: {int(first_number) + int(second_number)}")
            calc()
        elif user_input == "-":
            print(f"Ваш результат: {int(first_number) - int(second_number)}")
            calc()
        elif user_input == "*":
            print(f"Ваш результат: {int(first_number) * int(second_number)}")
            calc()
        elif user_input == "/":
            print(f"Ваш результат: {int(first_number) / int(second_number)}")
            calc()


if __name__ == '__main__':
    calc()
