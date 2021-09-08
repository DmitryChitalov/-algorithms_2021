
'''Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.'''

name_shop = [ 'pyaterocka','magnit', 'gyrman', 'magazin','magazin2','magazin3','magazin4','magazin5']
profit_shop = ['123123', '211414', '62356257', '632687', '5636326', '7647256', '56782', '634562']
def find_top3(name_shop, profit_shop):
    for i in range(len(name_shop) - 1):
        for j in range(i, len(name_shop)):
            if profit_shop[j] > profit_shop[i]:
                help = profit_shop[j]
                profit_shop[j] = profit_shop[i]
                profit_shop[i] = help
                help2 = name_shop[j]
                name_shop[j] = name_shop[i]
                name_shop[i] = help2
    print( ' прибыль магазина ' ,name_shop[0], ' = ', profit_shop[0], '\n прибыль магазина ' ,name_shop[1], ' = ' ,profit_shop[1],
     '\nприбыль магазина ' ,name_shop[2], ' = ' ,profit_shop[2] )

# сложность функции O(n^2)
name_shop = [ 'pyaterocka','magnit', 'gyrman', 'magazin','magazin2','magazin3','magazin4','magazin5']
profit_shop = ['100', '120', '150', '110', '170', '130', '140', '133']

def find_top3_v2(name_shop, profit_shop):
    name_top3 = [name_shop[0], name_shop[1], name_shop[2]]
    profit_top3 = [profit_shop[0], profit_shop[1], profit_shop[2]]
    for i in range(len(name_top3) - 1):
        for j in range(i, len(name_top3)):
            if profit_top3[j] > profit_top3[i]:
                help = profit_top3[j]
                profit_top3[j] = profit_top3[i]
                profit_top3[i] = help
                help2 = name_top3[j]
                name_top3[j] = name_top3[i]
                name_top3[i] = help2

    for i in range(3, len(profit_shop)):
        if profit_top3[0] < profit_shop[i]:
            profit_top3[2] = profit_top3[1]
            profit_top3[1] = profit_top3[0]
            profit_top3[0] = profit_shop[i]

            name_top3[2] = name_top3[1]
            name_top3[1] = name_top3[0]
            name_top3[0] = name_shop[i]

        elif profit_top3[1] < profit_shop[i]:
            profit_top3[2] = profit_top3[1]
            profit_top3[1] = profit_shop[i]

            name_top3[2] = name_top3[1]
            name_top3[1] = name_shop[i]

        elif profit_top3[2] < profit_shop[i]:
             profit_top3[2] = profit_shop[i]

             name_top3[2] = name_shop[i]


    print(' прибыль магазина ', name_top3[0], ' = ', profit_top3[0], '\n прибыль магазина ', name_top3[1], ' = ',
      profit_top3[1],
      '\nприбыль магазина ', name_top3[2], ' = ', profit_top3[2])
    # O(n) - линейная
    # По сложности написания кода выгоднее использовать 1 алгоритм(он легче), по скорости 2 агоритм быстрее.

find_top3_v2(name_shop, profit_shop)














