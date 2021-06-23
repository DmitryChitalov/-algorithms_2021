from collections import Counter


class BinaryNode:

    def __init__(self, val, left=None, right=None):
        self.right = right
        self.left = left
        self.val = val


def make_code(root, code_tab=dict(), code=''):

    if root is None:
        return

    if isinstance(root.val, str):
        code_tab[root.val] = code
        return code_tab

    make_code(root.left, code_tab, code + '0')
    make_code(root.right, code_tab, code + '1')

    return code_tab


def make_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = BinaryNode(None)

        if len(string_count) == 1:
            node.left = BinaryNode([key for key in string_count][0])
            node.right = BinaryNode(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = BinaryNode(None)
        char_count = string_count.most_common()[:-3:-1]

        if isinstance(char_count[0][0], str):
            node.left = BinaryNode(char_count[0][0])

        else:
            node.left = char_count[0][0]

        if isinstance(char_count[1][0], str):
            node.right = BinaryNode(char_count[1][0])

        else:
            node.right = char_count[1][0]

        del string_count[char_count[0][0]]
        del string_count[char_count[1][0]]
        string_count[node] = char_count[0][1] + char_count[1][1]

    return [key for key in string_count][0]


def coding(string, code_tab):
    res = ''

    for symbol in string:
        res += code_tab[symbol]

    return res


def decoding(string, code_tab):
    res = ''
    i = 0

    while i < len(string):

        for code in code_tab:

            if string[i:].find(code_tab[code]) == 0:
                res += code
                i += len(code_tab[code])

    return res


input_string = 'My uncle, man of true conviction'
tree = make_tree(input_string)
encoded_symbols = make_code(tree)
encoded_string = coding(input_string, encoded_symbols)
print('Original text: ', input_string)
print(f'Table of codes: {encoded_symbols}')
print('Encoded text: ', encoded_string)

