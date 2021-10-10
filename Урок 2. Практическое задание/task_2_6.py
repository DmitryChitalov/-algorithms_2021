from random import randint

def ygadaika(pk_numb, numb_att=10):
    if numb_att == 0:
        return print(f'Вы использовали все попытки, загаданое число было = {pk_numb}')

    num = int(input(f'Введите число которое загадал компьютер от 0 до 10, у вас осталось {numb_att} попыток : '))
    if num == pk_numb:
        return print(f'Вы угадачи, это число -  {pk_numb}')
    else:
        if num > pk_numb:
            print('Вы ввели больше чем загаданое число')
            print(f'Осталось попыток = {numb_att - 1}')
            ygadaika(pk_numb,numb_att - 1)
        else:
            print('Вы ввели меньше чем загаданое число')
            print(f'Осталось попыток = {numb_att - 1}')
            ygadaika(pk_numb,numb_att - 1)

pk_random = randint(0,10)
ygadaika(pk_random)
