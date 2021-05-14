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


class Stack_of_plates:
    def __init__(self, size):
        self.all_plates = []
        self.current_list = []
        self.size = size

    def is_empty(self):
        return self.current_list == []

    def push_in(self):
        if len(self.current_list) == self.size:
            self.all_plates.append(self.current_list.copy())
            self.current_list.clear()
        self.current_list.append(f'Plates_{len(self.current_list) + len(self.all_plates) * self.size + 1}')

    def pop_out(self):
        if len(self.current_list) == 1:
            last_plates = self.current_list.pop()
            if len(self.all_plates):
                self.current_list = self.all_plates.pop()
            return last_plates
        if self.is_empty() is False:
            return self.current_list.pop()

        else:
            return None

    def get_val(self):
        return self.current_list[len(self.all_plates) - 1]

    def stack_size(self):
        return len(self.all_plates) * self.size + len(self.current_list)


if __name__ == '__main__':

    stack_plates = Stack_of_plates(4)
    stack_plates.push_in()
    stack_plates.push_in()
    stack_plates.push_in()
    stack_plates.push_in()
    stack_plates.push_in()
    stack_plates.push_in()
    stack_plates.push_in()
    print(stack_plates.pop_out())
    print(stack_plates.pop_out())
    print(stack_plates.get_val())
    stack_plates.push_in()
    stack_plates.push_in()
    stack_plates.push_in()
    stack_plates.push_in()
    stack_plates.push_in()
    stack_plates.push_in()
    print(stack_plates.stack_size())


