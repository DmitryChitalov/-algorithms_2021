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


class PlateStackClass:
    def __init__(self):
        self.elems = [[]]
        self.counter = 0
        self.stek_size = 10

    def is_empty(self):
        return self.elems == [[]]

    def push(self, el):
        if not len(self.elems[self.counter]) < self.stek_size:
            self.counter += 1
            self.elems.append([])
        self.elems[self.counter].append(el)

    def pop(self):
        if self.is_empty():
            return None
        res = self.elems[self.counter].pop()
        if len(self.elems[self.counter]) == 0 and self.counter > 0:
            self.counter -= 1
            self.elems.pop()
        return res

    def size(self):
        return self.counter * self.stek_size + len(self.elems[self.counter])

    def new_method_not_from_classes(self):
        return "hello world"

    def toString(self):
        print("PlateStackClass counter:", self.counter, "size:", self.size(), "content:", self.elems)


""" для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
    какие именно? """


psc = PlateStackClass()

for i in range(32):
    psc.push(i)
    psc.toString()

while not psc.is_empty():
    psc.pop()
    psc.toString()

