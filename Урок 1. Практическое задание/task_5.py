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


from random import randint as ran


class StackClass:
    def __init__(self):
        self.elems = [[]]
        self.x = 0

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems[self.x]) < 10:
            self.elems[self.x].append(el)
        else:
            self.elems.append([])
            self.x += 1
            self.elems[self.x].append(el)

    def pop_out(self):
        if self.elems[self.x]:
            return self.elems[self.x].pop()
        else:
            self.elems.pop()
            self.x -= 1
            return self.elems[self.x].pop()

    def get_val(self):
        return self.elems[self.x][len(self.elems[self.x]) - 1]

    def stack_size(self):
        return (len(self.elems)-1) * 10 + len(self.elems[self.x])


if __name__ == '__main__':
    x = StackClass()
    for i in range(ran(1, 1000)):
        x.push_in(ran(1, 100))
    print(x.elems[-1])
    print(x.stack_size())
    print(x.get_val())
    x.pop_out()
    print(x.get_val())
    print(x.stack_size())
