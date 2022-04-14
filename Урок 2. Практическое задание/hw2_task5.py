# печать символов

def unicode_printer(code_number = 32):
    if code_number >= 127:
        return
    else:
        charstring = chr(code_number)
        print(str(code_number) + ' - ' + str(charstring))
        code_number +=1
        unicode_printer(code_number)

        