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


class TaskQueue:
    def __init__(self):
        self.tasks = []

    def is_empty(self):
        return self.tasks == []

    def add_task(self, item):
        self.tasks.insert(0, item)

    def remove_task(self):
        return self.tasks.pop()

    def get_size(self):
        return len(self.tasks)

    def get_all_tasks(self):
        return self.tasks


if __name__ == '__main__':
    all_tasks = TaskQueue()
    completed_tasks = TaskQueue()
    tasks_for_completion = TaskQueue()


    def set_task_status(is_completed=True):
        completed_tasks.add_task(all_tasks.remove_task()) if is_completed else tasks_for_completion.add_task(
            all_tasks.remove_task())


    for i in range(50):
        all_tasks.add_task(i)

    print(f'Было: {all_tasks.get_all_tasks()}')

    set_task_status()
    set_task_status()
    set_task_status(False)
    set_task_status()
    set_task_status(False)
    set_task_status()
    set_task_status()
    set_task_status()
    set_task_status(False)
    set_task_status(False)
    set_task_status(False)
    set_task_status(False)
    set_task_status()
    set_task_status()
    set_task_status()
    set_task_status(False)
    set_task_status()

    print(f'Стало: {all_tasks.get_all_tasks()}')
    print(f'Выполненные: {completed_tasks.get_all_tasks()}')
    print(f'На доработку: {tasks_for_completion.get_all_tasks()}')
