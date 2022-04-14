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
test_string = 'beep boop beer!'


"""Словарь Хаффмана. Глобальная переменная"""
HUFF_DICT = {}


def make_tree(text):
    s_list = [(letter, num) for num, letter in Counter(text).items()]
    s_list = sorted(s_list, key=lambda item: item[0])

    # [(1, 'r'), (1, '!'), (2, 'p'), (2, ' '), (2, 'o'), (3, 'b'), (4, 'e')]
    while len(s_list) >= 2:
        el = (s_list[0][0] + s_list[1][0], (s_list[0][1], s_list[1][1]))

        if s_list[-1][0] < el[0]:
            s_list.append(el)
        else:
            for i in range(2, len(s_list)):
                if s_list[i][0] >= el[0]:
                    s_list.insert(i, el)
                    break
        s_list.pop(0)
        s_list.pop(0)
    haf_tree = s_list[0][1]
    return haf_tree


def coding_dict(elem,  path=''):  # (('b', (' ', 'o')), ((('r', '!'), 'p'), 'e'))
    if type(elem) == str:
        HUFF_DICT[elem] = path
        return
    coding_dict(elem[0], path + '0')
    coding_dict(elem[1], path + '1')
    return


if __name__ == '__main__':

    coding_dict(make_tree(test_string))

    encoded_string = ' '.join(HUFF_DICT[el] for el in test_string)
    print(f'test string: {test_string}')
    print(f'encoded_string: {encoded_string}')
