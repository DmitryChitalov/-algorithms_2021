#число обратное данному

numberstring = int(input('Введите число'))

def reverse_number(numberstring, reversenumber=0):
    if numberstring == 0:
        print('Число, обратное данному: %' % (reversenumber))
        return 
    else:
        digit = numberstring % 10
        numberstring = numberstring // 10
        reversenumber = reversenumber * 10
        reversenumber = reversenumber + digit
        reverse_number(numberstring, reversenumber)

reverse_number(numberstring)
