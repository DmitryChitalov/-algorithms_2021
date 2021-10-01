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
        self.current_tasks = []
        self.finish_tasks = []
        self.tasks_on_modify = []

    def push_task(self, task):
        self.current_tasks.append(task)

    def show_next_task(self):
        print(f'Задача: {self.current_tasks[0]}')
        while True:
            status = input('Укажите статус задачи: 1 - Задача решена 2 - Отправить задачу на доработку')
            if status == '1':
                self.finish_tasks.append(self.current_tasks.pop(0))
                break
            elif status == '2':
                self.tasks_on_modify.append(self.current_tasks.pop(0))
                break
            else:
                print('Не корректный ввод статуса!')

    def finish(self):
        return self.finish_tasks

    def modify(self):
        return self.tasks_on_modify

    def all_current(self):
        return self.current_tasks
