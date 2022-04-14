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
from collections import Counter
from itertools import zip_longest

"""
Я попыталась реализовать свой вариант построения бинарного дерева, а считывание его и кодирование
символов в таблицу Хаффмана - вариант из конспекта (функция get_a_table).
Мой вариант, скорее всего, хуже уже существующих, так как целью было не создать оптимальное решение,
а разобраться в механизме.

Чтобы не повторяться с решениями с урока, я использовала не deque или ООП, а стандартные объекты
Python - списки и словари.

Задание интересное, спасибо!
"""

tongue_twister = 'thirty thirsty thieves'


def count_n_invert(some_str):
    """Function counts frequency of letters in a string and sorts it in ascending order"""
    calc_letters = Counter(some_str)
    print(calc_letters)
    inverted_letter_map = sorted(calc_letters, key=calc_letters.get)
    accumulation(inverted_letter_map)


def accumulation(some_letter_list):
    """Splitting a list of letters into two lists"""
    tmp_1, tmp_2 = [], []
    counter = 0
    for i in some_letter_list:
        if counter % 2 == 0:
            tmp_2.append(i)
            counter += 1
        else:
            tmp_1.append(i)
            counter += 1
    dict_of_values(tmp_1, tmp_2)


def dict_of_values(lst_1, lst_2):
    """Building a binary tree"""
    dict_1, dict_2 = {}, {}
    for i, j in zip_longest(lst_1, lst_2):
        if lst_2.index(j) < 1:
            dict_1 = {0: i, 1: j}
        elif lst_2.index(j) < 2:
            dict_2 = {0: i, 1: j}
        else:
            dict_1 = {0: dict_1, 1: j}
            if i is not None:
                dict_2 = {0: i, 1: dict_2}
    my_dict = {0: dict_2, 1: dict_1}
    get_a_table(my_dict)


def get_a_table(some_dict):
    """Encoding a binary tree using the Huffman algorithm"""
    code_table = {}

    def haffman_code(tree, path=''):
        if not isinstance(tree, dict):
            code_table[tree] = path
        else:
            haffman_code(tree[0], path=f'{path}0')
            haffman_code(tree[1], path=f'{path}1')
    haffman_code(some_dict)
    for i in code_table:
        print(f"{i} - {code_table[i]}")


count_n_invert(tongue_twister)
