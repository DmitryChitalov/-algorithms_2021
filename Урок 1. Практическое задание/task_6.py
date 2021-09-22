class QueueClass:
    def __init__(self):
        self.base = []
        self.revision = []
        self.resolve = []

    def is_empty(self):
        return f'Основная очередь пуста: {self.base == []} \n' \
               f'Очередь на доработку пуста: {self.revision == []}'

    def to_base(self, item):
        self.base.insert(0, item)

    def to_revision(self):
        self.revision.insert(0, self.base.pop())

    def from_base(self):
        self.resolve.insert(0, self.base.pop())
        return self.resolve

    def from_revision(self):
        self.resolve.insert(0, self.revision.pop())
        return self.resolve

    def size(self):
        return f'Base queue: {len(self.base)} \n'\
               f'Resolved queue: {len(self.resolve)} \n'\
               f'Revision queue: {len(self.revision)}'


if __name__ == '__main__':
    test = QueueClass()
    print(test.is_empty())

    test.to_base('my_obj')
    test.to_base(5)
    test.to_base(True)
    test.to_revision()

    print(test.is_empty())
    print(test.size())
    print(test.from_base())
    print(test.size())
