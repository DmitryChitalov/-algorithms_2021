"""Задание 5. Задание на закрепление навыков работы со стеком.

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

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
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class Stacks:
    def __init__(self):
        self.subjects = []

    def vacant(self):
        return self.subjects != []

    def add_to(self, item):
        list_blank = []
        if len(self.subjects) == 0 or len(self.subjects[-1]) == 4:
            self.subjects.append(list_blank)
        if len(self.subjects[-1]) < 4:
            self.subjects[-1].append(item)

    def viewing(self, stack):
        if stack == 'all':
            return self.subjects
        elif 'int' in str(type(stack)):
            return self.subjects[::-1][stack]
        elif '[' in stack:
            stack = stack[1:-1]
            stack = stack.split('][')
            return self.subjects[::-1][int(stack[0])][::-1][int(stack[1])]

    def rate_stack(self, stack):
        return len(stack)

    def item_out(self, item):
        if '[' in item:
            item = item[1:-1]
            return self.subjects[int(item[0])].pop()


if __name__ == '__main__':
    SCS_OBJECT = Stacks()

    print(SCS_OBJECT.vacant())  # смотрим есть ли стеки
    print()
    # наполняем стеки
    SCS_OBJECT.add_to(1)
    SCS_OBJECT.add_to(2)
    SCS_OBJECT.add_to(3)
    SCS_OBJECT.add_to(4)

    print(SCS_OBJECT.vacant())  # видим что есть как минимум 1 стек
    print()
    SCS_OBJECT.add_to(5)
    SCS_OBJECT.add_to(6)
    SCS_OBJECT.add_to(7)
    SCS_OBJECT.add_to(8)

    SCS_OBJECT.add_to(9)
    SCS_OBJECT.add_to(10)

    # просматриваем все стеки в виде списка списков
    print(SCS_OBJECT.viewing('all'))
    print()
    # просматриваем конкретный стек в виде списка
    print(SCS_OBJECT.viewing(0))  # выводится первая с конца списка стопка!
    print()
    # просматриваем конкретный элемент из конкретного стека
    # выводится верхний элемент стопки т е последний в списке!
    print(SCS_OBJECT.viewing('[0][0]'))
    print()
    # выводим размер конкретного стека
    print(SCS_OBJECT.rate_stack(SCS_OBJECT.viewing(1)))
    print()
    # отобразим стек в виде стопки
    for item in SCS_OBJECT.viewing(2)[::-1]:
        print(item)
    print()
    # убираем элемент с вершины стека и возвращаем его значение
    print(SCS_OBJECT.item_out('[0]'))
