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

    def push_to(self, el):
        if len(self.elems[len(self.elems) - 1]) == 5:
            self.elems.append([el])
        else:
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        if len(self.elems[len(self.elems) - 1]) == 1:
            return self.elems.pop()
        else:
            return self.elems[len(self.elems) - 1].pop()

    def stack_size(self):
        return len(self.elems)

    def get_val_last(self):
        return self.elems[len(self.elems) - 1]

    def get_stack(self):
        return self.elems


start = StackClass()
start.push_to(1)
start.push_to(2)
start.push_to(3)
start.push_to(4)
start.push_to(5)
start.push_to(6)
print(start.stack_size())
print(start.get_stack())
start.pop_out()
print(start.get_stack())