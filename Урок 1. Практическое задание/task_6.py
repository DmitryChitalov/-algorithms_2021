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


class Turn:
    def __init__(self):
        self.tasks = []
        self.debagging = []
        self.compleated = []

    def add_task(self, task):
        self.tasks.append(task)

    def finish(self):
        self.compleated.append(self.tasks.pop(0))

    def debagging(self):
        self.debagging.append(self.tasks.pop(0))

    def show(self):
        print(f'tasks: {self.tasks}', f'debagging: {self.debagging}', f'compleated: {self.compleated}', sep='\n')





if __name__ == '__main__':
    obj = Turn()
    obj.show()