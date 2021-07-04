"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

from collections import deque, Counter


def haffman_encrypt(string_to_encrypt):
    count_string = Counter(string_to_encrypt)  # Подсчет символов в строке
    sorted_counter_string = deque(sorted(count_string.items(), key=lambda item: item[1]))
    print(sorted_counter_string)

    if len(sorted_counter_string) != 1:
        while len(sorted_counter_string) > 1:
            weight = sorted_counter_string[0][1] + sorted_counter_string[1][1]
            temp = {0: sorted_counter_string.popleft()[0],
                    1: sorted_counter_string.popleft()[0]}
            for cnt, element in enumerate(sorted_counter_string):
                if weight > element[1]:
                    continue
                else:
                    sorted_counter_string.insert(cnt, (temp, weight))

                    break
            else:
                sorted_counter_string.append((temp, weight))
    else:
        weight = sorted_counter_string[0][1]
        temp = {0: sorted_counter_string.popleft()[0], 1: None}
        sorted_counter_string.append((temp, weight))
    print(sorted_counter_string)
    return sorted_counter_string[0][0]


encrypt_table = {}


def result_encrypt(tree, path=''):
    if type(tree) is dict:
        result_encrypt(tree[0], path=f'{path}0')
        result_encrypt(tree[1], path=f'{path}1')
    else:
        encrypt_table[tree] = path


input_string = 'beep boop beer!'
result_encrypt(haffman_encrypt(input_string))

for el in input_string:
    print(encrypt_table[el], end=' ')
