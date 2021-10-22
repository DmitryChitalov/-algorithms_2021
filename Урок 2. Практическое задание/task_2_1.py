def calculators():                                          #O(n)
    oper = input('+, -, *, / или 0 для выхода: ')
    if oper == '0':
        return
    if oper == '+' or oper == '-' or oper == '*' or oper == '/':  #O(n)
        True
    else:
        print('Ошибка, введите правильный знак')
        calculators()

    try:
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))

        if oper == '+':                                                 #O(n)
            result = num1 + num2
            print(f'Ваш результат = {result}')
            calculators()
        elif oper == '-':                                               #O(n)
            result = num1 - num2
            print(f'Ваш результат = {result}')
            calculators()
        elif oper == '*':
            result = num1 * num2
            print(f'Ваш результат = {result}')
            calculators()
        elif oper == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print('Делить на ноль запрещено !')
                calculators()
            else:
                result = num1 / num2
                print(f'Ваш результат = {result}')
                calculators()

    except ValueError:
        print('Вы вместо трехзначного числа ввели строку (((. Исправьтесь')


calculators()