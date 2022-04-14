
class QueueClass:
    def __init__(self):
        self.base = []
        self.rev = []

    def push_base(self, el):
        self.base.insert(0, el)

    def pop_out_base(self):
        return self.base.pop()

    def push_rev(self):
        self.rev.insert(0, self.pop_out_base())

    def pop_out_rev(self):
        self.base.insert(0, self.rev.pop())

    def size_base(self):
        return len(self.base)

    def size_rev(self):
        return len(self.rev)

    def get_all(self):
        return '{} - basic, where tasks are taken from, ' \
               'solved and sent to the lis of solved; {} - turn of reversion'.format(self.base, self.rev)


start = QueueClass()
start.push_base(1)
start.push_base(2)
start.push_base(3)
print(start.size_base())

start.push_rev()
print(start.get_all())
print(start.size_rev())
start.pop_out_rev()
start.pop_out_base()
print(start.get_all())
