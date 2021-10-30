"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

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
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""
import math


class StackClass:

    def __init__(self, size):
        self.elems = [[]]
        self.size = size

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        if not len(self.elems[len(self.elems) - 1]):
            self.elems.pop()
        return self.elems[len(self.elems) - 1].pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def stack_fulsize(self):
        ful_size = 0
        for el in self.elems:
            ful_size += len(el)
        return ful_size


if __name__ == '__main__':
    plates = StackClass(10)
    for i in range(25):
        plates.push_in(i)
    print(plates.elems)
    for i in range(11):
        plates.pop_out()
    print(plates.elems)
    print(plates.stack_size())
    print(plates.stack_fulsize())
