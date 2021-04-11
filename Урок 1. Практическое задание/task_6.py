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
# Создание Манипулятора со съемными наконечниками (пример работы).
# Тоже долго не могла понять как реализовать задачу, пока не стала искать информацию в сторонних источниках.


class QueueClass:

    def __init__(self):

        self.new_tasks = []
        self.completed_tasks = []
        self.repeat_tasks = []

    def add_task(self, task):

        self.new_tasks.insert(0, task)

    def get_task(self):

        if len(self.new_tasks) > 0:
            return self.new_tasks[-1]
        else:
            return "Задач нет"

    def repeat_task(self):

        if len(self.repeat_tasks) > 0:
            return self.repeat_tasks[-1]
        else:
            return "Задач нет"

    def send_new_task(self):

        self.tasks_to_move = self.new_tasks.pop()
        self.completed_tasks.insert(0, self.tasks_to_move)

    def send_repeat_task(self):

        self.tasks_to_move = self.repeat_tasks.pop()
        self.completed_tasks.insert(0, self.tasks_to_move)

    def send_new_task_to_repeat(self):

        self.tasks_to_move = self.new_tasks.pop()
        self.repeat_tasks.insert(0, self.tasks_to_move)

    def all_list(self):

        return self.new_tasks, self.repeat_tasks, self.completed_tasks


new_tasks_dispatcher = QueueClass()

print(new_tasks_dispatcher.get_task())

new_tasks_dispatcher.add_task("Создать 3Д модели основной части манипулятора")

new_tasks_dispatcher.add_task("Создать 3Д модели съемной части манипулятора")

new_tasks_dispatcher.add_task("Закупить материалы")

new_tasks_dispatcher.add_task("Собрать основную часть манипулятора")

new_tasks_dispatcher.add_task("Собрать съемную часть манипулятора")

new_tasks_dispatcher.add_task("Соединить все части")

print(new_tasks_dispatcher.get_task())

print(new_tasks_dispatcher.all_list())

print(new_tasks_dispatcher.all_list())

new_tasks_dispatcher.send_new_task_to_repeat()

print(new_tasks_dispatcher.all_list())

print(new_tasks_dispatcher.repeat_task())

new_tasks_dispatcher.send_repeat_task()

print(new_tasks_dispatcher.all_list())

new_tasks_dispatcher.send_new_task()

print(new_tasks_dispatcher.all_list())
