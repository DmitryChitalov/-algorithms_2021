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


from collections import Counter, deque


def haffman_tree(string):
    frequency = Counter(string)
    sort_frequency = deque(sorted(frequency.items(), key=lambda item: item[1]))
    if len(sort_frequency) != 1:
        while len(sort_frequency) > 1:
            weight = sort_frequency[0][1] + sort_frequency[1][1]
            sub_tree = {0: sort_frequency.popleft()[0],
                        1: sort_frequency.popleft()[0]}
            for i, elem in enumerate(sort_frequency):
                if weight > elem[1]:
                    continue
                else:
                    sort_frequency.insert(i, (sub_tree, weight))
                    break
            else:
                sort_frequency.append((sub_tree, weight))
    else:
        weight = sort_frequency[0][1]
        sub_tree = {0: sort_frequency.popleft()[0],
                    1: None}
    return sort_frequency[0][0]


table_code = {}


def haffman_encode(tree, symbol=''):
    # tree = haffman_tree(line)
    if not isinstance(tree, dict):
        table_code[tree] = symbol
    else:
        haffman_encode(tree[0], symbol=f'{symbol}0')
        haffman_encode(tree[1], symbol=f'{symbol}1')


line = input('Введите строку, которую необходимо закодировать: ') or 'beep boop beer!'

haffman_encode(haffman_tree(line))

encode_str = ''.join([f'{table_code[i]} ' for i in line])

print(f'Исходная строка: {line}\n'
      f'Закодированная строка: {encode_str}\n'
      f'Таблица кодировки: {table_code}')


'''
Тема понятна не до конца, много прочитал в сети про кодирование по хаффману, 
для общего развития интересно.
Задание сделал по примеру, в коде разобрался.
'''