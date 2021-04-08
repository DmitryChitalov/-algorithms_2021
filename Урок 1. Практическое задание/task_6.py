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


class BoardStruct:
    def __init__(self):
        self.counter_id = 0
        self.boards = {
            "on_going": dict(),
            "on_hold": dict(),
            "issued": dict(),
            "solved": dict()
        }

    def getId(self):
        self.counter_id += 1
        return self.counter_id - 1

    def get_boards(self):
        print("Boards:", self.boards.keys())
        return self.boards.keys()

    def get_tasks(self, board_name):
        if board_name in self.boards.keys():
            print(self.boards[board_name])
            return self.boards[board_name]

    def get_task_byName(self, board_name, task):
        if board_name in self.boards.keys():
            print(self.boards[board_name][task])
            return self.boards[board_name][task]

    def create_task(self, header, task):
        tsk = BoarsTask(header)
        tsk.set_task(task)
        tsk.set_board("on_hold")
        self.boards[tsk.get_boardName()][tsk.header] = tsk

    def move_task(self, task_name, mv_from, mv_to):
        if mv_from in self.boards.keys()\
                and mv_to in self.boards.keys()\
                and task_name in self.boards[mv_from].keys():
            ts: BoarsTask = self.boards[mv_from].pop(task_name)
            self.boards[mv_to][task_name] = ts
            print("Board from:", self.boards[mv_from])
            print("Board to:", self.boards[mv_to])
        else:
            print("The task does NOT exist!")  # reDo should throw an exception
        return ""

    def create_board(self, board_name):
        if board_name not in self.boards.keys():
            print("The board already exist!")  # reDo should throw an exception
        else:
            self.boards[board_name] = dict()
            print("Boards:", self.boards)

    def remove_board(self, board_name):
        if board_name in self.boards.keys():
            self.boards.pop(board_name, None)
            print("Boards:", self.boards)
        else:
            print("The board does NOT exist!")  # reDo should throw an exception


class BoarsTask:
    def __init__(self, header):
        self.header = header
        self.boardName = ""
        self.task = ""

    def set_task(self, input):
        self.task = input

    def set_board(self, board_name):
        self.boardName = board_name

    def get_header(self):
        return self.header

    def get_boardName(self):
        return self.boardName

    def get_task(self):
        return self.task


bs = BoardStruct()
bs.get_boards()
bs.get_tasks("on_hold")
bs.create_task("first task", "Do it!")
bs.create_task("second task", "Do it!")
bs.create_task("third task", "Do it!")
bs.get_tasks("on_hold")
ts: BoarsTask = bs.get_task_byName("on_hold", "second task")
print(ts.task)
bs.move_task("second task", "on_hold", "on_going")
bs.remove_board("on_hold")

