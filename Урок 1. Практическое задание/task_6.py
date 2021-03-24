"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def to_queue(self, item):
        self.elements.insert(0, item)

    def from_queue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

class TaskBoard:
    def __init__(self):
        self.todo = Queue()
        self.in_progress = Queue()
        self.verify = Queue()
        self.done = Queue()

# Добавить работу в очередь todo
    def to_todo(self, job):
        self.todo.to_queue(job)

# Добавить работу в очередь in progress
    def to_in_progress(self):
        if self.todo.is_empty():
            return False
        else:
            job = self.todo.from_queue()
            self.in_progress.to_queue(job)
            return True

# Добавить работу в очередь verify
    def to_verify(self):
        if self.in_progress.is_empty():
            return False
        else:
            job = self.in_progress.from_queue()
            self.verify.to_queue(job)
            return True

# Добавить работу в очередь done
    def to_done(self):
        if self.verify.is_empty():
            return False
        else:
            job = self.verify.from_queue()
            self.done.to_queue(job)
            return True

# Отправить работу на доработку (из verify в todo)
    def to_rework(self):
        if self.verify.is_empty():
            return False
        else:
            job = self.verify.from_queue()
            self.todo.to_queue(job)
            return True

my_jobs = TaskBoard()

print('Есть что-нибудь в очереди verify?', my_jobs.to_verify())
my_jobs.to_todo('Job 1')
my_jobs.to_todo('Job 2')
my_jobs.to_todo('Job 3')
my_jobs.to_todo('Job 4')
my_jobs.to_in_progress() # Job 1 to in progress
my_jobs.to_in_progress() # Job 2 to in progress
my_jobs.to_in_progress() # Job 3 to in progress
my_jobs.to_verify() # Job 1 to verify
my_jobs.to_verify() # Job 2 to verify
my_jobs.to_done() # Job 1 to done
my_jobs.to_rework() # Job 2 to begin of to do
print(my_jobs.todo.elements)
print(my_jobs.in_progress.elements)
print(my_jobs.verify.elements)
print(my_jobs.done.elements)
