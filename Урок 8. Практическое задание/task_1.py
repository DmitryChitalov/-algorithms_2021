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
import heapq

code_str = 'beep boop beer!'


def huffman_encod(s):
    dict_encod = {}
    heap = [(freq, char) for char, freq in Counter(s).items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        _freq, char = heapq.heappop(heap)
        dict_encod[char] = str(0)

    while len(heap) >= 2:
        min_freq, min_char = heapq.heappop(heap)
        min2_freq, min2_char = heapq.heappop(heap)

        heapq.heappush(heap, (min_freq + min2_freq, min_char + min2_char))

        for i, char_string in enumerate([min_char, min2_char]):
            for char in char_string:
                if char in dict_encod:
                    dict_encod[char] = str(i) + dict_encod[char]
                else:
                    dict_encod[char] = str(i)

    return dict_encod


def decode(dict_encode, str_encode):
    decoded_str = ''
    dict_encode = {value: key for key, value in dict_encode.items()}

    sequence = ''
    for char in str_encode:
        sequence += char
        if sequence in dict_encode:
            decoded_str += dict_encode[sequence]
            sequence = ''

    return decoded_str


encoding_dict = huffman_encod(code_str)
encoded_str = ''.join([encoding_dict[char] for char in code_str])
print(encoded_str)
print(decode(encoding_dict, encoded_str))
