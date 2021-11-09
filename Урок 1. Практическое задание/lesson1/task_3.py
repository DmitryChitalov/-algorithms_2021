import random

company = {f'Company {i}': random.randint(10000, 30000) for i in range(1, 101)}


def get_maximum_profit_company_v1(company: map) -> map:
    '''
    Сложность: O(n log n)
    '''
    return {i[0]: i[1] for i in sorted(company.items(), key=lambda x: x[1], reverse=True)[:3]}


def get_maximum_profit_company_v2(company: map) -> map:
    '''
    Сложность: O(n)
    '''

    temp = [('', 0), ('', 0), ('', 0)]

    for key, value in company.items():
        if value > temp[0][1]:
            temp[2], temp[1] = temp[1], temp[0]
            temp[0] = (key, value)
        elif value > temp[1][1]:
            temp[2] = temp[1]
            temp[1] = (key, value)
        elif value > temp[2][1]:
            temp[2] = (key, value)

    return {i[0]: i[1] for i in temp if i[0] != ''}


def main():
    '''
    Вариант 2 лучше т.к. имеет меньшую алгоритмическую сложность
    '''
    print(get_maximum_profit_company_v1(company.copy()))
    print(get_maximum_profit_company_v2(company.copy()))


if __name__ == '__main__':
    main()
