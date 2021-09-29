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
    def __init__(self):
        self.first_stack = []
        self.second_stack = []
        self.third_stack = []

    def add_elem(self, elem):
        if len(self.first_stack) < 5:
            self.first_stack.append(elem)
        elif len(self.second_stack) < 5:
            self.second_stack.append(elem)
        elif len(self.third_stack) < 5:
            self.third_stack.append(elem)
        else:
            print('Стек переполнен')

    def show_stack(self):
        print(self.first_stack, self.second_stack, self.third_stack, sep='\n')

    def pop_out(self, num_stack):
        if num_stack == 1 and self.first_stack:
            return self.first_stack.pop()
        elif num_stack == 2 and self.second_stack:
            return self.second_stack.pop()
        elif num_stack == 3 and self.third_stack:
            return self.third_stack.pop()
        else:
            return 'Unknow'


obj = StackClass()  # объект содержит 3 стека
obj.show_stack()
obj.add_elem('dvfsd')
obj.add_elem('rg')
obj.add_elem(5)
obj.add_elem(False)
obj.add_elem(456)
obj.add_elem(123.45)
obj.add_elem('vfvf')
obj.show_stack()
# наполнили объект, при достежении 5 значений в первом стеке заполняется второй
print(obj.pop_out(1))
# забираем объект с первого стека
print(obj.pop_out(2))
# можно забрать со второго стека

obj.show_stack()

obj.add_elem(obj.pop_out(2))
# можно перенести с одного стека на другой(на первый, если он не заполнен)

obj.show_stack()
