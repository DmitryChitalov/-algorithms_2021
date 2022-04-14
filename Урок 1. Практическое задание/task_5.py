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
    def __init__(self):
        self.elems = [[]]
        self.stack = 0

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[self.stack]) < 5:
            self.elems[self.stack].append(el)
        else:
            self.elems.append([])
            self.stack += 1
            self.elems[self.stack].append(el)

    def pop_out(self):
        if len(self.elems[self.stack]) > 1:
            return self.elems[self.stack].pop()
        else:
            temp_elems = self.elems[self.stack].pop()
            self.elems.pop()
            self.stack -= 1
            return temp_elems

    def get_val(self):
        return self.elems[self.stack][len(self.elems[self.stack]) - 1]

    def stack_size(self):
        return len(self.elems[self.stack])

    def stack_self(self):
        return self.elems

    def stack_count(self):
        return len(self.elems)


SC_OBJ = StackClass()

SC_OBJ.push_in(10)
SC_OBJ.push_in('code')
SC_OBJ.push_in(False)
SC_OBJ.push_in(5.5)
SC_OBJ.push_in(1)
SC_OBJ.push_in('cod')
SC_OBJ.push_in(False)
SC_OBJ.push_in(564)
print(SC_OBJ.stack_count())
print(SC_OBJ.stack_self())
print(SC_OBJ.pop_out())
print(SC_OBJ.pop_out())
print(SC_OBJ.pop_out())
print(SC_OBJ.pop_out())
print(SC_OBJ.stack_self())
