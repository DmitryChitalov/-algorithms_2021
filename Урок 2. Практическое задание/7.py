# Основная функция для решения слева
def equality(number):
    if number == 1:
        return number
    return number + equality(number - 1)


# Второстепенная функция для упращения повторений и красивого кода
def beautiful_code():
    user_input = int(input('Введите число цифрами: '))
    compare = user_input * (user_input + 1) // 2
    if compare == equality(user_input):
        print('Решение верное')
    print(equality(user_input), "==", compare)
    return


# методы исключений при воде строки и выводе большого числа, проверял на 0
try:
    try:
        beautiful_code()
    except ValueError:
        print('Вы ввели строку! Введите число цифрами!')
        beautiful_code()
except RecursionError:
    print('maximum recursion depth exceeded!')
    beautiful_code()
