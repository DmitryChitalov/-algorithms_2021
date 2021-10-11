from memory_profiler import profile


@profile
def wrapper(input_number):
    def func(numb, reversed_number=''):
        if numb == 0:
            return reversed_number
        else:
            digit = numb % 10
            return func(numb // 10, reversed_number + str(digit))

    return func(input_number)


if __name__ == '__main__':
    number = int(input('Введите число, которое требуется перевернуть: '))
    print(f'Перевернутое число: {wrapper(number)}')

    """
    Проблема в том, что при каждом вызове функции мы получаем новый вывод профайлера.
    Решение:
    Нужно обернуть рекурсивную функцию. 
    """
