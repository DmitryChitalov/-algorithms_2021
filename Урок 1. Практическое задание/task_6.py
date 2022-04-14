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


class TaskBoard:
    def __init__(self):
        """ Доска типа Канбан, содржит 4-е доски: task=[], in_develop=[], in_test=[], in_production=[]
            Задачи, которые не прошли тестирование будут возвращаться на доску task.
        """
        self.task_board = dict(task=[], in_develop=[], in_test=[], in_production=[])

    def is_empty(self):
        return self.task_board.get("task") == [] and self.task_board.get("in_develop") == [] and \
               self.task_board.get("in_test") == [] and self.task_board.get("in_production") == []

    def add_task(self, el):
        self.task_board.get("task").append(el)

    def move_task_to_develop(self, index):
        task = self.task_board.get("task").pop(index)
        self.task_board.get("in_develop").append(task)

    def move_develop_to_test(self, index):
        task = self.task_board.get("in_develop").pop(index)
        self.task_board.get("in_test").append(task)

    def move_test_to_production(self, index):
        task = self.task_board.get("in_test").pop(index)
        self.task_board.get("in_production").append(task)

    def move_test_to_task(self, index):
        task = self.task_board.get("in_test").pop(index)
        self.task_board.get("task").append(task)

    def move_test_to_develop(self, index):
        task = self.task_board.get("in_test").pop(index)
        self.task_board.get("in_develop").append(task)

    def move(self, index, board_name_from, board_name_to):
        """ Общий метод для свободного перемещения задач между досками"""
        if self.task_board.get(board_name_from) and self.task_board.get(board_name_to):
            task = self.task_board.get(board_name_from).pop(index)
            self.task_board.get(board_name_to).append(task)

    def get_task_board(self, task):
        board_name = str()
        for key, value in self.task_board.items():
            for x in value:
                if task == x:
                    board_name = key
                    break
        return board_name

    def get_task_index(self, task):
        index = -1
        for k, v in self.task_board.items():
            for ind, value in enumerate(v):
                if task == value:
                    index = ind
                    break
        return index

    def get_task_index(self, board_name, task):
        index = -1
        if self.task_board.get(board_name):
            for ind, value in enumerate(self.task_board.get(board_name)):
                if task == value:
                    index = ind
                    break
        return index

    def get_task_board_and_index(self, task):
        board_and_index = ()
        for k, v in self.task_board.items():
            for ind, value in enumerate(v):
                if task == value:
                    board_and_index = (k, ind)
                    break
        return board_and_index

    def get_board_size(self, board_name):
        if self.task_board.get(board_name):
            return len(self.task_board.get(board_name))


# Добавляем задачи на доску task
tsk_brd = TaskBoard()
tasks = ["Разработка архитектуры БД", "Создание таблиц", "Создание представлений", "Создание процедур",
        "Разработка логики сервера приложений", "Разработка клиентской части"]

for x in tasks:
    tsk_brd.add_task(x)

print(tsk_brd.task_board)

# Перенос задач "Разработка архитектуры БД", "Создание таблиц", "Создание представлений, "Создание процедур""
# на доску in_develop.

task_to_dev = ["Разработка архитектуры БД", "Создание таблиц", "Создание представлений", "Создание процедур"]

for x in task_to_dev:
    brd_and_ind = tsk_brd.get_task_board_and_index(x)
    if brd_and_ind:
        tsk_brd.move_task_to_develop(brd_and_ind[1])

print(tsk_brd.task_board)

# Перенос задач "Разработка архитектуры БД", "Создание таблиц" на доску test.
task_to_test = ["Разработка архитектуры БД", "Создание таблиц"]

for x in task_to_test:
    brd_and_ind = tsk_brd.get_task_board_and_index(x)
    if brd_and_ind:
        tsk_brd.move_develop_to_test(brd_and_ind[1])

print(tsk_brd.task_board)

# Возврат "Создание таблиц" с тестирования на task.
test_to_task = ["Создание таблиц"]

for x in test_to_task:
    brd_and_ind = tsk_brd.get_task_board_and_index(x)
    if brd_and_ind:
        tsk_brd.move_test_to_task(brd_and_ind[1])

print(tsk_brd.task_board)

# Перенос задачи "Разработка архитектуры БД" в in_production из in_test.
test_to_prod = ["Разработка архитектуры БД"]

for x in test_to_prod:
    brd_and_ind = tsk_brd.get_task_board_and_index(x)
    if brd_and_ind:
        tsk_brd.move_test_to_production(brd_and_ind[1])

print(tsk_brd.task_board)


