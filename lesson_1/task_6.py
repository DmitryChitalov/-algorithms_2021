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


class QueueClass:
    """
    код класса QueueClass из конспекта
    добавлен метод __str__
    """

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def __str__(self):
        if self.size():
            return ', '.join(self.elems)
        return 'нет'


class TaskManagerClass:
    """
    класс для манипулирования задачами в разных очередях
    """

    def __init__(self):
        self.main_queue = QueueClass()
        self.closed_queue = QueueClass()
        self.active_queue = QueueClass()

    def add_task(self, task_name):
        """ добавить задачу в главный список """
        self.main_queue.to_queue(task_name)

    def take_task(self):
        """ взять задачу из главного списка и переместить в активный """
        if not self.main_queue.size():
            return

        task_name = self.main_queue.from_queue()
        self.active_queue.to_queue(task_name)

    def close_task(self):
        """ закрыть задачу """
        if not self.active_queue.size():
            return

        task_name = self.active_queue.from_queue()
        self.closed_queue.to_queue(task_name)

    def __str__(self):
        result = f'главная очередь: {self.main_queue}\n'
        result += f'очередь активных задач: {self.active_queue}\n'
        result += f'очередь закрытых задач: {self.closed_queue}'
        return result


task_manager = TaskManagerClass()

task_manager.add_task('посмотреть лекцию')
task_manager.add_task('изучить конспект')
task_manager.add_task('решить домашнее задание')

print(task_manager)
print('------------------------------------------')

task_manager.take_task()

print(task_manager)
print('------------------------------------------')

task_manager.add_task('изучить pep-8')
task_manager.add_task('прочитать 1 главу книги "Грокаем алгоритмы"')

print(task_manager)
print('------------------------------------------')

task_manager.close_task()
task_manager.take_task()
task_manager.close_task()
task_manager.take_task()
task_manager.close_task()

print(task_manager)
print('------------------------------------------')
