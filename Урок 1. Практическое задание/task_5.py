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
class Error (Exception):
    pass

class ValueTooLargeError (Error):
    pass

class ValueTooSmallError (Error):
    pass

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

class Shot(StackClass):
    def __init__(self, max_size = 3):
        super ().__init__ ()
        self.max_size_stack = max_size

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)
        if self.stack_size () >= self.max_size_stack:
            raise ValueTooLargeError

    def pop_out(self):
        if self.is_empty():
            raise ValueTooSmallError
        else:
            return self.elems.pop ()




if __name__ == '__main__':
    max_size = 3
    reduction_size = 25
    stack_me = []
    my_list  = [10, 'code', False,
                11, 'code+', False,
                12, 'code++', False,
                13, 'code+++', False,
                14, 'code++++', False,
                15, 'code+++++', False,
                16, 'code++++++', False,
                17, 'code+++++++', False,
                18, 'code++++++++', False,
                ]
    count = 0
    stack_me.append (Shot (max_size))
    for value in my_list:
        try:
            stack_me[count].push_in (value)
        except ValueTooLargeError:
            count += 1
            if count < len(my_list) / max_size:
                stack_me.append (Shot (max_size))



    for stack in stack_me:
        print(stack.elems)

    # length_stack_me = len(stack_me)
    length_stack_me = reduction_size // max_size

    for index in range(length_stack_me):
        for index_two in range(stack_me[length_stack_me - (index + 1) ].stack_size()):
            print(f'Вытаскиваем из стопки', (length_stack_me - index), ' ',
                  stack_me[length_stack_me - (index + 1)].pop_out())
        stack_me.pop()

    print(f'Содержание стэка', stack_me)




''' 
    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)

    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())  # -> 5.5

    # узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 4

    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.4

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 5.5

    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 3
'''