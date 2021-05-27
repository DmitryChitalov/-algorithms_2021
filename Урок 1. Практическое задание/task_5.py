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
    def __init__(self, max_size: int):
        self.stacks = []
        self.max_size = max_size

    def is_empty(self):
        return self.stacks == []

    def pop_out(self):
        return self.stacks.pop(0)

    def get_val(self):
        return self.stacks[0]

    def stack_size(self):
        return len(self.stacks)

    def push_in(self, element):
        if self.is_empty() or len(self.stacks[self.stacks_count - 1]) == self.max_size:
            self.stacks.append([])
        self.stacks[self.stacks_count - 1].append(element)

    @property
    def stacks_count(self):
        return len(self.stacks)


if __name__ == '__main__':

    plates = StackClass(4)

    # заполняем элементами
    for i in range(15):
        plates.push_in(i)

    # plates.pop_out()
    # print(plates.get_val())

    # выводим на экран получившиеся списки
    for i in range(plates.stacks_count):
        print(plates.stacks[i])