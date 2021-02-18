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


class Todo:
    def __init__(self):
        self.tasks = [
            {1: 'Сделать задачу'},
            {2: 'Добавить задачу'},
            {3: 'Разобраться с проблемой'}
        ]
        self.check_tasks = []
        self.rewrite = []
        self.completed = []

    @staticmethod
    def get_position(idn, lst):
        if isinstance(lst, dict):
            for dct in lst:
                if dct.get(idn) is not None:
                    return dct

    def get_tasks(self):
        """
        Метод который выводит задачи
        """
        print('\nЗадачи для работы:')
        if len(self.tasks) == 0:
            print('\tЗадач нет')
        for task in self.tasks:
            for idn, content in task.items():
                print(f'\t {idn}. {content}')

    def get_check_tasks(self):
        """
        Метод для вывода задач на проверке
        """
        print('\nЗадачи на проверку:')
        if len(self.check_tasks) == 0:
            print('\tНет задач на проверку')
        for task in self.check_tasks:
            print(task)
            for idn, content in task.items():
                print(f'\t {idn}. {content}')

    def get_rewrite(self):
        """
        Метод для вывода задач на доработку
        """
        print('\nЗадачи на доработку:')
        if len(self.rewrite) == 0:
            print('\tНет задач на доработку')
        for task in self.rewrite:
            for idn, content in task.items():
                print(f'\t {idn}. {content}')

    def get_complete(self):
        """
        Метод для вывода выполненных задач
        """
        print('\nВыполненные задачи:')
        if len(self.completed) == 0:
            print('\tНет выполненных задач')
        for task in self.completed:
            for idn, content in task.items():
                print(f'\t {idn}. {content}')

    def add_task(self, content):
        """
        Метод для добавления новой задачи
        """
        for idn in self.tasks[-1].keys():
            self.tasks.append({idn + 1: content})

    def add_to_check(self, idn):
        """
        Метод для перенаправления задачи на проверку
        """
        if len(self.tasks) == 0:
            print("Нет задач на проверку")
        if len(self.tasks) >= 1:
            self.check_tasks.append(self.get_position(idn, self.tasks))
            self.tasks.pop()

    def add_to_complete(self, idn):
        """
        Метод для перенаправления проверенной задачи на выполнение
        """
        if len(self.check_tasks) == 0:
            print("Нет задач на выполнение")
        if len(self.check_tasks) >= 1:
            self.completed.append(self.get_position(idn, self.check_tasks))

    def add_to_rewrite(self, idn):
        """
        Метод для перенаправления задач с проверки на доработку
        """
        if len(self.check_tasks) == 0:
            print("Нет задач на выполнение")
        if len(self.check_tasks) >= 1:
            self.rewrite.append(self.get_position(idn, self.check_tasks))


sess = Todo()

sess.get_tasks()
sess.get_check_tasks()
sess.get_complete()
sess.get_rewrite()
print("\n****************************")
sess.add_task('Проверка и доработка')
sess.add_task('Заполнение')
sess.add_task('Последняя проверка')
sess.add_to_check(1)
sess.add_to_check(2)
sess.add_to_check(3)
sess.add_to_check(5)
sess.add_to_complete(1)
sess.add_to_rewrite(2)
print("\n****************************")
sess.get_tasks()
sess.get_check_tasks()
sess.get_complete()
sess.get_rewrite()
