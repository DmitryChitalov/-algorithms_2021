"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются #revision
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class Desc:
    def __init__(self):
        self.task_list = []
        self.turn_list = []

    def task_append(self, task_text):
        if len(self.task_list) == 0:
            self.task_list.append([task_text])
        elif len(self.task_list[len(self.task_list) - 1]) > 0:
            self.task_list.append([task_text])

    def do_task(self, status):
        if status == 'ready':
            self.task_list.pop([0][0])
        if status == 'revision':
            self.task_list[0].append('revision')
            self.turn_list.append(self.task_list[0])


Object_desk = Desc()
Object_desk.task_append('create file')
Object_desk.task_append('print hello world')
Object_desk.do_task('ready')
Object_desk.do_task('revision')
print(Object_desk.task_list)
print(Object_desk.turn_list)
