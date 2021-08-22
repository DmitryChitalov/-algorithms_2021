"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import random


class StackClass:
    """
    Класс имитации стека
    """

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def push_in(self, element):
        self.elements.append(element)

    def pop_out(self):
        return self.elements.pop()

    def get_value(self):
        return self.elements[len(self.elements) - 1]

    def stack_size(self):
        return len(self.elements)

    def show_elements(self):
        print(self.elements)


class ListOfStacks:
    """
    Класс набора стеков
    """

    def __init__(self, maxsize):
        self.elements = []
        self.maxsize = maxsize

    def list_size(self):
        return len(self.elements)

    def push_list(self, elements):
        self.elements.append(StackClass())
        for item in elements:
            if self.elements[self.list_size() - 1].stack_size() == self.maxsize:
                self.elements.append(StackClass())
            self.elements[self.list_size() - 1].push_in(item)

    def print_list(self):
        for item in self.elements:
            item.show_elements()


if __name__ == '__main__':
    lst = random.sample(range(-1, 100000), 23)

    list_of_stacks = ListOfStacks(5)
    list_of_stacks.push_list(lst)
    list_of_stacks.print_list()
