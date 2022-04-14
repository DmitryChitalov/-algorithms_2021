def check_numbers(user_num, even_numbers=[], odd_numbers=[]):
    if user_num == 0:
        return f'The number of evens is {len(even_numbers)}, ' \
               f'The number of odds is {len(odd_numbers)}'
    else:
        current_num = user_num % 10
        user_num = user_num // 10
        if current_num % 2 == 0:
            even_numbers.append(current_num)
        else:
            odd_numbers.append(current_num)

        return check_numbers(user_num, even_numbers, odd_numbers)


user_num = int(input('Enter an integer: '))
print(check_numbers(user_num))
