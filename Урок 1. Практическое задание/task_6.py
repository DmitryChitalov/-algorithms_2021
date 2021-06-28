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
        self.basicq = []  # очередь на обработку
        self.workflowq = []  # очередь в работе
        self.corrq = []  # очередь на исправление
        self.doneq = []  # очередь закрытых задач

    def add_task(self, task):
        if task == '':
            return None
        self.basicq.insert(0, task)

    def proc_task(self):
        if len(self.basicq) == 0:
            return None
        self.workflowq.insert(0, self.basicq.pop())

    def redo_task(self):
        if len(self.workflowq) == 0:
            return None
        self.corrq.insert(0, self.workflowq.pop())

    def end_task(self):
        if len(self.workflowq) == 0:
            return None
        self.doneq.insert(0, self.workflowq.pop())

    def end_redo_task(self):
        if len(self.corrq) == 0:
            return None
        self.doneq.insert(0, self.corrq.pop())

    def delete_task(self):
        if len(self.doneq) == 0:
            return None
        self.doneq.pop()

    def show(self):
        print('//--------------------------------')
        print('Добавленные задачи:')
        print(', '.join(self.basicq), '\n')
        print('Задачи в работе:')
        print(', '.join(self.workflowq), '\n')
        print('Задачи на доработке:')
        print(', '.join(self.corrq), '\n')
        print('Завершенные задачи:')
        print(', '.join(self.doneq), '\n')


myworkflow = TaskBoard()
myworkflow.add_task('Придумать концепт')
myworkflow.add_task('Написать движок')
myworkflow.add_task('Нарисовать дизайн')
myworkflow.add_task('Запрограммировать логику')
myworkflow.add_task('Задизайнить мир')
myworkflow.add_task('Собрать проект')
myworkflow.add_task('Протестировать')
myworkflow.add_task('Выпустить на рынок')
myworkflow.add_task('Запустить рекламную компанию')
myworkflow.add_task('Передраться за долю акций')
myworkflow.add_task('Отпраздновать')
myworkflow.show()

myworkflow.proc_task()
myworkflow.end_redo_task()
myworkflow.show()
myworkflow.proc_task()
myworkflow.proc_task()
myworkflow.proc_task()
myworkflow.show()
myworkflow.redo_task()
myworkflow.redo_task()
myworkflow.show()

myworkflow.end_task()
myworkflow.end_task()
myworkflow.end_task()
myworkflow.end_redo_task()
myworkflow.end_redo_task()
myworkflow.show()

myworkflow.proc_task()
myworkflow.proc_task()
myworkflow.proc_task()
myworkflow.show()

myworkflow.proc_task()
myworkflow.proc_task()
myworkflow.end_task()
myworkflow.end_task()
myworkflow.end_task()
myworkflow.end_task()
myworkflow.show()

myworkflow.delete_task()
myworkflow.delete_task()
myworkflow.delete_task()
myworkflow.delete_task()
myworkflow.delete_task()
myworkflow.delete_task()
myworkflow.delete_task()
myworkflow.delete_task()
myworkflow.end_task()
myworkflow.proc_task()
myworkflow.proc_task()
myworkflow.show()

myworkflow.end_task()
myworkflow.end_task()
myworkflow.show()

myworkflow.delete_task()
myworkflow.delete_task()
myworkflow.delete_task()
myworkflow.show()