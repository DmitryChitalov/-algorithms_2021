
def get_char(value=32):
    if  value == 128:
        return
    char = chr(value)
    print(f'{value} - {char}', end= ' ')
    if (value - 31) % 10 == 0:
        print()
    value += 1
    return get_char(value)

get_char()
