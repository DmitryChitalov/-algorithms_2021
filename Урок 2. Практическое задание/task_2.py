def odd_even(user_num, odd=0, even=0):

    if user_num <= 0:
        print(f'Ваше число содержит {odd} нечетных чифр и {even} четных')

    else:
        if user_num % 2 == 0:
            even += 1
        else:
            odd +=1
        num = user_num // 10
        return odd_even(num, odd, even)


odd_even(int(input('Введите любое натуральное число\n')))
