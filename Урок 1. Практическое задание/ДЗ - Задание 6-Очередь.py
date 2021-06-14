"""
Задание 6.
Задание на закрепление навыков работы с очередью
Реализуйте структуру "ДОСКА ЗАДАЧ".
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

# Очередь создаем аналогично стеку - через использование ООП и списки
class QueueClass: # Класс Очередь. Создаем интерфейс
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item): # Вставка
        self.elems.insert(0, item)

    def from_queue(self): # Удаление
        return self.elems.pop()

    def size(self): # Размер
        return len(self.elems)


class TaskBoard: # Класс "ДОСКА ЗАДАЧ"
    def __init__(self):
        self.cur_queue = QueueClass()    # Базоваяя очередь
        self.revision_queue = QueueClass()   # очередь на доработку
        self.log = []  # Список решенных задач

    def resolve_task(self): # текущая решонная задача
        """Закрываем текущую задачу и добавляем в лог"""
        task = self.cur_queue.from_queue()
        self.log.append(task)

    def to_revision_task(self): # текущая задача в доработку
        """Отправляем текущую задачу на доработку"""
        task = self.cur_queue.from_queue()
        self.revision_queue.to_queue(task)

    def to_current_queue(self, item):
        """Добавляем задачу в текущие"""
        self.cur_queue.to_queue(item)

    def from_revision(self):
        """Возвращаем задачу из доработки в текущую очередь"""
        task = self.revision_queue.from_queue()
        self.cur_queue.to_queue(task)

    def current_task(self):
        """Текущая задача"""
        return self.cur_queue.elems[len(self.cur_queue.elems) - 1]

    def current_revision(self):
        """Задача в доработке"""
        return self.revision_queue.elems[len(self.revision_queue.elems) - 1]

# Клиентский код
if __name__ == '__main__': # Позволяет осуществлять отладку кода, не мешая импортам ниже.
    task_board = TaskBoard()
    task_board.to_current_queue("Task1")
    task_board.to_current_queue("Task2")
    task_board.to_current_queue("Task3")
    print(task_board.cur_queue.elems)
    print(task_board.current_task())
    task_board.to_revision_task()
    task_board.resolve_task()
    task_board.from_revision()
    print(task_board.cur_queue.elems)
    print(task_board.current_task())
    print(task_board.log)
