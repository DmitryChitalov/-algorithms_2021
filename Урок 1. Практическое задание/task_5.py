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


class StacksOfPlates:

    def __init__(self, capacity):
        self.elms = []
        self.cap = capacity
        self.size = 0
        self.size_of_cur_stack = 0

    def is_empty(self):
        return self.elms == []

    def is_full(self):
        return self.size_of_cur_stack == self.cap

    def push_in(self, el):
        if el + self.size_of_cur_stack <= self.cap:
            for _ in range(el):
                if self.is_full() or self.is_empty():
                    self.elms.append([])
                    self.elms[-1].append(0)
                else:
                    self.elms[-1].append(0)
        else:
            for _ in range(el % self.cap):
                if self.is_full() or self.is_empty():
                    self.elms.append([])
                    self.elms[-1].append(0)
                else:
                    self.elms[-1].append(0)
            for _ in range(el // self.cap):
                self.elms.insert(-2, self.cap * [0])
            self.size = len(self.elms) if not self.is_empty() else 0
            self.size_of_cur_stack = len(self.elms[-1]) if not self.is_empty() else 0

    def pop_out(self, el):
        if el > self.get_val():
            return f'Cannot take {el} plates, it is more than we have now({self.get_val()})'
        if el > self.cap:
            for _ in range(el // self.cap):
                self.elms.pop(-2)
            for _ in range(el % self.cap):
                self.elms[-1].pop()
                self.elms = list(filter(None, self.elms))
        else:
            for _ in range(el):
                self.elms[-1].pop()
                self.elms = list(filter(None, self.elms))

        self.size = len(self.elms) if not self.is_empty() else 0
        self.size_of_cur_stack = len(self.elms[-1]) if not self.is_empty() else 0

    def get_val(self):
        return 0 if self.is_empty() else len(self.elms[:-1]) * self.cap + self.size_of_cur_stack

    def structure(self):
        return self.elms


if __name__ == '__main__':
    a = StacksOfPlates(10)
    a.push_in(34)
    print(a.structure())
    print(a.size)
    print(a.size_of_cur_stack)
    a.pop_out(12)
    print(a.structure())
    print(a.size)
    print(a.size_of_cur_stack)
    a.push_in(45)
    print(a.structure())
    print(a.size)
    print(a.size_of_cur_stack)
    a.pop_out(67)
    print(a.structure())
    print(a.size)
    print(a.size_of_cur_stack)
