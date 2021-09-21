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


class TaskBoard:

    def __init__(self):
        self.main = []
        self.revision = []
        self.resolved = []

    def add_task(self, item, in_stack='main'):
        if in_stack == 'main':
            self.main.append(item)
        elif in_stack == 'revision':
            self.revision.append(item)

    def take_task(self, in_stack='main'):
        if in_stack == 'main' and self.main:
            print(self.main.pop(-1))
        elif in_stack == 'revision' and self.revision:
            print(self.revision.pop(-1))
        else:
            print('No assignments available')

    def submit_task(self, item):
        self.resolved.append(item)

    def check_task(self, in_stack='main', number=0):
        if in_stack == 'main' and self.main:
            print(f'Task {len(self.main) - number} : {self.main[-1 - number]}')
        elif in_stack == 'revision' and self.revision:
            print(f'Task {len(self.revision) - number} : {self.revision[-1 - number]}')
        elif in_stack == 'resolved':
            print(f'Task {len(self.resolved) - number} : {self.resolved[-1 - number]}')
        else:
            print('No assignments available')


if __name__ == '__main__':

    tasks = TaskBoard()

    for num in range(6):
        tasks.add_task(num)

    for num in range(6):
        tasks.check_task()
        tasks.take_task()

    tasks.submit_task(5)

    for num in range(5):
        tasks.add_task(num, 'revision')

