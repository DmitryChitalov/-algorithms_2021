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


class MyDesk:

    def __init__(self, taskname):
        number_tasks = ++ 1
        self.id_task = number_tasks
        self.name = taskname
        self.status = 'watching'
        watching_queue.append(self.name)
        print('Create new task ' + self.name)

    def change_status(self, userstatus):
        if userstatus == 'complete':
            watching_queue.remove(self.name)
            complete_stack.append(self.name)
        elif userstatus == 'resolve':
            watching_queue.remove(self.name)
            resolve_stack.append(self.name)
        elif userstatus == 'in_work']:
            self.status = userstatus
            print(self.name + ' status changed to ' + userstatus);
        else:
            print('status incorrect');


task1 = MyDesk('task1')
task2 = MyDesk('task2')
task1.change_status('complete')
print(getattr(task1, 'status'), getattr(task1, 'id_task'))
print(getattr(task2, 'status'), getattr(task2, 'id_task'))
