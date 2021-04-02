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


class MyClass:
    def __init__(self, sz):
        self.all_elems = []
        self.cur_elems = []
        self.maxSize = sz

    def __str__(self):
        return str(self.all_elems + self.cur_elems)

    def is_empty(self):
        return len(self.cur_elems) == 0

    def push_in(self, el):
        if len(self.cur_elems) == self.maxSize:
            self.all_elems.append(self.cur_elems.copy())
            self.cur_elems.clear()
        self.cur_elems.append(el)

    def pop_out(self):
        if len(self.cur_elems) == 1:
            temp = self.cur_elems.pop()
            if len(self.all_elems):
                self.cur_elems = self.all_elems.pop()
            return temp
        if self.is_empty() is False:
            return self.cur_elems.pop()
        else:
            return None

    def get_val(self):
        return self.cur_elems[len(self.cur_elems) - 1]

    def stack_size(self):
        return len(self.all_elems) * self.maxSize + len(self.cur_elems)

    def push_many(self, elems):
        for el in elems:
            self.push_in(el)

    def get_many(self, count):
        for i in range(count):
            yield self.pop_out()

    def pop_out_many(self, count):
        out_list = []
        for qwe in self.get_many(count):
            if qwe is None:
                break
            out_list.append(qwe)
        return out_list


if __name__ == '__main__':
    plates = MyClass(3)
    plates.push_in('Plate1')
    plates.push_in('Plate2')
    plates.push_in('Plate3')
    plates.push_in('Plate4')
    plates.push_in('Plate5')
    print(plates)
    print(plates.pop_out())
    print(plates.get_val())
    print(plates.pop_out_many(3))
    plates.push_many(['Plate111', 'Plate222', 'Plate333', 'Plate444', 'Plate555', 'Plate666', 'Plate777', 'Plate888', 'Plate999'])
    print(plates)
    print(plates.stack_size())
    print(plates.pop_out_many(100))
    print(plates.pop_out_many(100))
