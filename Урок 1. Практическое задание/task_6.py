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


class Board:
    def __init__(self):
        self.base_queue = []
        self.revision_queue = []
        self.resolved = []

    def is_empty(self, name_queue):
        if name_queue == "base_queue":
            return self.base_queue == []
        elif name_queue == "revision_queue":
            return self.revision_queue == []
        else:
            return self.resolved == []

    def to_base_queue(self, item):
        self.base_queue.insert(0, item)

    def from_base_queue(self):
        self.resolved.append(self.base_queue.pop())
        return self.resolved[len(self.resolved) - 1]

    def size(self):
        return f"base_queue: {len(self.base_queue)} | " \
               f"revision_queue: {len(self.revision_queue)} | " \
               f"resolved: {len(self.resolved)}"

    def to_revision_queue(self):
        self.revision_queue.insert(0, self.base_queue.pop())
        return self.revision_queue[0]

    def from_revision_queue(self):
        self.base_queue.insert(0, self.revision_queue.pop())
        return self.base_queue[0]


obj = Board()
# базовая очередь задач пустая
print(obj.is_empty("base_queue"))
# помещаем объекты в очередь
obj.to_base_queue("task1")
obj.to_base_queue("task2")
obj.to_base_queue("task3")
obj.to_base_queue("task4")
# базовая очередь задач пустая
print(obj.is_empty("base_queue"))
# кол-во задач на доске
print(obj.size())
# решаем одну задачу
print(obj.from_base_queue())
# обновляем кол-во задач на доске
print(obj.size())
# отправляем задачу на доработку
print(obj.to_revision_queue())
# обновляем кол-во задач на доске
print(obj.size())
# возвращаем задачу в конец очередь после доработки
print(obj.from_revision_queue())
# обновляем кол-во задач на доске
print(obj.size())
# базовая очередь задач
print(obj.base_queue)
