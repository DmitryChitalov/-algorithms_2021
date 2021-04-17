from collections import Counter
import hashlib


class Node:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, codes=dict(), code=''):

    if root is None:
        return
    elif isinstance(root.value, str):  # проверяемый является ли root.value экземпляром указанного класса
        codes[root.value] = code  # если "да" то это будет код
        return codes
    else:
        get_code(root.left, codes, code + '0')
        get_code(root.right, codes, code + '1')
    return codes


def get_tree(string):
    string_count = Counter(string)  # получаем частоту для каждого символа в строке

    if len(string_count) <= 1:
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]
        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]
        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]


    return [key for key in string_count][0]


def coding(string, codes):
    res = ''
    string = set(string)  # оставляем только уникальные символы в строке
    for symbol in string:
        res += codes[symbol]
        print("{}: {}".format(symbol, codes[symbol]))  # выводим символ и его код
    print('Сжатая строка:', res)

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

my_string = input('Введите строку для сжатия: ')

tree = get_tree(my_string)
codes = get_code(tree)
print(codes)
coding_str = coding(my_string, codes)
print("бинарный код:", text_to_bits(my_string))  # только для проверки эффективности сжалия
#hash_object = hashlib.md5(b'Someone else')
#print("Кодировка через md5:", hash_object.hexdigest())  # только для проверки эффективности сжалия

"""
Введите строку для сжатия: Slomeone else
{'l': '00', 'S': '010', 'n': '0110', 'm': '0111', 's': '1000', ' ': '1001', 'o': '101', 'e': '11'}
n: 0110
S: 010
m: 0111
l: 00
 : 1001
o: 101
s: 1000
e: 11
Сжатая строка: 01100100111001001101100011
бинарный код: 01010011011011000110111101101101011001010110111101101110011001010010000001100101011011000111001101100101
Кодировка через md5: 81e053d78f01540e9cd6fb68a1c03976

Видим что получены коды для всех уникальных элементов в ключая буквы в верхнем регистре и пробелы
так же можем наблюдать эффективность сжатия по сравнению с другими способами кодировки строки
"""
