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
    def __init__(self, max_stack):
        self.max_stack = max_stack
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if self.is_empty():
            self.elems.append(el)
        else:
            self.elems[len(self.elems) - 1] += el
        while self.elems[len(self.elems) - 1] > self.max_stack:
            self.elems.append(self.elems[len(self.elems) - 1] - self.max_stack)
            self.elems[len(self.elems) - 2] = self.max_stack

    def pop_out(self, el):
        while el > self.elems[len(self.elems) - 1]:
            el -= self.elems[len(self.elems) - 1]
            self.elems.pop()
        self.elems[len(self.elems) - 1] -= el

    def stack_size(self):
        elem_sum = 0
        for stack in self.elems:
            elem_sum += stack
        return elem_sum


if __name__ == '__main__':
    num_of_plates = int(input('Сколько тарелок в стопке? '))
    plates = StacksOfPlates(num_of_plates)
    print('Стопка пустая или нет? ', plates.is_empty())
    print('Добавляю необходимое количество тарелок:')
    plates.push_in(35)
    plates.push_in(23)
    print(plates.elems)
    print('Убираю нужное количество тарелок:')
    plates.pop_out(22)
    plates.pop_out(2)
    print(plates.elems)
    print('Всего тарелок сейчас: ')
    print(plates.stack_size())

