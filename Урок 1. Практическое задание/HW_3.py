dict1 = {'Ava': 160000, 'Eva': 356953, 'Hindi': 257102, 'Aqua': 817284, 'Tera': 883028, 'Ignite': 928374}
dict2 = {'Ava': 160000, 'Eva': 356953, 'Hindi': 257102, 'Aqua': 817284, 'Tera': 883028, 'Ignite': 928374}


def top_3_1():  # O(n)
    top_3 = []
    n = 0
    while len(top_3) != 3:  # O(1)
        n += 1
        earn = 0
        for value in dict1:  # O(n)
            if earn < dict1[value]:
                earn = dict1[value]
        # print(earn)
        for key in dict1:  # O(n)
            if dict1[key] == earn:
                print(f'{n}. {key}', end=' ')
                a = key
                top_3.append(key)
        dict1.pop(a)
    print('\n')


top_3_1()


def top_3_2(): #O(n)
    list2 = []
    for i in dict2:  # O(n)
        list2.append(((i, dict2.get(i))))
    x = sorted(list2, key=lambda item: item[1], reverse=True)  # O(n*log(n))
    print(f'1. {list2[5][0]} 2. {list2[4][0]} 3. {list2[3][0]}')


top_3_2()


""" Вывод: первый способ кажется сложнее из-за количества операций
и строк кода, но по сути они оба имеют сожность O(n). 
Я бы выбрал 2 способ из-за кол-ва операций и лаконичности
"""