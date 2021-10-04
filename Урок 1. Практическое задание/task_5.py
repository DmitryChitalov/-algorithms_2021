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
    def __init__(self, max_plates):
        self.max_plates = max_plates
        self.stacks = []

    def __str__(self):
        return str(self.stacks)

    def is_empty(self):
        return self.stacks == []

    def push_in(self, el):
        if self.is_empty():
            self.stacks.append(el)
        else:
            self.stacks[len(self.stacks) - 1] = self.stacks[
                                                    len(self.stacks) - 1] + el
        while self.stacks[len(self.stacks) - 1] > self.max_plates:
            self.stacks.append(self.stacks[len(self.stacks) - 1] - self.max_plates)
            self.stacks[len(self.stacks) - 2] = self.max_plates

    def pop_out(self, el):
        if sum(self.stacks) < el:
            return print(f'В стопках {sum(self.stacks)} тарелок(и) невозможно удалить {el} тарелок(и)')

        while el > self.stacks[len(self.stacks) - 1]:
            el -= self.stacks[len(self.stacks) - 1]
            self.stacks.pop()
        self.stacks[len(self.stacks) - 1] -= el

        if self.stacks[len(self.stacks) - 1] == 0:
            self.stacks.pop()

    def number_of_stacks(self):
        return len(self.stacks)

    def last_stack_size(self):
        if not self.is_empty():
            return self.stacks[len(self.stacks) - 1]
        return 0

    def full_stacks(self):
        full = 0
        for item in self.stacks:
            if item == self.max_plates:
                full += 1
        return full


if __name__ == '__main__':
    max_size = 5
    plates = PlateStackClass(max_size)

    print('Стопка пуста?:', plates.is_empty())
    plates.push_in(11)
    plates.push_in(12)
    print('Стопка пуста?:', plates.is_empty())
    plates.pop_out(25)
    plates.pop_out(8)
    print('Стопки тарелок:', plates)
    print('Количество тарелок в последней стопке: ', plates.last_stack_size())
    print('Количество стопок: ', plates.number_of_stacks())
    print('Заполненные стопки:', plates.full_stacks())
