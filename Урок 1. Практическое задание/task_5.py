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


STACK_LEN = 5


class StackOfPlates:
    def __init__(self):
        self.stack = {}
        self.stack_key = 0

    def append(self, value):
        if len(self.stack) == 0:
            self.stack_key = 0
            self.stack[self.stack_key] = [value]
        else:
            use_stack = self.stack[self.stack_key]
            if len(use_stack) < STACK_LEN:
                use_stack.append(value)
            else:
                self.stack_key = len(self.stack)
                self.stack[len(self.stack)] = [value]

    def pop(self):
        if len(self.stack) == 0:
            print('Stack of plates empty')
            return
        use_stack = self.stack[self.stack_key]
        if len(use_stack) != 0:
            return use_stack.pop()
        else:
            del self.stack[self.stack_key]
            self.stack_key = len(self.stack) - 1
            if len(self.stack) == 0:
                print('Stack of plates empty')
                return
            use_stack = self.stack[self.stack_key]
            return use_stack.pop()
