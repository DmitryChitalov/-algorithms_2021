def ascii_table(number):
    '''
        Выводит ASCII таблицу
    '''
    # начальное значение кода ASCII таблицы
    num_from = 32

    if number == num_from:
        print(f'{number: <3} - {chr(number)}', end=" ")
        return

    ascii_table(number - 1)

    if (number - 2) % 10 == 9:
        print(f'{number: <3} - {chr(number)}')
    else:
        print(f'{number: <3} - {chr(number)}', end=" ")


if __name__ == "__main__":
    ascii_table(127)
