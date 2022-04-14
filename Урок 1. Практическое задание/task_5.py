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


# Данная реализация создаёт список внутри списка объекта при достижении лимита 100.
class StackClass:
    def __init__(self):
        self.elem = [[]]
        self.num = 0
        self.i = 0

    def is_empty(self):
        return self.elem == [[]]

    def push_in(self, el):
        if self.num < 100:
            self.elem[self.i].append(el)
            self.num += 1
        elif self.num == 100:
            self.elem.append([])
            self.i += 1
            self.num = 1
            self.elem[self.i].append(el)

    def pop_out(self):
        if self.num > 0:
            self.num -= 1
            return self.elem[self.i].pop()
        elif self.num == 0 and self.i > 0:
            self.i -= 1
            self.elem.pop()
            return self.elem[self.i].pop()

    def get_val(self):
        return self.elem[self.i][len(self.elem[self.i]) - 1]

    def stack_size(self):
        return (len(self.elem) - 1) * 100 + len(self.elem[self.i])

    def stack_size_list(self):
        return self.i + 1


if __name__ == '__main__':
    obj = StackClass()
    x = 102789
    y = 90
    while x > 0:
        obj.push_in(10)
        x -= 1
    print(obj.stack_size())
    while y > 0:
        obj.pop_out()
        y -= 1
    print(obj.stack_size())
    print(obj.get_val())
    obj.push_in('Hello')
    print(obj.get_val())
    print(obj.stack_size_list())
