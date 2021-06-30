def ascii_code_table(code=32):
    if code == 128:
        exit()
    print(f'`{code} - {chr(code)}`', end=' ') # ` для разграничения пар, и создание подобия таблицы
    if (code - 31) % 10 == 0:
        print('\n')
    ascii_code_table(code + 1)

ascii_code_table()
