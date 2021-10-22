result = ''

def resiver(number, rlt):
    res_str = len(str(number))
    if res_str == 1:
        numbers = int(number)
        result_int = str(numbers % 10)
        rlt += result_int                       # Специально перевел rlt в строку, и тогда накопление работает.
        print(f'Обратный результат {rlt}')
        return
    else:
        numbers = int(number)
        result_int = str(numbers % 10)
        rlt += result_int
        numbers = numbers // 10
        resiver(numbers, rlt)


num = int(input('Ввидите 3-4 значное число:  '))
print(f'Пользователь ввел число:  {num}')
resiver(num, result)




# Вариант 2

# def revers_number(nums):
#     return str(nums) if nums < 10 else str(nums % 10) + revers_number(nums // 10)
#     print(nums)
#
# numbers = int(input('Введите число которое требуесят перевенуть :'))
# print(type(numbers))
# print(f' Перевернутое число: {revers_number(numbers)}, {type({revers_number(numbers)})}')


