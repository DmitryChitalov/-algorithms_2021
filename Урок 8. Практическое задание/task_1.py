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
import ast


def str_to_deque(my_stroke):
    not_sorted = Counter(my_stroke)
    result = deque(sorted(not_sorted.items(),
                          key=lambda item: item[1]))
    return result


def get_tree(sorted_deque):
    sort_value = sorted_deque.copy()
    if len(sort_value) != 1:
        while len(sort_value) > 1:
            weight = sort_value[0][1] + sort_value[1][1]
            new_elem = {0: sort_value.popleft()[0],
                        1: sort_value.popleft()[0]}
            for i, _count in enumerate(sort_value):
                if weight > _count[1]:
                    continue
                else:
                    sort_value.insert(i, (new_elem, weight))
                    break
            else:
                sort_value.append((new_elem, weight))
    else:
        weight = sort_value[0][1]
        new_elem = {0: sort_value.popleft()[0], 1: None}
        sort_value.append((new_elem, weight))
    return sort_value[0][0]


def huffman_code(my_tree, path='', code_table={}):
    if not isinstance(my_tree, dict):
        code_table[my_tree] = path
    else:
        huffman_code(my_tree[0], path=f'{path}0')
        huffman_code(my_tree[1], path=f'{path}1')
    return code_table


def get_string_code(my_string, code_table, res='', i=0):
    if i == len(my_string):
        return res
    else:
        res += code_table[my_string[i]]
    i += 1
    return get_string_code(my_string, code_table, res, i)


def decoding(code_string, code_table):
    res = ''
    i = 0
    codes_dict = code_table
    while i < len(code_string):
        for code in codes_dict:
            if code_string[i:].find(codes_dict[code]) == 0:
                res += code
                i += len(codes_dict[code])
    return res


# all in one:
def huffman():
    x = input("Please insert 1 to code a string or 2 to uncode a string: ")
    if x == '1':
        my_string = input("Please insert the string: ")
        my_deque = str_to_deque(my_string)
        my_tree = get_tree(my_deque)
        my_code_table = huffman_code(my_tree)
        my_string_code = get_string_code(my_string, my_code_table)
        return print("The code of the string is: ", my_string_code)
    else:
        my_code = input("Please insert the code: ")
        my_table = ast.literal_eval(input("Please insert the coding table: "))
        return print(decoding(my_code, my_table))


my_string = "beep boop beer!"
my_deque = str_to_deque(my_string)
my_tree = get_tree(my_deque)
my_code_table = huffman_code(my_tree)
my_string_code = get_string_code(my_string, my_code_table)
print(my_code_table)
# {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
print(my_string_code)
##0011111010100001101110101000111110001001
print(decoding(my_string_code, my_code_table))
# beep boop beer!


# Or second variant all in one:
huffman()
"""
Please insert 1 to code a string or 2 to uncode a string: 1
Please insert the string: beep boop beer!
The code of the string is:  0011111010100001101110101000111110001001

----------------------------------------------------------------------------------------------------------------

Please insert 1 to code a string or 2 to uncode a string: 2
Please insert the code: 0011111010100001101110101000111110001001
Please insert the coding table: {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
beep boop beer!
"""
