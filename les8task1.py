from collections import Counter

class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(new_root, codes=None, code=''):
    if codes is None:
        codes = dict()
    if new_root is None:
        return
    if isinstance(new_root.value, str):
        codes[new_root.value] = code
        return codes
    get_code(new_root.left, codes, code + '0')
    get_code(new_root.right, codes, code + '1')
    return codes


def get_tree(str1):
    count = Counter(str1)
    if len(count) <= 1:
        node = Node(None)
        if len(count) == 1:
            node.left = Node([i for i in count][0])
            node.right = Node(None)
        count = {node: 1}
    while len(count) != 1:
        node = Node(None)
        junk = count.most_common()[:-3:-1]
        if isinstance(junk[0][0], str):
            node.left = Node(junk[0][0])
        else:
            node.left = junk[0][0]
        if isinstance(junk[1][0], str):
            node.right = Node(junk[1][0])
        else:
            node.right = junk[1][0]
        del count[junk[0][0]]
        del count[junk[1][0]]
        count[node] = junk[0][1] + junk[1][1]
    return [i for i in count][0]


def coding_process(str, codes):
    result = ''
    for symbol in str:
        result += codes[symbol]
    return result


def decoding_process(str, codes):
    result = ''
    i = 0
    while i < len(str):
        for code in codes:
            if str[i:].find(codes[code]) == 0:
                result += code
                i += len(codes[code])
    return result


new_str = input("Введите строчку для кодирования: ")
new_tree = get_tree(new_str)
new_codes = get_code(new_tree)
coding_new_str = coding_process(new_str, new_codes)
decoding_new_str = decoding_process(coding_new_str, new_codes)
print(f'Коды символов: {new_codes}')
print('Закодированная строка: ', coding_new_str)
print('Декодированная строка: ', decoding_new_str)

