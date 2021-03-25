

def get_result(n, total, sum):
    print(n, total, sum)
    if n == 0:
        if sum == total:
            return print ('Доказано !!!')
        else:
            return print('Не доказано !!!')
    sum = sum + n
    return get_result(n - 1, total, sum)



n = int(input('Введите натуральное число: '))
get_result(n, n*(n+1)/2 ,0)    # отправляем ТРИ параметра, не придумал как 2, так как в условии задачи в функцию нужно отсылать
                                # правую часть тоже, суммируем левую часть в функции, поэтому отслыаем 0,
                                    # можно вынести проверку равенства вне функции, тогда