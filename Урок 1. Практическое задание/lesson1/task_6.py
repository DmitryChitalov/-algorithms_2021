class QueueClass:
    def __init__(self):
        self.elems = []

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
        self.basic = QueueClass()
        self.modified = QueueClass()
        self.resolved = []

    def current_task(self):
        return self.basic.elems[len(self.basic.elems) - 1]

    def current_revision(self):
        return self.modified.elems[len(self.modified.elems) - 1]

    def to_current_tasks(self, item):
        self.basic.to_queue(item)

    def resolved_tasks(self):
        task = self.basic.from_queue()
        self.resolved.append(task)

    def to_revision(self):
        task = self.basic.from_queue()
        self.modified.to_queue(task)

    def from_revision(self):
        task = self.modified.from_queue()
        self.basic.to_queue(task)


task_board = TaskBoard()
task_board.to_current_tasks('task1')
task_board.to_current_tasks('task2')

print(task_board.basic.elems)
print(task_board.current_task())

task_board.to_revision()

print(task_board.modified.elems)
print(task_board.current_revision())

task_board.from_revision()

print(task_board.basic.elems)

task_board.resolved_tasks()

print(task_board.basic.elems)
print(task_board.resolved)
