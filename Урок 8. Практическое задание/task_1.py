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
import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(str_obj):
    priority_queue = []
    for item, freq in Counter(str_obj).items():
        priority_queue.append((freq, len(priority_queue), Leaf(item)))
    heapq.heapify(priority_queue)
    count = len(priority_queue)
    while len(priority_queue) > 1:
        freq1, _count1, left = heapq.heappop(priority_queue)
        freq2, _count2, right = heapq.heappop(priority_queue)
        heapq.heappush(priority_queue, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if priority_queue:
        [(_freq, _count, direction)] = priority_queue
        direction.walk(code, " ")
    return code


def huffman_decode(encoded, code):
    items_of_decoded_str =[]
    item_val = ""
    for item_en in encoded:
        item_val += item_en
        for item_c in code:
            if code.get(item_c) == item_val:
                items_of_decoded_str.append(item_c)
                item_val = ""
                break
    return "".join(items_of_decoded_str)



if __name__ == "__main__":
    str_obj = input('Enter the string to encode***Введите строку для кодирования: ')
    code = huffman_encode(str_obj)
    encoded = "".join(code[item] for item in str_obj)
    decoded = huffman_decode(encoded, code)
    print(f'Encoded string***Закодированная строка: {encoded}')
    print(f'Decoded string***Раскодированная строка: {decoded}')
    
    '''
    C:\Users\79115\AppData\Local\Programs\Python\Python39\python.exe "C:/Users/79115/Desktop/2 Урок Алгоритмы/Урок 2. Коды примеров + Все домашки/Algorithm8.1.py"
Enter the string to encode***Введите строку для кодирования: Python Forever !
Encoded string***Закодированная строка:  1000 1001 1010 1011 000 1100 001 1101 000 010 011 1110 011 010 001 1111
Decoded string***Раскодированная строка: Python Forever !

Process finished with exit code 0

    '''
