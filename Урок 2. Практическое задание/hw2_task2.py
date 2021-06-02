#количество четных и нечетных

def count_numbers(numberstring = '', numbercount = -1):
    if numberstring == '':
        if numbercount == -1:
            numberstring = input('Введите число или q для завершения работы')
            numbercount = len(numberstring)
            even = 0
            odd = 0
            count_numbers(numberstring, numbercount)
        elif numbercount == 0:
            print('Количество четных и нечетных цифр в числе равно: (%, %)' % (even, odd))
            numbercount = numbercount - 1;
            count_numbers(numberstring, numbercount)
    elif numberstring == 'q':
        print('Всего доброго!')
        return
    else:
        try:
            number_from_string = float(numberstring)
            if number_from_string % 2 == 0:
                even += 1
            else:
                odd += 1
            number_from_string = number_from_string // 10
            numbercount = numbercount - 1
            count_numbers(str(number_from_string), numbercount)
        except:
            'Вы ввели не число'
            count_numbers('', -1)