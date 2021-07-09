from collections import Counter, deque


class Node:
    def __init__(self, left_child=None, right_child=None):
        self.left_child = left_child
        self.right_child = right_child


class HuffmanTree:
    def __init__(self, text):
        self.text = text
        self.path = {}

    def encode(self):
        self._build_path(self._get_tree())
        res = ''
        for el in self.text:
            res += f'{self.path[el]} '
        return res[:-1]

    def _get_tree(self):
        count_s = Counter(self.text)
        sorted_s = deque(sorted(count_s.items(), key=lambda it: it[1]))

        while len(sorted_s) > 1:
            weight = sorted_s[0][1] + sorted_s[1][1]
            node = Node(left_child=sorted_s.popleft()[0], right_child=sorted_s.popleft()[0])

            for i, item in enumerate(sorted_s):
                if weight > item[1]:
                    continue
                else:
                    sorted_s.insert(i, (node, weight))
                    break
            else:
                sorted_s.append((node, weight))

        return sorted_s[0][0]

    def _build_path(self, tree, path=''):
        if not isinstance(tree, Node):
            self.path[tree] = path
        else:
            self._build_path(tree.left_child, path=f'{path}0')
            self._build_path(tree.right_child, path=f'{path}1')


print(HuffmanTree('beep boop beer!').encode())
