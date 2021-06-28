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


class StackPlatesTest:
    def __init__(self):
        self.countofstack = 0
        self.maxinstack = 5
        self.elems = [[]]
        self.curr_stack = self.elems[self.countofstack]

    def clear(self):
        self.curr_stack = []
        self.elems = [[]]
        self.countofstack = 0
        return

    def empty(self):
        return self.elems[0] == []

    def error(self):
        print("Ошибка наполнения стека")
        exit()

    def push_into(self, el):
        if isinstance(el, int):                 # Тарелки то целые
            for i in range(el):
                if sum(self.curr_stack) == self.maxinstack:
                    self.elems.append([])
                    self.countofstack += 1
                    self.curr_stack = self.elems[self.countofstack]
                    self.curr_stack.append(1)
                else:
                    self.curr_stack.append(1)
        else:
            self.error()

    def del_one(self):
        result = self.curr_stack.pop()
        if (len(self.curr_stack) == 0) and (self.countofstack > 0):
            self.countofstack -= 1
            self.elems.pop()
            self.curr_stack = self.elems[self.countofstack]
        return result

    def countstacks(self):
        return self.countofstack + 1

    def totalplates(self):
        return self.countofstack * self.maxinstack + len(self.curr_stack)


if __name__ == '__main__':
    # Создаем экземпляр
    stack = StackPlatesTest()

    print("Пуст ли стек:", stack.empty())   # ДА
    # Наполняем
    stack.push_into(16)
    stack.push_into(50)
    stack.push_into(16)
    stack.push_into(4)

    print("Пуст ли стек:", stack.empty())   # НЕТ
    print("Всего тарелок:", stack.totalplates())
    print("Текущая стопка:", stack.countstacks())

    stack.del_one()
    print("Всего тарелок:", stack.totalplates())
    print("Текущая стопка:", stack.countstacks())

    # полная очистка
    stack.clear()
    print("Всего тарелок:", stack.totalplates())
    print("Текущая стопка:", stack.countstacks())
    print("Пуст ли стек:", stack.empty())   # ДА
