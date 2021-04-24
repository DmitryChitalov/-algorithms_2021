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


class QueueClass:
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


# Класс "доска задач" на основе класса "очередь" с урока
class Kanban:

    def __init__(self):
        self.new_tasks = QueueClass()
        self.ongoing_tasks = QueueClass()
        self.done_tasks = QueueClass()
        self.tasks_to_correct = QueueClass()

    # добавляем новую задачу на доску
    # можно добавить несколько задач одновременно
    def add_new_tasks(self, *args):
        for el in args:
            self.new_tasks.to_queue(el)

    # берём задачу из новых и переносим в выполняемые
    def move_to_ongoing(self):
        if not self.new_tasks.is_empty():
            self.ongoing_tasks.to_queue(self.new_tasks.from_queue())
        else:
            print('Нет новых задач для выполнения')

    # Берём задачу из выполняемых и переносим в завершённые
    def ongoing_to_done(self):
        if not self.ongoing_tasks.is_empty():
            self.done_tasks.to_queue(self.ongoing_tasks.from_queue())
        else:
            print('Нет выполненных задач')

    # Берём задачу из выполненных и переносим на доработку
    def move_to_correct(self):
        if not self.done_tasks.is_empty():
            self.tasks_to_correct.to_queue(self.done_tasks.from_queue())
        else:
            print('Нет задач на корректировку')

    # Берём задачу из доработанных и переносим в завершённые
    def corrected_to_done(self):
        if not self.tasks_to_correct.is_empty():
            self.done_tasks.to_queue(self.tasks_to_correct.from_queue())
        else:
            print('Нет откорректированных задач')

    # Если задача больше не нуждается в доработке, убираем с доски
    def remove_task(self):
        if not self.done_tasks.is_empty():
            self.done_tasks.from_queue()

    # Показывает верхние задачи во всех списках
    def show_tasks(self):
        try:
            print(f'Следующая задача: {self.new_tasks.elems[-1]}')
        except IndexError:
            print('Нет новых задач')
        try:
            print(f'Текущая задача: {self.ongoing_tasks.elems[-1]}')
        except IndexError:
            print('Нет выполняемых задач')
        try:
            print(f'Выполненная задача: {self.done_tasks.elems[-1]}')
        except IndexError:
            print('Нет выполненных задач')
        try:
            print(f'Текущая задача на доработке: {self.tasks_to_correct.elems[-1]}')
        except IndexError:
            print('Нет задач на корректировке')


if __name__ == '__main__':

    kanban = Kanban()
    # добавляем список задач
    kanban.add_new_tasks('t1', 't2', 't3', 'some_other_task', 't4', 't5', 't6')
    # переносим 2 задачи в выполняемые
    kanban.move_to_ongoing()
    kanban.move_to_ongoing()
    # переносим задачу в выполненные
    kanban.ongoing_to_done()
    # возвращаем задачу на корректировку
    kanban.move_to_correct()
    # завершаем ещё одну задачу и возвращаем задачу с коректировки
    kanban.ongoing_to_done()
    kanban.corrected_to_done()
    # выводим текущие задачи
    kanban.show_tasks()
