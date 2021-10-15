from collections import Counter, deque


class HaffMan:

    def __init__(self, my_str):
        self.my_str = my_str
        self.code_table = dict()

    def __str__(self):
        self.haffman_code(self.make_tree())
        result = ''
        for i in self.my_str:
            result += f'{self.code_table[i]} '
        return result

    def make_tree(self):
        string_deque = deque(sorted(Counter(self.my_str).items(), key=lambda item: item[1]))

        if len(string_deque) != 1:

            while len(string_deque) > 1:
                weight = string_deque[0][1] + string_deque[1][1]
                comb = {0: string_deque.popleft()[0],
                        1: string_deque.popleft()[0]}

                for ind, count in enumerate(string_deque):
                    if weight > count[1]:
                        continue
                    else:
                        string_deque.insert(ind, (comb, weight))
                        break
                else:
                    string_deque.append((comb, weight))

        else:
            weight = string_deque[0][1]
            comb = {0: string_deque.popleft()[0], 1: None}
            string_deque.append((comb, weight))
        return string_deque[0][0]

    def haffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.haffman_code(tree[0], path=f'{path}0')
            self.haffman_code(tree[1], path=f'{path}1')


if __name__ == '__main__':
    obj = HaffMan('beep boop beer!')
    print(obj.my_str)
    print(obj)
