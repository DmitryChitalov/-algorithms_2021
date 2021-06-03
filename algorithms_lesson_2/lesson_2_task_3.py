def rev_numbers(user_num, reverse_list=[]):
    if user_num == 0:
        return ''.join(map(str, reverse_list))
    else:
        current_num = user_num % 10
        user_num = user_num // 10
        reverse_list.append(current_num)
        return rev_numbers(user_num, reverse_list)

user_num = int(input('Enter an integer: '))
print(rev_numbers(user_num))
