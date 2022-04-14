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


class StackClass:
    def __init__(self, max_len):
        self.elements = [[]]
        self.max_len = max_len

    def __str__(self):
        return str(self.elements)

    def is_empty(self):
        return self.elements == [[]]

    def push_in(self, el):
        if len(self.elements[len(self.elements)-1]) < self.max_len:
            self.elements[len(self.elements)-1].append(el)
        else:
            self.elements.append([])
            self.elements[len(self.elements)-1].append(el)

    def pop_out(self):
        res = self.elements[len(self.elements)-1].pop()
        if len(self.elements[len(self.elements)-1]) == 0:
            self.elements.pop()
        return res

    def get_val(self):
        return self.elements[len(self.elements)-1]

    def get_el_val(self):
        return self.elements[len(self.elements)-1][-1]

    def stack_size(self):
        return len(self.elements)


SC_obj_1 = StackClass(3)
print(SC_obj_1.is_empty())
print(SC_obj_1.__str__())

SC_obj_1.push_in(1000)
SC_obj_1.push_in(7)
SC_obj_1.push_in(7)
SC_obj_1.push_in(8)
print(SC_obj_1.__str__())
print(SC_obj_1.get_val())
print(SC_obj_1.get_el_val())
SC_obj_1.pop_out()
print(SC_obj_1.__str__())
print(SC_obj_1.pop_out())
print(SC_obj_1.__str__())
print(SC_obj_1.get_val())
print(SC_obj_1.get_el_val())
