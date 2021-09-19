from memory_profiler import profile

dict_evens_odds = {'evens': 0, 'odds': 0}


@profile
def profiled_even_n_odd(*args):
    def even_n_odd(number: int):
        if number // 10 == 0 and number == 0:
            return
        last_digit = number % 10
        if last_digit % 2 == 0:
            dict_evens_odds['evens'] += 1
        else:
            dict_evens_odds['odds'] += 1
        even_n_odd(number // 10)

    return even_n_odd(*args)


def ask_user():
    number = input("Введите целое число! Нажмите 0 для выхода: ")

    try:
        if int(number) <= 0:
            return None
        profiled_even_n_odd(int(number))
        print(dict_evens_odds)
    except ValueError:
        print("Допускаются только целые числа. Попробуйте еще раз.")
    dict_evens_odds['evens'] = 0
    dict_evens_odds['odds'] = 0
    return ask_user()


if __name__ == "__main__":
    ask_user()

"""
Чтобы профилировщик не вызывался при каждом вызове рекурсивной ункции,
нужно завернуть исходную функцию в другую функцию
"""
