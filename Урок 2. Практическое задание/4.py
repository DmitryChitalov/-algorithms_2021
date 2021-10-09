def sum_of_numbers(number_of_elements):
    if number_of_elements == 1:
        return 1
    return sum_of_numbers(number_of_elements - 1) / -2 + 1


try:
    user_input = int(input('Введите число цифрами: '))
    print(sum_of_numbers(user_input))
except ValueError:
    print('Вы ввели строку! Введите число цифрами!')
    user_input = int(input('Введите число цифрами: '))
    print(sum_of_numbers(user_input))
