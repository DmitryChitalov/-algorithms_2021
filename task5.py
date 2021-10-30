class Stack:
    def __init__(self):
        self.stack = []
        self.max = 5

    def empty_table(self):
        return self.stack == []

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        if len(self.stack) == 0:
            self.max = None
        elif removed == self.max:
            self.max = self.stack[0]
            for value in self.stack:
                if value > self.max:
                    self.max = value
        return removed

    def push(self, item):
        if len(self.stack) <= self.max:
            self.stack.append(item)
        else:
            print('Стек полон')

    def get_max(self):
        return self.max

    def full(self):
        return len(self.stack) == self.max


def new_stack():
    return Stack()

