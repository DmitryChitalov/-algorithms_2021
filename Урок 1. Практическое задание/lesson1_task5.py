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


class PlateStack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stacks = []

    def push(self, item):  # O(1)
        sl = len(self.stacks)
        if sl == 0 or len(self.stacks[sl - 1]) == self.stack_size:
            new_stack = []
            self.stacks.append(new_stack)
            new_stack.append(item)
            return
        self.stacks[sl - 1].append(item)

    def pop(self):  # O(1)
        sl = len(self.stacks)
        if len(self.stacks) == 0:
            return None
        stack = self.stacks[sl - 1]
        result = stack.pop()
        if len(stack) == 0:
            self.stacks.pop()
        return result

    def stack_count(self):  # O(1)
        return len(self.stacks)

    def size(self):  # O(n)
        return sum(map(lambda x: len(x), self.stacks))


plates = PlateStack(3)
plates.push('1')
plates.push('2')
plates.push('3')
plates.push('4')
plates.push('5')
plates.push('6')
plates.push('7')
plates.push('8')
plates.push('9')
plates.push('10')
print(f'Stack count {plates.stack_count()}')
print(f'Total size {plates.size()}')
print(plates.pop())
print(plates.pop())
print(plates.pop())
print(plates.pop())
print(plates.pop())
print(plates.pop())
print(plates.pop())
print(plates.pop())
print(plates.pop())
print(plates.pop())
print(plates.pop())
print(plates.pop())
plates.push('1')
plates.push('2')
plates.push('3')
plates.push('4')
plates.push('5')
print(plates.pop())
print(plates.pop())
print(plates.pop())