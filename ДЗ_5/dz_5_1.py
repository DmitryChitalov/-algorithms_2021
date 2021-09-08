import collections

Firm = collections.namedtuple('firm', ['name', 'mid_profit'])


def ask_user():
    number = input("Введите количество предприятий для расчета прибыли: ")

    try:
        if int(number) <= 0:
            return
        # количество преприятий
        firms_count = int(number)

        # средние значения по всем предприятиям
        ls_firms = []
        mid_value = 0

        # Коллекция приприятий со среднегодовой прибылью
        firm_obj = None

        while firms_count > 0:
            firm_name = input("Введите название предприятия: ")
            profits = input("Через пробел введите прибыль данного предприятия "
                            "за каждый квартал (Всего 4 квартала)")
            arr_profits = profits.split(" ")
            int_arr_profits = list(map(lambda x: int(x), arr_profits))

            firm_obj = Firm(firm_name, sum(int_arr_profits) / 4)
            ls_firms.append(firm_obj)

            firms_count -= 1

        mid_value = sum([m_prof.mid_profit for m_prof in ls_firms]) / len(ls_firms)

        # Фирмы с прибылью выше среднего
        profit_gt_avg_firms = []

        # Фирмы с прибылью ниже среднего
        profit_lt_avg_firms = []

        for firm in ls_firms:
            if firm.mid_profit > mid_value:
                profit_gt_avg_firms.append(firm.name)
            else:
                profit_lt_avg_firms.append(firm.name)

        print("Предприяте, с прибылью выше среднего значения:")
        print(profit_gt_avg_firms)
        print("Предприяте, с прибылью ниже среднего значения:")
        print(profit_lt_avg_firms)

    except ValueError:
        print("Вы ввели не целое число. ")


if __name__ == "__main__":
    ask_user()
