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
        self.stack = []
        self.max_size = max_size

    def stack_count(self):
        return len(self.stack)

    def stack_size(self):
        sum = 0
        for stack in self.stack:
            sum += len(stack)
        return sum

    def push(self, item):
        if len(self.stack[len(self.stack) - 1]) < self.max_size:
            self.stack[len(self.stack) - 1].append(item)
        else:
            self.stack.append([])
            self.stack[len(self.stack) - 1].append(item)

    def pop(self):
        result = self.stack[len(self.stack) - 1].pop()
        if len(self.stack[len(self.stack) - 1]) == 0:
            return result

    def get_value(self):
        return self.stack[len(self.stack) - 1]

    def __str__(self):
        return str(self.stack)


if __name__ == '__main__':
    plates = StackClass(3)
    plates.push('Тарелка_1')
    plates.push('Тарелка_2')
    plates.push('Тарелка_3')
    plates.push('Тарелка_4')
    plates.push('Тарелка_5')
    plates.push('Тарелка_6')
    print(plates)
    print(plates.pop())
    print(plates.get_value())
    print(plates.stack_size())
    print(plates.stack_count())
    print(plates)
