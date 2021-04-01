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


class ClassStack:

    auto_count = -1

    def __init__(self):
        self.elements = []
        self.stack = []

    def upd_stack(self):
        self.stack.append(self.elements)
        self.elements = []
        return

    def push_in(self, el):
        ClassStack.auto_count += 1
        if ClassStack.auto_count == 4:
            ClassStack.auto_count = 0
            ClassStack.upd_stack(self)
        return self.elements.append(el)

    def pop_out(self):
        if [] in self.stack:
            self.stack.remove([])
        else:
            for el in range(len(self.stack)):
                return self.stack[el - 1].pop()


cs = ClassStack()

cs.push_in(1)
cs.push_in(2)
cs.push_in(3)
cs.push_in(4)
cs.push_in(5)
cs.push_in(6)
cs.push_in(7)
cs.push_in(8)
cs.push_in(9)
cs.push_in(10)
cs.push_in(11)
cs.push_in(12)
cs.push_in(13)
cs.push_in(14)
cs.push_in(15)
cs.push_in(16)
cs.push_in(17)

# удаление по принципу первый вошел последний вышел
"""cs.pop_out()
cs.pop_out()
cs.pop_out()
cs.pop_out()
cs.pop_out()
cs.pop_out()
cs.pop_out()"""

print(cs.stack)
print(cs.elements)
