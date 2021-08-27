def type_numbers(number, count_even=0, count_odd=0):
    n = len(str(number)) - 1
    if n < 1:
        if number % 10 % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        return count_even, count_odd
    else:
        if number // 10**n % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        return type_numbers(number % 10**n, count_even, count_odd)


print(type_numbers(24444233355))