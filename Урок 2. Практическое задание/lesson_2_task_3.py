
def get_result(num):
    a = num // 10
    b = num % 10
    if a == 0:
        return str(b)
    else:
        return str(b) + get_result(a)

number = int(input('Введите число:'))
print (get_result(number))
