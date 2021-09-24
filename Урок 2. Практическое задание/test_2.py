def is_number(parametr_x):
    try:
        parametr_x = int(parametr_x)
    except:
        parametr_x = is_number(input('Вы ввели не цело число, введите, пожалуйста, число: '))
    return parametr_x
def digits(slovar):
    digit = slovar['number_help'] % 10
    if digit % 2 == 0:
        slovar['even_digits'] += 1
    else:
        slovar['odd_digits'] += 1
    slovar['number_help'] //= 10
    if slovar['number_help'] == 0:
        return
    digits(slovar)
slovar = {'even_digits': 0, 'odd_digits': 0}
slovar['number_help']=slovar['number'] = is_number(input('Введите число: '))
digits(slovar)
print("Кол-во чётных цифр в числе: ", slovar['even_digits'], "\nКол-во нечётных цифр в числе: ", slovar['odd_digits'])
