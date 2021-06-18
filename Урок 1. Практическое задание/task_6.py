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

class TaskClass:
    allowed = {}  # решенные задачи
    task = []  # Поставленные задачи
    _task_id = 0

    def is_empty(self):
        return self.task == []

    def to_task(self, item):
        self._task_id += 1
        self.task.insert(0, {self._task_id: {'item': item}})

    def from_task(self):
        task = self.task.pop()
        self.allowed.update(task)
        return task

    def size(self):
        return len(self.task)

    def show_allowed(self):
        print(f'Всего задач выполнено:\n{"=" * 20}')
        for task_id, item in self.allowed.items():
            print(f'Идентификатор задачи: {task_id}; Описание: {item}')

    @classmethod
    def get_allowed(cls, task_id):
        return cls.allowed.get(task_id)


class TaskRefineClass(TaskClass):
    refine_dict = {}  # Архив того, что отправлено на доработку

    def __init__(self):
        TaskClass.__init__(self)

    def to_refine_task(self, task_id):
        ref = self.allowed[task_id]
        # Добавляем данные предыдущего id и записываем в задачи
        result = {task_id: {'item': ref, 'refine': 'from_anybody'}}
        TaskClass().task.insert(0, result)
        self.refine_dict.update(result)
        return f'Отправлена на доработку задача id: {task_id}. {self.allowed.pop(task_id)}'



if __name__ == '__main__':
    tc_object = TaskClass()

    # помещаем объекты в очередь
    for i in range(23):
        tc_object.to_task(f'{i}-Текст задачи')

    print(f'Объем задач: {tc_object.size()}\n')

    # помещаем объекты в выполненные
    for i in range(6):
        tc_object.from_task()

    # Смотрим выполненные
    tc_object.show_allowed()

    # получаем выполненную задачу по id
    print(tc_object.get_allowed(1))

    # Создаем экземпляр дочернего класса
    tc_rf_object = TaskRefineClass()

    # Инициализируем экземпляр класса, возвращающего задачу в работу
    print(tc_rf_object.to_refine_task(2))

    # Инициализируем экземпляр класса, возвращающего задачу в работу
    print(tc_rf_object.to_refine_task(6))

    # Инициализируем экземпляр класса, возвращающего задачу в работу
    print(tc_rf_object.to_refine_task(3))

    # помещаем объект в  стандартную очередь
    tc_object.to_task(f'GH-Текст задачи')

    print(f'Объем задач: {tc_object.size()}\n')

    # делаем контрольный срез задач в очереди. Задачи вернулись в очередь
    for el in TaskClass.task:
        print(el)

    # Смотрим выполненные - сколько осталовсь. Те, которые вернулись в основную очеред ушли из выполненных
    tc_object.show_allowed()
