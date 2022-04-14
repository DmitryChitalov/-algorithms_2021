def calc_summ(numbers, total_summ=0):
    if numbers == 1:
        return total_summ + 1
    else:
        total_summ += numbers
    return calc_summ(numbers - 1, total_summ)


my_number = 100

result = calc_summ(my_number)
result_2 = my_number * (my_number + 1) / 2

if result == result_2:
    print('Yep')
else:
    print('Nope')
