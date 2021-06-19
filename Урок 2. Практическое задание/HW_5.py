def table_print(ascii_num=32):
    print(f'{ascii_num} - {chr(ascii_num)}', end=' ')
    if (ascii_num - 31) % 10 == 0:
        print('')
    if ascii_num <= len(range(32, 158)):
        return table_print(ascii_num + 1)


table_print()
