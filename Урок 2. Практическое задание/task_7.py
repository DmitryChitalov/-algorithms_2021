def proof(number):
    if number < 2:
        return number
    else:
        return number + proof(number - 1)


if __name__ == '__main__':
    num = 5
    print(f'{proof(num)} == {num * (num + 1) / 2}')
