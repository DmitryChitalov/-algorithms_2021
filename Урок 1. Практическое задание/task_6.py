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


class QueueTasks:

    # Список задач
    complete_tasks = []

    @staticmethod
    def get_all_solved():
        print(QueueTasks.complete_tasks)

    # Создание очереди с наименованием
    def __init__(self, name):
        self.queue = []
        self.name = name

    # Создание задачи
    def add_task(self, task):
        return self.queue.insert(0, task)

    # Забрать первую задачу в очереди
    def get_task(self):
        return self.queue.pop()

    # Перенос задачи в другую очередь
    def transfer_task(self, queue):
        return queue.add_task(self.get_task())

    # Вывод очереди на экран
    def get_queue(self):
        print(self.queue)

    # перенос задачи в решенные
    def solve_task(self):
        return QueueTasks.complete_tasks.append(self.get_task())


if __name__ == '__main__':
    tasks_1 = QueueTasks('Базовая очередь')
    tasks_2 = QueueTasks('Очередь на доработку')
    tasks_1.add_task('прочитать войну и мир')
    tasks_1.add_task('прочитать мифы древней греции')
    tasks_1.add_task('прогуляться')
    tasks_1.add_task('сварить борщ')
    tasks_1.add_task('лечь пораньше')
    tasks_1.get_queue()
    tasks_1.transfer_task(tasks_2)
    tasks_2.get_queue()
    tasks_2.solve_task()
    tasks_2.get_queue()
    QueueTasks.get_all_solved()
