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


class PlatesStack:
    def __init__(self, max_size):
        self.items = [[]]
        self.max_size = max_size

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if len(self.items[-1]) >= self.max_size:
            self.items.append([])
        self.items[-1].append(item)
        return self.items

    def pop(self):
        if not self.is_empty():
            self.items[-1].pop()

    def count_elements(self):
        summ = 0
        for item in self.items:
            summ += len(item)
        return f'Total amount: {summ}\n' \
               f'Num of stacks: {len(self.items)}'


if __name__ == '__main__':
    plates = PlatesStack(5)
    for el in range(0, 30):
        plates.push(el)
    print(plates.count_elements(), '\n', plates.items)
    plates.pop()
    print(plates.count_elements(), '\n', plates.items)
