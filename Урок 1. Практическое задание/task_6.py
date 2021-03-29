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


class TaskBoard:
    """Класс структуры"""
    def __init__(self):
        self.__solved = []  # Список решенных задач
        self.__basic = Queue()  # Очередь решаемых задач
        self.__revision = Queue()  # Очередь на доработку

    def add_task(self, task):
        """Добавляет задачу в список решаемых"""
        self.__basic.add(task)

    def move_to_revision(self):
        """Перемещает последнюю задачу из решаемых на доработку"""
        self.__revision.add(self.__basic.remove())

    def move_to_solved(self):
        """Перемещает последнюю задачу из решаемых в решенные"""
        self.__solved.append(self.__basic.remove())

    def complete_revision(self):
        """Перемещает последнюю задачу из списка на дорабоке в решенные"""
        self.__solved.append(self.__revision.remove())

    def __str__(self):
        return 'Решаемые задачи: ' + str(self.__basic) + '\nЗадачи на доработку: ' + str(self.__revision) + \
               '\nЗавершенные задачи: ' + ', '.join(self.__solved) + '\n'


class Queue:
    """Класс очереди"""
    def __init__(self):
        self.__lst = []

    def add(self, element):
        """Добавляет элемент в очередь"""
        self.__lst.insert(0, element)

    def remove(self):
        """Убирает элемент из очереди"""
        return self.__lst.pop()

    def __len__(self):
        """Возвращает длину очереди"""
        return len(self.__lst)

    def __str__(self):
        return ', '.join(reversed(self.__lst))


task_board = TaskBoard()

task_board.add_task('собрать команду')
task_board.add_task('придумать план')
print(task_board)

task_board.move_to_revision()
print(task_board)

task_board.add_task('назначить встречу')
task_board.move_to_solved()
print(task_board)

task_board.complete_revision()
task_board.move_to_solved()
print(task_board)
