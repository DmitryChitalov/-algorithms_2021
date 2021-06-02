""" Домашнее задание к уроку №1 курс Алгоритмы и структуры данных на Python
    студент: Максим Сапунов Jenny6199@yandex.ru
    28.05.2021
"""

#    Задание 5.
#    Задание на закрепление навыков работы со стеком
#    Реализуйте структуру "стопка тарелок".
#    Мы можем складывать тарелки в стопку и при превышении некоторого значения
#    нужно начать складывать тарелки в новую стопку.
#    Структура должна предусматривать наличие нескольких стеков.
#    Создание нового стека происходит при достижении предыдущим стеком порогового значения.
#    Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
#    для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
#    для реализации этой задачи.
#    После реализации структуры, проверьте ее работу на различных сценариях
#    Подсказка:
#    Отдельне стопки можно реализовать через:
#    1) созд-е экземпляров стека (если стопка - класс)
#    или
#    2) lst = [[], [], [], [],....]
#    Примечание: в этом задании вспомните ваши знания по работе с ООП
#    и опирайтесь на пример урока
#    Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
#    Задание творческое. Здесь нет жестких требований к выполнению.


class Stack:  # Реализован принцип LIFO
    """ Простое представление стека """

    def __init__(self, boarder: int):
        """
        Конструктор класса
        :param - boarder - значение переполнения элемента стэка
        """
        self.boarder = boarder
        self.stack_element = []
        self.stack_collection = []

    def put_to_stack(self, box):
        """
        Добавить запись в стек
        :param - box - значение добавляемое в стэк.
        :return - None
        """
        if self.boarder_line():
            self.stack_collection.append(self.stack_element[:])
            self.stack_element.clear()
            self.stack_element.append(box)
        else:
            self.stack_element.append(box)

    def get_from_stack(self):
        """
        Функция извлекает последнее значение из стэка и возвращает его значение.
        :return - последнее помещенное в стэк значение, или None если стэк пустой.
        """
        if self.stack_is_empty():
            print('Стэк пустой')
            return None
        else:
            if len(self.stack_element) == 0:
                self.stack_element = self.stack_collection.pop()
                return self.stack_element.pop()
            return self.stack_element.pop()

    def boarder_line(self):
        """
        Функция проверяет заполненность экземпляра стэка
        :return Истина если граница наполненности экземпляра стэка достигнута, иначе ложь.
        """
        return True if (len(self.stack_element) == self.boarder) else False

    def stack_is_empty(self):
        """
        Функция проверяет наличие элементов в стэке
        :return - Истина при наличии элементов в стэке, иначе ложь.
        """
        return True if self.stack_element == [] and self.stack_collection == [] else False

    def stack_remove(self):
        """
        Функция очищает очередь стэка
        :return: None
        """
        self.stack_collection.clear()
        self.stack_element.clear()
        print('Стэк очищен.')

    def count_of_stack(self):
        """ Функция сообщает об общем количестве элементов в стэке"""
        stack_len = len(self.stack_collection) * self.boarder + len(self.stack_element)
        print(f'В настоящий момент в стэке всего {stack_len} элементов.')
        return stack_len


if __name__ == '__main__':
    # Создаем экземпляр стэка.
    v1 = Stack(5)
    # Наполняем стэк и демонстрируем работу функции.
    for i in range(16):
        v1.put_to_stack('+')
        print(v1.stack_collection)
        print(v1.stack_element)

    v1.count_of_stack()

    # Убираем значения из стэка и демонстрируем работу функции.
    for i in range(16):
        v1.get_from_stack()
        print(v1.stack_collection)
        print(v1.stack_element)
