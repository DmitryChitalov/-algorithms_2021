class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def tasks_count(self):
        return len(self.elems)

    def add_to_line(self, item):
        self.elems.insert(0, item)

    def remove_from_line(self):
        return self.elems.pop()


class Tasks:
    def __init__(self):
        self.current_line = QueueClass()
        self.revision_line = QueueClass()
        self.solved_tasks = []

    def complete_task(self):
        task = self.current_line.remove_from_line()
        self.solved_tasks.append(task)

    def to_revision_line(self):
        task = self.current_line.remove_from_line()
        self.revision_line.add_to_line(task)

    def to_current_line(self, item):
        self.current_line.add_to_line(item)

    def from_revision_line(self):
        task = self.revision_line.remove_from_line()

    def current_task(self):
        return self.current_line.elems[len(self.current_line.elems) - 1]


if __name__ == '__main__':
    tasks = Tasks()
    new_line = QueueClass()
    new_line.add_to_line('task_1')
    new_line.add_to_line('task_2')
    new_line.add_to_line('task_3')
    new_line.add_to_line('task_4')
    new_line.add_to_line('task_5')
    print(new_line.is_empty())
    new_line.remove_from_line()
    print(new_line.tasks_count())
    new_line.remove_from_line()
    print(new_line.tasks_count())

