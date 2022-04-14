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


class MyStack():
    def __init__(self, capacity):
        self.elems, self.capacity = [], self.capacity

    def __str__(self):
        print(self.elems)

    def __add__(self, el):
        if len(self.elems) < self.capacity:
            self.elems.append(el)
        else:
            self.elems.append([el])

    def pop_out(self):
        result = self.elems[len(self.elems)-1].pop()
        if len(self.elems[len(self.elems)-1]) == 0:
            self.elems.pop()
        return result

    def stack_size(self):
        size = 0
        for el in self.elems:
            size += len(el)
        return size

    def stack_counter(self):
        counter = 0
        for el in self.elems:
            counter += 1
        return counter


if __name__ == '__main__':
    stack = MyStack(3)
    stack.__add__('plate1')
    stack.__add__('plate2')
    stack.__add__('plate3')


