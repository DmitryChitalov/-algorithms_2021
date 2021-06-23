class QueueClass:
    def __init__(self):
        self.elems = []

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:
    def __init__(self):
        self.actual = QueueClass()
        self.remade = QueueClass()
        self.done = []

    def input_task(self, item):
        self.actual.to_queue(item)

    def task_done(self):
        end_task = self.actual.from_queue()
        self.done.append(end_task)

    def to_remade(self):
        remade_task = self.actual.from_queue()
        self.remade.to_queue(remade_task)

    def actual_print(self):
        """Вывод задач в актуальном порядке, т.е. в реверсе"""
        new_str = reversed(self.actual.elems)
        return list(new_str)

    def to_do_now(self):
        """Печатает задачу, которую надо выполнить"""
        return self.actual.elems[-1]


my_task_board = TaskBoard()
my_task_board.input_task('Встань')
my_task_board.input_task('Иди')
my_task_board.input_task('Неси добро')

print(my_task_board.actual.elems)
print(my_task_board.actual_print())
print(my_task_board.to_do_now())

my_task_board.to_remade()
my_task_board.task_done()

print(my_task_board.actual.elems)
print(my_task_board.remade.elems)
print(my_task_board.done)
