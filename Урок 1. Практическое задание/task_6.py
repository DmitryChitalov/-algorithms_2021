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


class Queue:
    """Реализация структуры данных очередь"""

    def __init__(self):
        self.queue = list()

    def is_empty(self):
        return self.queue == []

    def add(self, element):
        self.queue.insert(0, element)

    def pop(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def get_element(self):
        return self.queue[len(self.queue) - 1]


class TaskBoard:
    """Реализация класса доска задач. Класс содержит очередь:
    список предстоящих задач - to_do_tasks.
    in_progress - поле содержашее активную задачу, над которой в данный момент ведется работа.
    done_task - последняя завершенная задача.
    """

    def __init__(self):
        self.to_do_tasks = Queue()
        self.in_progress = ""
        self.done_task = ""

    def add_new_task(self, _task):
        """Наполнение очереди задач"""
        self.to_do_tasks.add(_task)

    def start_task(self):
        """перевод задачи из очереди to_do_tasks в активнй статус. Начало работы над задачей"""
        if self.in_progress == "":
            self.in_progress = self.to_do_tasks.pop()
            print(f"Начинаем работать над задачей: {self.in_progress}")
        else:
            print(f"Нельзя начать следующую задачу, пока есть незавершенные: {self.in_progress}")

    def complete_task(self):
        """Завершение работы над задаей. Задача переводится в статус завершена.
        Активная задача очищается"""
        if not self.in_progress == "":
            self.done_task = self.in_progress
            self.in_progress = ""
            print(f"завершена задача {self.done_task}")
        else:
            print("Нет начатых и незавершеннх задач. Начните работу над следующей задачей")

    def get_next_new_task(self):
        """Вывод следующей задаче в очереди to_do_tasks"""
        return print(f"--{self.to_do_tasks.get_element()}") \
            if not self.to_do_tasks.is_empty() else print("Нет новых задач")

    def get_current_task(self):
        """Вывод активной задачи"""
        return print(f"--{self.in_progress}") if not self.in_progress == "" else print(
            "Нет незавершенных задач")

    def get_last_accomplished_task(self):
        """вывод последней завершенной задачи"""
        return print(f"--{self.done_task}") if not self.done_task == "" else print(
            "Вы не закончили ни одной задачи")


def get_status():
    """Вывод статуса. Активная задача, следующая задача, последняя завершенная задача"""
    print("*" * 30)
    print("Статус текущих задач:")
    print("*" * 30)
    print("активная задача: ")
    tb.get_current_task()
    print("последняя завершенная задача:")
    tb.get_last_accomplished_task()
    print("следующая задача:")
    tb.get_next_new_task()
    print("*" * 30)


tasks = ["вымыть посуду", "сделать уроки", "проаылесосить",
         "вытереть пыль", "сходить в магазин", "погулять",
         "поиграть", "посмотреть кино"]

tb = TaskBoard()

for task in tasks:
    tb.add_new_task(task)

get_status()

tb.start_task()
tb.complete_task()

get_status()

tb.start_task()
tb.start_task()
tb.complete_task()
get_status()

tb.start_task()
get_status()
