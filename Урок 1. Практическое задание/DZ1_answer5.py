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
"""

class StackClass:
    def __init__(self, max_elems):
        self.elems = [[]]
        self.max_elems = max_elems
        #self.multi_elems = []

    def is_empty(self):                                 #информация о пустоте стека (пустой/полный)
        return self.elems[0] == []

    def push_in(self, el):                              #наполнение стека новым элементом (добавление в конец списка)
        if len(self.elems[-1]) == self.max_elems:
            self.elems.append([])
            self.elems[-1].append(el)
        else:
            self.elems[-1].append(el)

    def pop_out(self):                                  #удаление последнего элемента (самого позднего по времени)
       pop_elem = self.elems[-1].pop()
       if self.elems[-1] == []:
           del self.elems[-1]
       return pop_elem

    def get_val(self):                                  #получение последнего элемента (самого позднего по времени)
        if self.is_empty():
            return None
        else:
            return self.elems[-1][-1]

    def stack_size(self):                               #размер стека (общий, кол-во элементов во всех маленьких стопках)
        len_stack = 0
        for i in self.elems:
            len_stack += len(i)
        return len_stack

b = StackClass(7)

print(b.is_empty())
print(b.stack_size())
print(b.get_val())
b.push_in(1)
b.push_in(2)
b.push_in(3)
b.push_in(4)
b.push_in(5)
b.push_in(6)
b.push_in(7)
b.push_in(8)
b.push_in(9)
b.push_in(10)
b.push_in(11)
b.push_in(12)
b.push_in(13)
b.push_in(14)
b.push_in(15)
b.push_in(16)
b.push_in(17)
print(b.elems)
print(b.is_empty())
print(b.stack_size())
print(b.get_val())
b.pop_out()
b.pop_out()
b.pop_out()
b.pop_out()
print(b.elems)
print(b.is_empty())
print(b.stack_size())
print(b.get_val())