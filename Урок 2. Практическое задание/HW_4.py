def g_progression():
    user_qty = int(input('Какое кол-во элементов '))

    def recur(n_qty, qty, res=0, num=1):
        if qty >= 1:
            return recur(n_qty, qty - 1, res + num, num / -2)
        else:
            print(f'Количество элементов: {n_qty}, их сумма {res}')

    return recur(user_qty, user_qty)


g_progression()
