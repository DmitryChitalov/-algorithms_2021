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


class QueueClass:
    def __init__(self):
        self.elems = []

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:
    """
    Класс "Доска задач"
    """

    def __init__(self):
        self.__tasks = QueueClass()
        self.__solved_problems = QueueClass()
        self.__tasks_for_revision = QueueClass()

    def __str__(self):
        return f"Задач не рассмотрено - {self.__tasks.size()}" \
               f"Задач решено - {self.__solved_problems.size()}" \
               f"Задач на исправлении - {self.__tasks_for_revision.size()}"

    def add_task(self, element):
        """
        Добавляет задачу в очередь нерешенных
        :param element:
        :return:
        """
        self.__tasks.to_queue(element)

    def solve_the_problem(self):
        """
        Переносит очередную задачу в очередь решенных
        :return:
        """
        if self.__tasks.size() > 0:
            self.__solved_problems.to_queue(self.__tasks.from_queue())
        else:
            print("Нет задач для решения")

    def add_ro_revision(self):
        """
        Отправляет очередную задачу на доработку
        :return:
        """
        if self.__tasks.size() > 0:
            self.__tasks_for_revision.to_queue(self.__tasks.from_queue())
        else:
            print("Нет задач для исправления")

    def solve_the_revision_problem(self):
        """
        Решает отправленную на доработку задачу
        :return:
        """
        if self.__tasks_for_revision.size() > 0:
            self.__solved_problems.to_queue(self.__tasks_for_revision.from_queue())
        else:
            print("Нет доступных для испарвления задач")

    def clear_desk_from_solved_tasks(self):
        """
        Очищает список решенных задач
        :return:
        """
        self.__solved_problems = QueueClass()

    def print_all_task_board(self):
        """
        Выводин на печать все содержимое доски
        :return:
        """
        print(f"Список предстоящих дел: {self.__tasks}\n"
              f"Список решенных дел: {self.__solved_problems}\n"
              f"Список отложенных дел: {self.__tasks_for_revision}\n")


if __name__ == "__main__":
    tb = TaskBoard()
    for idx in range(1, 7):
        tb.add_task(f"Важное дело №{idx}")

    tb.print_all_task_board()

    tb.add_ro_revision()
    tb.solve_the_problem()
    tb.solve_the_problem()
    tb.add_ro_revision()

    tb.print_all_task_board()

    tb.solve_the_revision_problem()

    tb.print_all_task_board()

    print("============= Второй сценарий =============")
    tb2 = TaskBoard()

    tb2.add_task("Супер сложная задача")
    tb2.print_all_task_board()
    tb2.add_ro_revision()
    tb2.solve_the_problem()

    tb2.print_all_task_board()

    tb2.solve_the_revision_problem()
    tb2.solve_the_revision_problem()

    tb2.print_all_task_board()

    tb2.clear_desk_from_solved_tasks()

    tb2.print_all_task_board()
