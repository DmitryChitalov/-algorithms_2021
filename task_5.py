
class Stack:
    def __init__(self, n):
        self.items = []
        self.n = n

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.item = item
        if len(self.items) > self.n:
            self.items[len(self.items) - 1].append(self.item)
        elif len(self.items) == self.n:
            self.items.insert(len(self.items), [self.item])
        else:
            self.items.append(self.item)

    def pop(self):
        if len(self.items) > self.n:
            self.items[len(self.items) - 1].pop()
        else: self.items.pop()

    def size(self):
        return len(self.items)

    def fullStack(self):
        return self.items


stack = Stack(4)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(9)
stack.pop()
stack.push(99)
stack.push(999)
stack.push(77)
print(stack.fullStack())
stack.pop()
print(stack.size())
print(stack.fullStack())
