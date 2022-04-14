"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие нескольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class DashBoard:
    def __init__(self):
        self.__base = []
        self.__in_work = []
        self.__to_fix = []
        self.__done = []

    def is_empty(self):
        return self.__base == []

    def create_new_task(self, item):
        self.__base.append(item)

    def task_to_work(self):
        if self.__base:
            self.__in_work.append(self.__base.pop(0))
            return f'The task {self.__in_work[-1]} accepted for work'
        return 'All tasks are in work or done'

    def task_to_fix(self):
        if self.__in_work:
            self.__to_fix.append(self.__in_work.pop(0))
            return f'The task {self.__to_fix[-1]} is accepted for revision'
        return 'No tasks in this queue'

    def task_to_done(self, queue):
        msg = 'Good job!'
        if queue == 'work' and self.__in_work:
            self.__done.append(self.__in_work.pop(0))
        elif queue == 'fix' and self.__to_fix:
            self.__done.append(self.__to_fix.pop(0))
        else:
            msg = 'Something wrong'
        return msg

    def size(self):
        return len(self.__base)


if __name__ == '__main__':
    dashboard = DashBoard()
    print(dashboard.is_empty())
    for i in range(1, 11):
        dashboard.create_new_task(i)
    for i in range(10):
        print(dashboard.task_to_work())
    for i in range(10):
        if i % 2 == 0:
            print(dashboard.task_to_fix())
        else:
            print(dashboard.task_to_done('work'))
    print(dashboard.size())
