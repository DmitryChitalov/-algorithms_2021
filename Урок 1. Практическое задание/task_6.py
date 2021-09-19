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
        self.tasks = []
        self.base_qu = []
        self.resolved_qu = []
        self.revision_qu = []

    def add_to_base_qu(self, task):
        """ Добавляем задачу в базовую очередь на проверку """
        self.base_qu.insert(0, task)

    def pop_task_from_base(self, completed=True):
        """ Если принимаем решение, что задача выполнена,
        то добавляем ее в конец другой очереди (начало списка)"""
        if self.base_qu:
            if completed:
                self.resolved_qu.insert(0, self.base_qu.pop())
            else:
                self.revision_qu.insert(0, self.base_qu.pop())
        else:
            return 'В базовой очереди нет задач!'

    def pop_from_revision(self):
        """ После доработки задачу возвращаем в базовую очередь на проверку """
        return self.base_qu.insert(0, self.revision_qu.pop()) if self.revision_qu else None

    def pop_from_resolved(self):
        """ Берем из очереди решенных задач результаты """
        return self.resolved_qu.pop() if self.resolved_qu else 'Решенных задач в очереди нет!'

    def show_qu(self):
        print(f'Базовая очередь:\t\t{self.base_qu}\n'
              f'Очередь на доработку:\t{self.revision_qu}\n'
              f'Очередь решенных:\t\t{self.resolved_qu}\n')


# --- Проверка работоспособности
MyTask = TaskBoard()

# 1. Добавим 4 задачи в базовую очередь
print("1. Добавим 7 задач в базовую очередь")
MyTask.add_to_base_qu([1, 'Закрыть проект'])
MyTask.add_to_base_qu([2, 'Закрыть проект'])
MyTask.add_to_base_qu([3, 'Закрыть проект'])
MyTask.add_to_base_qu([4, 'Закрыть проект'])
MyTask.add_to_base_qu([5, 'Закрыть проект'])
MyTask.add_to_base_qu([6, 'Закрыть проект'])
MyTask.add_to_base_qu([7, 'Закрыть проект'])
# Покажем результат
MyTask.show_qu()

# 2. Предположим, что прошли проверку 4 задачи, но 1-3 не прошли
print("2. Прошли проверку 4 задачи, но 1-3 не прошли")
MyTask.pop_task_from_base(False)
MyTask.pop_task_from_base(True)
MyTask.pop_task_from_base(False)
MyTask.pop_task_from_base(True)
# Покажем результат
MyTask.show_qu()

# 3. После доработки 1 и 3 задачи были переданы в базовую очередь
print("3. 1-3 задачи были переданы в базовую очередь")
MyTask.pop_from_revision()
MyTask.pop_from_revision()
# Покажем результат
MyTask.show_qu()

# 4. Предположим, что еще 4 задачи прошли проверку положительно
print("4. Предположим, что еще 4 задачи прошли проверку положительно, в последняя не прошла.")
MyTask.pop_task_from_base(True)
MyTask.pop_task_from_base(True)
MyTask.pop_task_from_base(True)
MyTask.pop_task_from_base(True)
MyTask.pop_task_from_base(False)
# Покажем результат
MyTask.show_qu()

# 5. Заберем из очереди 3 решенных задачи
print("5. Заберем из очереди решенных 3 задачи")
print(MyTask.pop_from_resolved())
print(MyTask.pop_from_resolved())
print(MyTask.pop_from_resolved())
# Покажем результат
print("\n6. Покажем состояние TaskBoard")
MyTask.show_qu()

# 5. Заберем оставшиеся задачи и
print("5. Заберем из очереди решенных 3 задачи")
print(MyTask.pop_from_resolved())
print(MyTask.pop_from_resolved())
print(MyTask.pop_from_resolved())
print(MyTask.pop_from_resolved())
