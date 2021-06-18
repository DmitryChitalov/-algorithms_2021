from collections import Counter, deque


class HuffmanEncoder:
    def __init__(self, string_in):
        self.string_in = str(string_in)
        self.code_table = dict()

    def huffman_tree(self):
        elem_frequency = Counter(self.string_in)
        sorted_elem = deque(sorted(elem_frequency.items(), key=lambda item: item[1]))
        if len(sorted_elem) != 1:
            while len(sorted_elem) > 1:
                freq = sorted_elem[0][1] + sorted_elem[1][1]
                tree_node = {0: sorted_elem.popleft()[0],
                             1: sorted_elem.popleft()[0]}
                for index, arguments in enumerate(sorted_elem):
                    if freq > arguments[1]:
                        continue
                    else:
                        sorted_elem.insert(index, (tree_node, freq))
                        break
                else:
                    sorted_elem.append((tree_node, freq))
        else:
            freq = sorted_elem[0][1]
            tree_node = {0: sorted_elem.popleft()[0], 1: None}
            sorted_elem.append((tree_node, freq))

        return sorted_elem[0][0]

    def huffman_code_table(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.huffman_code_table(tree[0], path=f'{path}0')
            self.huffman_code_table(tree[1], path=f'{path}1')
        return self.code_table

    def huffman_encoding(self):
        encoded_string = ''
        for i in self.string_in:
            encoded_string += self.code_table[i] + ' '
        return encoded_string

    def huffman_decoding(self):
        decoded_string = ''
        for item in self.huffman_encoding().split(' '):
            for key, value in self.code_table.items():
                if value == item:
                    decoded_string += key
        return decoded_string


my_string = HuffmanEncoder("beep boop beer!")

print(my_string.huffman_code_table(my_string.huffman_tree()))
print(my_string.huffman_encoding())
print(my_string.huffman_decoding())
