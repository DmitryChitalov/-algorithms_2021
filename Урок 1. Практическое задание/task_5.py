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
    def __init__(self, limit):
        self.plate_list = []
        self.all_plate_list = []
        self.max_length = limit

    def is_empty(self):
        return len(self.plate_list) == 0

    def size(self):
        return len(self.plate_list)

    def push(self, count):
        self.plate_list.append(count)
        if self.size() > self.max_length:
            self.all_plate_list.append(self.plate_list[:self.max_length])
            self.plate_list = self.plate_list[self.max_length:]

    def pop_out(self):
        return self.plate_list.pop()

    def peek(self):
        if self.plate_list:
            return self.plate_list[-1]
        else:
            print("Empty Stack")
        return None

    def stack_size(self):
        return self.all_plate_list + self.plate_list


if __name__ == '__main__':
    folding = PlatesStack(5)
    for i in range(1, 16):
        folding.push(i)
        if i % 5 == 0:
            folding.pop_out()
        print(folding.stack_size())
