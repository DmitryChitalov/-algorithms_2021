def revers_number(number, newnumber=0):
    n = len(str(number)) - 1
    if number == 0:
        return newnumber
    else:
        numb = number % 10
        newnumber += numb * 10**n
        number = number // 10
        n -= 1
        return revers_number(number, newnumber,)

print(revers_number(155566489))