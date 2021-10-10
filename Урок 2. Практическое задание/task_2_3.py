reslt = ''

def resiver(number,rlt):
    res_str = len(str(number))
    if res_str == 1:
        num = int(number)
        result_int = str(num % 10)
        rlt += result_int                       # Специально перевел rlt в строку, и тогда накопление работает.
        print(f'Обратный результат {rlt}')
        return
    else:
        num = int(number)
        result_int = str(num % 10)
        rlt +=result_int
        num = num // 10
        resiver(num,rlt)


# num = int(input('Ввидите 3-4 значное число:  '))
# print(f'Пользователь ввел число:  {num}')
# resiver(num,reslt)




# Вариант 2

def revers_number(num):
    return str(num) if num < 10 else str(num % 10) + revers_number(num // 10)
    print(num)

numbers = int(input('Введите число которое требуесят перевенуть :'))
print(type(numbers))
print(f' Перевернутое число: {revers_number(numbers)}, {type({revers_number(numbers)})}')


