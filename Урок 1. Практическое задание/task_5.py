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
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


class PlatesStack:
    def __init__(self, max_val):
        self.max_val = max_val
        self.stacks = []
        self.plates = []

    def push(self, plate):
        if len(self.plates) < self.max_val:
            self.plates.append(plate)
        else: 
            self.stacks.append(self.plates)
            print('here\'s too much plates. let\'s make new stack')
            self.plates = []

    def stacksnum(self):
        return len(self.stacks)

    def stackcontained(self):
        for stack in self.stacks:
            print(stack)

    def popout(self):
        poped = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return poped


    def present_stack_eval(self):
        return len(self.stacks[-1])




sm = PlatesStack(9)
print(sm.stacksnum())
sm.push('red')
sm.push('BLACK')
sm.push('GREEN')
sm.push('yellow')
sm.push('purple')
sm.push('BLACK')
sm.push('GREEN')
sm.push('yellow')
sm.push('BLACK')
sm.push('GREEN')
sm.push('yellow')
sm.push('white')
sm.push('yellow')
sm.push('red')
sm.push('yellow')
sm.push('purple')
sm.push('white')
sm.push('yellow')
sm.push('red')
sm.push('yellow')
sm.push('purple')
sm.push('white')
sm.push('yellow')
sm.push('red')
sm.push('yellow')
sm.push('purple')
sm.push('white')
sm.push('yellow')
sm.push('red')
sm.push('yellow')
sm.push('purple')
sm.push('white')
sm.push('yellow')
sm.push('red')
sm.push('yellow')
sm.push('purple')
sm.push('white')
sm.push('yellow')
sm.push('red')
sm.push('yellow')
sm.push('purple')
sm.push('white')
sm.push('yellow')
sm.push('red')
sm.push('yellow')
sm.push('purple')
sm.push('white')
sm.push('yellow')

print(sm.stacksnum())
print(sm.stackcontained())
print(sm.present_stack_eval())
print(sm.popout())
print(sm.present_stack_eval())

