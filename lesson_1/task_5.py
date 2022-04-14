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


class PlateStackClass:
    def __init__(self, max_size):
        self.elems = [[[]]]  # При создании экземпляра класса создаётся стопка из одной тарелки
        self.max_size = max_size

    def __str__(self):
        return str(self.elems)

    def push_in(self):
        if len(self.elems[-1]) < self.max_size:
            self.elems[-1].append([])
        else:
            self.elems.append([[]])

    def pop_out(self):
        if len(self.elems[-1]) > 1:
            self.elems[-1].pop()
        else:
            self.elems.pop()

    def get_value(self):  # Колличество тарелок в последней стопке
        return len(self.elems[-1])

    def stack_size(self):    # Суммарное олличество тарелок во всех стопках
        sum_plates = 0
        for el in self.elems:
            sum_plates += len(el)
        return sum_plates


if __name__ == '__main__':
    test = PlateStackClass(3)
    print(test)
    test.push_in()
    test.push_in()
    test.push_in()
    test.push_in()
    test.push_in()
    test.push_in()
    print(test)
    print(test.get_value())
    print(test.stack_size())
    test.pop_out()
    test.pop_out()
    print(test)
    print(test.get_value())
    print(test.stack_size())


