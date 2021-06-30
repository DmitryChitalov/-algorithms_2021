def number_reverse(num):
    if num < 10:
        print('Число наоборот: ')
        return str(num)
    return str(num % 10) + number_reverse(num // 10)

def number_input():
    try:
        num = int(input('Введите число которое будем переворачивать: \n'))
        if num <= 0:
            print('Error! т.е. ОШИБКА!!! может я забыл сказать, число должно быть натуральным')
            return number_input()
    except ValueError:
        print('Не похоже это на натуральное число')
        return number_input()
    return number_reverse(num)

print(number_input())
