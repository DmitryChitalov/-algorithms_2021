import heapq
from collections import Counter, deque
from collections import namedtuple

str_user = "beep boop beer!"


class Branches(namedtuple("Branch", ["left", "right"])):    # класс ветвей
    def walk(self, code_dictionary, binary_code):
        self.left.walk(code_dictionary, binary_code + "0")
        self.right.walk(code_dictionary, binary_code + "1")


class Leaves(namedtuple("Leave", ["symbol"])):    # класс листье
    def walk(self, code_dictionary, binary_code):
        code_dictionary[self.symbol] = binary_code or "0"


def huffman_encode(str_coding):
    huffman_list = []
    code_binary = {}
    sorted_elements = deque(sorted((Counter(str_coding)).items(), key=lambda item: item[1]))
    for number_occurrences, obj in sorted_elements:    # тут создадутся листья
        huffman_list.append((obj, len(huffman_list), Leaves(number_occurrences)))
    heapq.heapify(huffman_list)
    len_huffman_list = len(huffman_list)
    while len(huffman_list) > 1:    # тут создадутся ветви
        number1, _count1, left = heapq.heappop(huffman_list)
        number2, _count2, right = heapq.heappop(huffman_list)
        heapq.heappush(huffman_list, (number1 + number2, len_huffman_list, Branches(left, right)))
        len_huffman_list += 1
    [(_, _, root)] = huffman_list
    root.walk(code_binary, "")
    return code_binary


code = huffman_encode(str_user)

print(*(code[i] for i in str_user))
