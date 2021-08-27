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
Отдельные стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class StackOfPlates:
    def __init__(self, stack_height):
        self.elems = [[]]
        self.stack_height = stack_height

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, plate):
        if len(self.elems[len(self.elems) - 1]) < self.stack_height:
            self.elems[len(self.elems) - 1].append(plate)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(plate)

    def pop_out(self):
        if len(self.elems[len(self.elems) - 1]) > 0:
            self.elems[len(self.elems) - 1].pop()
        else:
            self.elems.remove(self.elems[len(self.elems) - 1])
            self.elems[len(self.elems) - 1].pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1][-1]

    def stack_size(self):
        return len(self.elems)


my_stack = StackOfPlates(2)
my_stack.push_in('plate_1')
my_stack.push_in('plate_2')
my_stack.push_in('plate_3')
my_stack.push_in('plate_4')
my_stack.push_in('plate_5')
my_stack.push_in('plate_6')
my_stack.push_in('plate_7')
my_stack.push_in('plate_8')

print(my_stack.elems)

my_stack.pop_out()
my_stack.pop_out()
my_stack.pop_out()
my_stack.pop_out()
my_stack.pop_out()
my_stack.pop_out()
my_stack.pop_out()

print(my_stack.elems)

my_stack.push_in('plate_2')
my_stack.push_in('plate_3')

print(my_stack.get_val())

print(my_stack.stack_size())

# Изначальный вариант. Хотелось бы понять как правильно решить именно таким образом:

prefix_list = ['second', 'third', 'fourth', 'fifth']
ending = '_stack'


def new_name():
    for item in prefix_list:
        new_stack = item + ending
        prefix_list.pop(prefix_list.index(item))
        return new_stack


class StackOfPlates:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if self.is_full is True:
            print('Cтопка достигла максимальной высоты')
            second_stack = StackOfPlates()
            second_stack.new_name()
            second_stack.elems.append(el)
        else:
            self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    @property
    def is_full(self):
        if len(self.elems) == 3:
            return True
        else:
            return False


first_stack = StackOfPlates()

print(first_stack.is_empty())
first_stack.push_in('1')
first_stack.push_in('2')
first_stack.push_in('3')
print(first_stack.elems)
print(first_stack.is_full)
first_stack.push_in('4')
print(second_stack.elems)

