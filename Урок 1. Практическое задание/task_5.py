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


class Stack:
    __list_of_stacks = list()
    __counter = -2

    def __init__(self, n: int):
        self.__size = n
        self.stack = list()
        Stack.__counter += 1

    def push(self, el):
        if not Stack.__list_of_stacks:
            Stack.__list_of_stacks.append(Stack(self.__size))
        elif len(Stack.__list_of_stacks[Stack.__counter].stack) >= self.__size:
            Stack.__list_of_stacks.append(Stack(self.__size))
        Stack.__list_of_stacks[Stack.__counter].stack.append(el)

    @staticmethod
    def pop():
        if not Stack.__list_of_stacks:
            print('Стек пуст')
            return
        else:
            Stack.__list_of_stacks[Stack.__counter].stack.pop()

    def __str__(self):
        string = ''
        for element in Stack.__list_of_stacks:
            string += '\n'
            for stack in element.stack:
                string += str(stack)
                string += '\n'
        string += '\n'
        return string


stack_1 = Stack(3)
stack_1.push(1)
stack_1.push(2)
stack_1.push(3)
stack_1.push(4)
stack_1.push(5)
stack_1.pop()
stack_1.push(5)
stack_1.push(6)
stack_1.push(7)
print(stack_1)
