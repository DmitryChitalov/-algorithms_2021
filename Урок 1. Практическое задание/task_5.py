"""
Задание 5.
Задание на закрепление навыков работы со стеком

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


class PlateStack:

    # Создаём стопки тарелок, как список списков
    # При создании задаём максимальное количество тарелок в одной стопке
    def __init__(self, max_plate_count: int):
        self.stacks = []
        self.max_plate_count = max_plate_count

    def is_empty(self):
        return self.stacks == []

    # добавляем новый элемент в последнюю стопку
    # если нет стопок или текущая стопка полная, добавляем новую
    def push_in(self, el):
        if self.is_empty() or len(self.stacks[self.stacks_count-1]) == self.max_plate_count:
            self.stacks.append([])
        self.stacks[self.stacks_count-1].append(el)

    # удаляем элемент из последней стопки
    # если в стопке не осталось элементов, удаляем её
    def pop_out(self):
        item = self.stacks[self.stacks_count-1].pop()
        if not self.stacks[self.stacks_count-1]:
            del self.stacks[self.stacks_count-1]
        return item

    # свойство, количество имеющихся стопок
    @property
    def stacks_count(self):
        return len(self.stacks)

    # предполагая, что все тарелки одинаковые, можно брать тарелку
    # из любой стопки и класть на верх любой, не полной

    # забираем тарелку из произвольной стопки
    # если стопка опустела, удаляем её из списка стопок
    # если номер стопки больше количества стопок, удаляем элемент из последней
    def pop_from(self, stack_num):
        if stack_num >= self.stacks_count:
            return self.pop_out()
        item = self.stacks[stack_num].pop()
        if not self.stacks[stack_num]:
            del self.stacks[stack_num]
        return item

    # добавляем тарелку в первую неполную стопку
    # если таких нет, добавляем тарелку в последнюю стопку
    def push_at_incomplete(self, el):
        for num in range(self.stacks_count):
            if len(self.stacks[num]) != self.max_plate_count:
                self.stacks[num].append(el)
                break
        else:
            self.push_in(el)


if __name__ == '__main__':

    # создаём экземпляр класса "стопка тарелок"
    # максимум 3 тарелки в стопке
    plates = PlateStack(3)

    # заполняем элементами
    for i in range(10):
        plates.push_in(i)

    # выводим на экран получившиеся списки
    for i in range(plates.stacks_count):
        print(plates.stacks[i])

    # взять последний элемент
    print(plates.pop_out())

    # добавить два элемента
    plates.push_in(10)
    plates.push_in(11)

    # поочерёдно берём тарелки из 2й стопки
    plates.pop_from(2)
    plates.pop_from(2)
    plates.pop_from(2)

    # добавляем тарелки в неполные стопки
    plates.push_at_incomplete(100)
    plates.pop_from(0)
    plates.push_at_incomplete(100)

    # Результат:
    for i in range(plates.stacks_count):
        print(plates.stacks[i])
