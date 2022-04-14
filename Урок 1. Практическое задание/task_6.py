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


class KanbanElements:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def in_section(self, item):
        self.items.append(item)

    def from_section(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Kanban:
    def __init__(self):
        self.to_do = KanbanElements()            # Kanban To-Do Section
        self.in_progress = KanbanElements()      # Kanban In-progress section
        self.testing = KanbanElements()          # Kanban Testing section
        self.done = []                           # Kanban Done section

    def new_task(self, item):
        self.to_do.in_section(item)

    def task_in_progress(self):
        self.in_progress.in_section(self.to_do.from_section())

    def task_in_testing(self):
        self.testing.in_section(self.in_progress.from_section())

    def repeat_task(self):
        self.in_progress.in_section(self.testing.from_section())

    def task_done(self):
        self.done.append(self.testing.from_section())


if __name__ == '__main__':
    kanban = Kanban()
    kanban.new_task('Task_1')
    kanban.new_task('Task_2')
    kanban.new_task('Task_3')
    kanban.new_task('Task_4')
    kanban.new_task('Task_5')
    kanban.task_in_progress()
    kanban.task_in_progress()
    kanban.task_in_progress()
    kanban.task_in_testing()
    kanban.task_in_testing()
    kanban.task_done()
    kanban.repeat_task()
    print(f'New tasks: {kanban.to_do.items}\n'
          f'Tasks in progress: {kanban.in_progress.items}\n'
          f'Tasks in testing: {kanban.testing.items}\n'
          f'Completed tasks: {kanban.done}')
