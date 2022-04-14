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

encoded_table = dict()


def huffman_tree(my_string):
    # создаем дек с отсортированными по возрастанию частоты использования символами
    frequency_table = deque(sorted(Counter(my_string).items(), key=lambda item: item[1]))
    # если в деке осталось больше одного символа - строим дерево
    if len(frequency_table) > 1:
        # последовательно выбираем по два очередных символа в деке
        while len(frequency_table) > 1:
            # суммируем частоту первых двух симоволов в деке
            frequency = frequency_table[0][1] + frequency_table[1][1]

            # создаем поддерево из первых двух символов в деке, одновременно извлекая их из дека
            sub_tree = {0: frequency_table.popleft()[0],
                        1: frequency_table.popleft()[0]}

            # обходим дек и ищем, куда вставить поддерево
            for i, pos in enumerate(frequency_table):
                if frequency > pos[1]:
                    continue
                else:
                    frequency_table.insert(i, (sub_tree, frequency))
                    break
            else:
                frequency_table.append((sub_tree, frequency))

    else:
        # если в деке остался один символ - ему присваивается значение 0
        frequency = frequency_table[0][1]
        sub_tree = {0: frequency_table.popleft()[0], 1: None}
        frequency_table.append((sub_tree, frequency))
    return frequency_table[0][0]


def huffman_code(tree, path=''):
    # если получен символ, а не словарь - значит заносим его с кодом в словарь
    if not isinstance(tree, dict):
        encoded_table[tree] = path
    # если получен словарь - обходим левую и правую ветви
    else:
        huffman_code(tree[0], path=f'{path}0')
        huffman_code(tree[1], path=f'{path}1')


# исходная строка
my_string = "beep boop beer!"

# создаем код
huffman_code(huffman_tree(my_string))

# выводим закодированную исходную строку
for i in my_string:
    print(encoded_table[i], end=' ')
