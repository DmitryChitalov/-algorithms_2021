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


class StackOfPlates:
    def __init__(self, max):
        self.plates = [[]]
        self.max = max

    def is_empty(self):
        return self.plates == [[]]

    def push_in(self, plate):
        if len(self.plates[len(self.plates) - 1]) == self.max:
            self.plates.append([])
        self.plates[len(self.plates) - 1].append(plate)

    def pop_uot(self):
        value = self.plates[len(self.plates) - 1].pop()
        if self.plates[len(self.plates) - 1] == []:
            del self.plates[len(self.plates) - 1]
        return value

    def get_val(self):
        return self.plates[len(self.plates) - 1]

    def stack_size(self):
        return len(self.plates)

if __name__ == '__main__':

    pl = StackOfPlates(3)
    print(pl.plates)
    pl.push_in(1)
    print(pl.plates)
    pl.push_in(2)
    print(pl.plates)
    pl.push_in(3)
    print(pl.plates)
    pl.push_in(4)
    print(pl.plates)
    pl.push_in(5)
    print(pl.plates)
    pl.push_in(6)
    print(pl.plates)
    pl.push_in(7)
    print(pl.plates)
    pl.push_in(8)
    print(pl.plates)
    print(pl.stack_size())
    pl.pop_uot()
    print(pl.plates)
    pl.pop_uot()
    print(pl.plates)
    pl.pop_uot()
    print(pl.plates)
    pl.pop_uot()
    print(pl.plates)
    print(pl.stack_size())
    print(pl.get_val())
