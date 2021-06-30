""" скоро можно будет вывести эту функцию в отдельный модуль, чтоб не писать каждый раз  """

def count_input():
    try:
        num = int(input('Введите количество элементов: \n'))
        if num <= 0:
            print('Error! т.е. ОШИБКА!!! может я забыл сказать, число должно быть натуральным')
            return count_input()
    except ValueError:
        print('Не похоже это на натуральное число')
        return count_input()
    return my_sum(num)

def my_sum(num):
    if num > 1:
        return (-0.5) ** (num - 1) + my_sum(num - 1)
    print('Сумма элементов равна: ', end='')
    return num

print(count_input())
