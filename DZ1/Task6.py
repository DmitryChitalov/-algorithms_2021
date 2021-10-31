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


class Queue:
    def __init__(self):
        self.stack = []

    def __str__(self):
        s = ' '
        for el in self.stack:
            s += el.__str__() + ' '
        return s + '\n'

    def empty(self):
        return (len(self.stack) == 0)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.empty():
            return None
        else:
            return self.stack.pop(0)


class TaskTable:
    def __init__(self):
        self.current = Queue()
        self.solved = Queue()
        self.revision = Queue()

    def __str__(self):
        s = ''
        s = "Current: " + self.current.__str__()
        s += "Solved: " + self.solved.__str__()
        s += "Revision: " + self.revision.__str__()
        return s + '\n'

    def AddTask(self, task):
        self.current.push(task)

    def SolveTask(self):
        if not self.current.empty():
            self.solved.push(self.current.pop())
        else:
            print('Add task, please')

    def SolveRevision(self):
        if not self.revision.empty():
            self.solved.push(self.revision.pop())
        else:
            print('No task on revision')

    def AddRevision(self):
        if not self.current.empty():
            self.revision.push(self.current.pop())
        else:
            print('Add task please')

    def DeleteTask(self):
        if not self.solved.empty():
            self.solved.pop()


test = TaskTable()

for i in range(20):
    test.AddTask(i)
print(test)

for i in range(5):
    test.SolveTask()
print(test)

for i in range(9):
    test.AddRevision()
print(test)

for i in range(3):
    test.SolveRevision()
print(test)

for i in range(4):
    test.DeleteTask()
print(test)
