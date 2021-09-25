"""
Задание 6.
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

from _datetime import datetime, timedelta
from collections import namedtuple
from pprint import pprint


# user = User(0, "John", "McClane", "die.hard@hollywood.com")
# TODO: Make DB integration, make authentication, make commands processing...


class TaskBoard:
    User = namedtuple('User', 'first_name, last_name, email')
    Task = namedtuple('Task',
                      'current_status, previous_status, title, description, author, supervisor, performer, '
                      'deadline, date_added, date_edited, date_finished')
    STATUS = ("new", "in progress", "review", "clarification required", "confirmation", "done")

    def __init__(self):
        """
        Standard class initializer
        """
        self.__tasks = dict()  # key - id
        self.__users = dict()  # key - login
        self.__last_tid = -1

    def add_user(self, login: str, first_name: str, last_name: str, email: str) -> bool:
        """
        A user adding function.
        :param login: str; user's login
        :param first_name: str; user's first name
        :param last_name: str; user's last name
        :param email: str; user's e-mail
        :return: True if user added, else - False
        """

        if login in self.__users.keys():
            print("This login already exists!")
            return False

        self.__users[login] = TaskBoard.User(first_name, last_name, email)

        print("Success!")
        return True

    def add_task(self, title: str, description: str, author: str,
                 deadline: datetime = None, supervisor: str = None, performer: str = None) -> bool:
        """
        A task adding function.
        :param title: str; title of the task
        :param description: str; description of the task
        :param author: str; login of the author
        :param deadline: datetime; date and time of the deadline
        :param supervisor: str; login of the supervisor
        :param performer: str; login of the performer
        :return: True if task successfully added, else - False
        """

        if deadline is None:
            datetime.now() + timedelta(days=21)
        if supervisor is None:
            supervisor = author

        self.__last_tid += 1
        self.__tasks[self.__last_tid] = (TaskBoard.Task(TaskBoard.STATUS[0], TaskBoard.STATUS[0], title, description,
                                                        author, supervisor, performer, deadline,
                                                        datetime.now(), datetime.now(), None))
        return True

    def update_task(self, task_id: int, status: int, editor: str, performer: str = None,
                    description: str = None, deadline: datetime = None) -> bool:
        """
        current_status, previous_status, title, description, author, supervisor, performer, '
                      'deadline, date_added, date_edited, date_finished
        :param task_id: int; ID of the task for update
        :param status: int; new status of the task. Only author or supervisor can set status 'done'(5)
        :param editor: str; login of the user, who edit the task
        :param performer: str; new task performer
        :param description: str; new description (prepend with '+' to add text to the end of current description).
                                Only author or supervisor can edit that!
        :param deadline: datetime; new deadline date and time for the task. Only author or supervisor can edit that!
        :return: True if task successfully updated, else - False
        """
        # Looking for task_id
        if task_id not in self.__tasks.keys():
            print(f"There is no task with id = {task_id}")
            return False
        # Looking for user ID
        if editor not in (self.__tasks[task_id].author, self.__tasks[task_id].supervisor,
                          self.__tasks[task_id].performer):
            print(f"Permission denied! Only author, supervisor or performer can change status! {editor} can not!")
            return False
        if performer is None:
            if self.__tasks[task_id].performer is None:
                performer = self.__tasks[task_id].performer
            else:
                if editor != self.__tasks[task_id].author and editor != self.__tasks[task_id].supervisor:
                    print(f"Only author or supervisor can set new performer! {editor} can not!")
                    return False
        else:
            if editor != self.__tasks[task_id].author and editor != self.__tasks[task_id].supervisor:
                print(f"Only author or supervisor can set new performer! {editor} can not!")
                return False

        if status < 0:
            status = 0
        if status >= len(TaskBoard.STATUS):
            status = len(TaskBoard.STATUS)
        if status == TaskBoard.STATUS[5] and self.__tasks[task_id].author != editor \
                and self.__tasks[task_id].supervisor != editor:
            print("Only author or supervisor can set status 'done'(5)")
            return False
        # current_status, previous_status
        previous_status = self.__tasks[task_id].current_status

        if description is not None:
            if self.__tasks[task_id].author != editor and self.__tasks[task_id].supervisor != editor:
                print("This user has no permission to change description in this task!")
                return False
        else:
            description = self.__tasks[task_id].description

        if deadline is not None:
            if self.__tasks[task_id].author != editor and self.__tasks[task_id].supervisor != editor:
                print("This user has no permission to change deadline in this task!")
                return False
        else:
            deadline = self.__tasks[task_id].deadline

        # date_edited, date_finished
        if status == TaskBoard.STATUS[5]:
            date_finished = datetime.now()
        else:
            date_finished = None
        date_edited = datetime.now()

        self.__tasks[task_id]._replace(current_status=status, previous_status=previous_status,
                                       performer=performer, description=description,
                                       deadline=deadline, date_edited=date_edited, date_finished=date_finished)
        print(f"Task updated: task_id: {task_id}, status: {status}.{TaskBoard.STATUS[status]}, editor: {editor}, "
              f"performer: {performer}, description: {description}, "
              f"deadline: {deadline.isoformat() if deadline is not None else None}")
        return True

    def show_tasks(self, status: int = None) -> list or None:
        """
        Показывает имеющиеся задачи
        :param status: str; статус задач, которые надо показать
        :return: список кортежей (id, задача)
        """
        task_list = []
        if status is None:
            for id, task in self.__tasks.items():
                task_list.append((id, task))
        elif status < 0 or status > len(TaskBoard.STATUS) - 1:
            print(f"Wrong argument: status can be only between 0 and {len(TaskBoard.STATUS) - 1} (both inclusive)!")
            return None
        else:
            for id, task in self.__tasks.items():
                if task.current_status == status:
                    task_list.append((id, task))

        pprint(task_list)
        return task_list


if __name__ == '__main__':
    tb = TaskBoard()
    tb.add_user('login1', 'fname1', 'lname1', 'email1')
    tb.add_user('login2', 'fname2', 'lname2', 'email2')
    tb.add_user('login3', 'fname3', 'lname3', 'email3')
    tb.add_task('Some task1', 'Some description1', 'login1', supervisor='login1')
    tb.add_task('Some task2', 'Some description2', 'login1', supervisor='login2')
    tb.add_task('Some task3', 'Some description3', 'login2', supervisor='login2', performer='login1',
                deadline=datetime(2021, 9, 23, 19, 0, 0))
    tb.show_tasks()
    tb.update_task(0, 2, 'login1', 'login3')
    tb.update_task(1, 3, 'login2', performer='login2', deadline=datetime.now()+timedelta(days=20))
    tb.show_tasks()
