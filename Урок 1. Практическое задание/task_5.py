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


# первый вариант решения (видимо не совсем правильный относительно ТЗ, но раз сделал, то пусть будет)
class Plates:
    def __init__(self, plates_num):
        self.plates_num = int(plates_num)

    def make_order(self, plates_in_stack):
        stacks = ''
        for i in range(int(self.plates_num / plates_in_stack)):
            stacks += f'{"0" * plates_in_stack}\n'
        stacks += f'{"0" * (self.plates_num % plates_in_stack)}'
        return f'{stacks}'


# второй вариант (выводит список состоящий из элементов класса StackClass)
class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def __str__(self):
        return f'{self.elems}'

    def make_order(self, plates_num, plates_in_stack):
        objs = [StackClass() for i in range(int(plates_num / plates_in_stack))]
        last_stack = StackClass()
        for obj in objs:
            obj.push_in('0' * plates_in_stack)
        last_stack.push_in('0' * (plates_num % plates_in_stack))
        objs.append(last_stack)
        for obj in objs:  # визуальный вывод словоря (просто для наглядности)
            print(obj)
        return objs


a = StackClass()
print(a.make_order(45, 10))

b = Plates(45)  # создаём элемент класса тарелки
print(b.make_order(10))  # раскладываем тарелки по стопкам
