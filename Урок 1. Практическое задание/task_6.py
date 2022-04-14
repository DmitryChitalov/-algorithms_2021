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

class DashBoard:
    def __init__(self):
        self.queue_main = []
        self.queue_for_revision = []
        self.done_list = []

    def is_empty(self):
        return self.queue_main == []

    def is_empty_revision(self):
        return self.queue_for_revision == []

    def to_queue(self, item):
        return self.queue_main.insert(0, item)

    def see_tasks(self):
        return '\n'.join(self.queue_main)

    def see_solved_tasks(self):
        return '\n'.join(self.done_list)

    def see_revision_tasks(self):
        return '\n'.join(self.queue_for_revision)

    def try_to_solve(self):
        if self.queue_main == []:
            print("It doesn't have tasks")
            return None
        if input("You need to input True or False decision statement: ") == 'True':
            self.done_list.append(self.queue_main.pop())
            print('Task done!')
            return None
        else:
            self.queue_for_revision.insert(0, self.queue_main.pop())
            print('Task needs a revision')

    def try_to_solve_revision(self):
        if self.queue_for_revision == []:
            print("Revision doesn't have tasks")
            return None
        if input("You need to input True or False decision statement: ")  == 'True':
            self.done_list.append(self.queue_for_revision.pop())
            print('Task done!')
            return None
        else:
            self.queue_for_revision.insert(0, self.queue_for_revision.pop())
            print('Task needs a revision again')


if __name__ == '__main__':
    qc_obj = DashBoard()

    print(qc_obj.is_empty())  # True

    # Наполним очередь задачами
    qc_obj.to_queue('task_1')
    qc_obj.to_queue('task_2')
    qc_obj.to_queue('task_3')
    qc_obj.to_queue('task_4')
    qc_obj.to_queue('task_5')
    qc_obj.to_queue('task_6')
    qc_obj.to_queue('task_123')
    qc_obj.to_queue('task_1996')

    print(qc_obj.is_empty())  # False

    # посмотреть список задач
    print(qc_obj.see_tasks())

    # обработать пару задач
    qc_obj.try_to_solve()
    qc_obj.try_to_solve()
    qc_obj.try_to_solve()

    # посмотреть список решенных задач
    print(qc_obj.see_solved_tasks())

    # посмотреть список задач
    print(qc_obj.see_tasks())

    # проверить пустой ли список задач на ревизии
    print(qc_obj.is_empty())

    # посмотреть список задач на ревизии
    print(qc_obj.see_revision_tasks())

    # обработать пару задач на ревизии
    qc_obj.try_to_solve_revision()
    qc_obj.try_to_solve_revision()

    # посмотреть список задач на ревизии
    print(qc_obj.see_revision_tasks())