"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class TaskBord:
    def __init__(self):
        self.basic_task = []
        self.completed_task = []
        self.revision_task = []

    def adding(self, task):
        self.basic_task.insert(0, task)

    def complete(self):
        self.completed_task.insert(0, self.basic_task.pop())

    def complete_revision(self):
        self.completed_task.insert(0, self.revision_task.pop())

    def revision(self):
        self.revision_task.insert(0, self.basic_task.pop())

    def show_basic_tasks(self):
        return len(self.basic_task)

    def show_all_in_work_tasks(self):
        return self.basic_task, self.revision_task

    def show_completed(self):
        return self.completed_task


if __name__ == '__main__':

    Task = TaskBord()
    Task.adding(1)
    Task.adding(2)
    Task.adding(3)
    Task.adding(4)
    Task.adding(5)
    Task.adding(6)
    Task.adding(7)
    Task.adding(8)
    print(Task.show_basic_tasks(), ' Всего заданий')
    Task.complete()
    Task.complete()
    print(Task.show_basic_tasks(), ' осталось заданий')
    Task.revision()
    Task.revision()
    print(Task.show_all_in_work_tasks(), ' основные задания и на доработке')
    Task.complete_revision()
    print(Task.show_all_in_work_tasks(), ' основные задания и на доработке')
    print(Task.show_completed(), ' задания выполнены')
