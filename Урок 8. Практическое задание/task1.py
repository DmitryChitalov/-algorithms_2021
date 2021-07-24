from collections import Counter, namedtuple
import heapq

class Node(namedtuple("Node", ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def huffman_tree(s):
    dq = []
    for ch, freq in Counter(s).items():
        dq.append((freq, len(dq), Leaf(ch)))
    heapq.heapify(dq)
    count = len(dq)
    while len(dq) > 1:
        freq1, _count1, left = heapq.heappop(dq)
        freq2, _count2, right = heapq.heappop(dq)
        heapq.heappush(dq, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if dq:
        [(_freq, _count, root)] = dq
        root.walk(code, "")
    return code

def main():
    s = input()
    code = huffman_tree(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)




def huffman_decode(encoded, code):
    s_decoded = []
    encoded_ch = ""
    for ch in encoded:
        encoded_ch += ch
        for decod_ch in code:
            if code.get(decod_ch) == encoded_ch:
                s_decoded.append(decod_ch)
                encoded_ch = ""
                break
    return "".join(decod_ch)

def test(n_iter = 100):
    import random
    import string

    for i in range(n_iter):
        length = random.randint(0,32)
        s = "".join(random.choice(string.ascii_letters) for _ in range(length))

        code = huffman_tree(s)
        encoded = "".join(code[ch] for ch in s)
        assert huffman_decode(encoded, code) == s

if __name__ == "__main__":
    main()
    test()