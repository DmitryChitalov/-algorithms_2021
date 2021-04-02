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

    def __init__(self):
        self.basic_list = []
        self.resolved = []
        self.not_resolved = []

    def add_task(self, task):
        self.basic_list.append(task)

    def get_task(self, solution=True):
        task = self.basic_list.pop(0)

        if solution is True:
            self.resolved.append(task)
        else:
            self.not_resolved.append(task)

    def result(self):
        return f'Список задач: {self.basic_list}\nРешенные: {self.resolved}\nЕще нерешенные: {self.not_resolved}'


# создаем объект класса и заполняем список
task_1 = TaskBoard()
for i in range(10):
    task_1.add_task(i)

# поставил простое условие - как пример сортировки задач на решеные и не решеные
for i in range(len(task_1.basic_list)):
    if i % 2 == 1:
        task_1.get_task(solution=False)
    else:
        task_1.get_task()

print(task_1.result())
