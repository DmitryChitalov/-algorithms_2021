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
    def __init__(self, max_size):
        self.stack = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.stack)

    def is_empty(self):
        return self.stack == [[]]

    def push_in(self, el):
        if len(self.stack[len(self.stack) - 1]) < self.max_size:
            self.stack[len(self.stack) - 1].append(el)
        else:
            self.stack.append([])
            self.stack[len(self.stack) - 1].append(el)

    def pop_out(self):
        result = self.stack[len(self.stack) - 1].pop()
        if len(self.stack[len(self.stack) - 1]) == 0:
            self.stack.pop()
        return result

    def get_val(self):
        return self.stack[len(self.stack) - 1]

    def stack_size(self):
        all_of_el = 0
        for st in self.stack:
            all_of_el += len(st)
        return all_of_el

    def stack_count(self):
        return len(self.stack)


plates = StackClass(2)
plates.push_in('1')
plates.push_in('2')
plates.push_in('3')
plates.push_in('4')
plates.push_in('5')
print(plates)
print(plates.stack_size(), plates.stack_count())
print(plates.pop_out(), plates)
