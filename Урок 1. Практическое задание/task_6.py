"""
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие нескольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class Task:
    def __init__(self, name, description, board, queue):
        self.name = name
        self.description = description
        self.board = board
        self.queue = queue

    def __str__(self):
        # return f'Задача: {self.name} (расположение: {self.board})'
        return f'Задача: "{self.name}"'


class TaskBoard:
    def __init__(self, name):
        self.name = name
        self.__toDo__ = []  # Базовая очередь (новые задачи)
        self.__inProgress__ = []  # Список задач в работе
        self.__resolved__ = []  # Список решенных задач
        self.__garbage__ = []  # Мусор (удаленные таски)

    def __str__(self):
        return self.name

    def __viewstring__(self, header, table):
        view_string = header

        if len(table) == 0:
            view_string = f'{view_string}\nЗАДАЧИ ОТСУТСВУЮТ'
        else:
            for task_item in enumerate(table):
                view_string = f'{view_string}\n{task_item[0]}. {str(task_item[1])}'

        return view_string

    def __get_table_by_name__(self, name):
        target_table = []

        if name == 'todo':
            target_table = self.__toDo__
        elif name == 'in_progress':
            target_table = self.__inProgress__
        elif name == 'resolved':
            target_table = self.__resolved__

        return target_table

    def add_task(self, name, description):
        new_task = Task(name, description, self, self.__toDo__)
        self.__toDo__.append(new_task)
        return new_task

    def move_task(self, task, target_queue):
        # Удаляем задачу с текущей доски
        task.queue.remove(task)

        # Добавляем ее на целевую доску
        target_queue_ref = self.__get_table_by_name__(target_queue)
        task.queue = target_queue_ref
        target_queue_ref.append(task)
        print(f'[!!!] {task} была перемещена в очередь {target_queue}\n')

    def del_task(self, task):
        task.queue.remove(task)
        self.__garbage__.append(task)
        print(f'[!!!] {task} была перемещена в мусорную корзину\n')

    @property
    def todo(self):
        return self.__viewstring__('Список задач для выполнения:', self.__toDo__)

    @property
    def in_progress(self):
        return self.__viewstring__('Список задач в работе:', self.__inProgress__)

    @property
    def resolved(self):
        return self.__viewstring__('Список решенных задач:', self.__resolved__)


task_board = TaskBoard('Доска Scrum-команды')

task_1 = task_board.add_task('Создать классы', 'Создать классы, необходимые для работы алгоритма')
task_2 = task_board.add_task('Описать тестовые данные', 'Заполнить описание тестовых данных')
task_3 = task_board.add_task('Pull-Request', 'Приложить пулл реквест к сдаче домашнего задания')

print(f'{task_board.todo}\n\n{task_board.in_progress}\n\n{task_board.resolved}\n\n')
task_board.move_task(task_1, 'in_progress')
print(f'{task_board.todo}\n\n{task_board.in_progress}\n\n{task_board.resolved}\n\n')
task_board.del_task(task_2)
print(f'{task_board.todo}\n\n{task_board.in_progress}\n\n{task_board.resolved}\n\n')