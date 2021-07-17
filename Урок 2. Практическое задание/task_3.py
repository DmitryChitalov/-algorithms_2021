number = list(str(input('Введите число - ')))
rebmun = []


def revers():
    if len(number) == 0:
        print(f'Перевернутое число - {"".join(rebmun)}')
    else:
        rebmun.append(number.pop())
        return revers()


revers()


# def revers_number(numb):
#     rest_numb, numeral = divmod(numb, 10)
#     if rest_numb == 0:
#         return str(numeral)
#     else:
#         return str(numeral) + str(revers_number(rest_numb))
#
#
# number = int(input("Введите число, которое требуется перевернуть: "))
# print(f'Перевернутое число: {revers_number(number)}')
