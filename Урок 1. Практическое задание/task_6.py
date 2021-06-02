""" Домашнее задание к уроку №1 курс Алгоритмы и структуры данных на Python
    студент: Максим Сапунов Jenny6199@yandex.ru
    29.05.2021
"""


#    Задание 6.
#    Задание на закрепление навыков работы с очередью
#    Реализуйте структуру "доска задач".
#    Структура должна предусматривать наличие несольких очередей задач, например,
#    1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
#    2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
#    на корректировку решения
#    После реализации структуры, проверьте ее работу на различных сценариях
#    Примечание: в этом задании вспомните ваши знания по работе с ООП
#    и опирайтесь на пример урока
#    Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
#    Задание творческое. Здесь нет жестких требований к выполнению.


class Queue:
    """ Простое представление очереди """

    def __init__(self):
        """" Конструктор класса"""
        self.queue = []

    def new_task(self, task_text: str):
        """ Добавление задачи в очередь."""
        self.queue.insert(0, task_text)

    @property
    def next_task(self):
        """ Получить задачу из очереди. """
        return self.queue.pop() if self.are_some_tasks() else '!Нет текущих задач!'

    def are_some_tasks(self):
        """ Проверяет наличие задач в очереди. """
        return True if self.queue != [] else False


def test_queue():
    """ тестирующая функция для класса очереди"""
    my_queue = Queue()
    my_queue.new_task('Подпереть землянку')
    my_queue.new_task('Залатать корыто')
    my_queue.new_task('Закинуть невод')
    print(my_queue.queue)
    for i in range(4):
        print(my_queue.next_task)


if __name__ == '__main__':
    # Создраем экземпляры очередей
    waiting_task = Queue()
    completed_task = Queue()
    not_full_task = Queue()

    # Наполняем очередь ожидающих задач
    waiting_task.new_task('Купить продукты')
    waiting_task.new_task('Помыть машину')
    waiting_task.new_task('На работу эгейн')
    waiting_task.new_task('Сходить в аптеку')
    waiting_task.new_task('Забрать детей из сада')

    print(waiting_task.queue)
    for el in range(len(waiting_task.queue)):
        current_task = waiting_task.next_task
        print(f'Обозначьте статус задачи "{current_task}": 1-выполнено, 0-не выполнено.')
        selector = int(input())
        if selector == 1:
            completed_task.new_task(current_task)
        else:
            not_full_task.new_task(current_task)
    print(f'Выполненные задачи : {completed_task.queue}')
    print(f'Ожидают завершения : {not_full_task.queue}')
