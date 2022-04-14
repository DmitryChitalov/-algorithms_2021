"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
class QueueTasks:
    def __init__(self):
        self.elems = [[]]

    def size(self):
        return len(self.elems)

    def base_queue(self, item):
        self.elems[0].insert(0, item)

    def revision_queue(self, item):
        if self.size() == 1:
            self.elems.append([])
            self.elems[1].insert(0, item)
        else:
            self.elems[1].insert(0, item)

    def solved_queue(self, item):
        if self.size() < 3:
            if self.size() == 1:
                self.elems.append([])
            self.elems.append([])
            self.elems[2].insert(0, item)
        else:
            self.elems[2].insert(0, item)

    def base_to_revision(self):
        self.revision_queue(self.elems[0].pop())

    def base_to_solved(self):
        self.solved_queue(self.elems[0].pop())

    def revision_to_base(self):
        self.base_queue(self.elems[1].pop())

    def from_solved(self):
        self.elems[2].pop()

    def tasks_count(self):
        count = 0
        for que in self.elems:
            count = len(que)
        return count

    def print_base_tasks(self):
        print(f'base_tasks: ')
        for i in self.elems[0]:
            print(i)

    def print_revision_tasks(self):
        print(f'revision_tasks: ')
        for i in self.elems[1]:
            print(i)

    def print_solved_tasks(self):
        print(f'solved_tasks: ')
        for i in self.elems[2]:
            print(i)


tasks = QueueTasks()
tasks.base_queue('task_1')
tasks.base_queue('task_2')
tasks.base_queue('task_3')
tasks.base_queue('task_4')
tasks.base_queue('task_5')
tasks.print_base_tasks()
tasks.base_to_revision()
tasks.print_revision_tasks()
tasks.base_to_solved()
tasks.print_solved_tasks()
