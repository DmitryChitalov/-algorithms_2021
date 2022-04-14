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


class StackOfPlates():
    '''
    Базовый стек с методами (винзу демонстрация его работы).
    Для реализации многостопочного стека этот класс мы и будем наслед овать.
    '''
    def __init__(self, num=10):
        self.stack = []
        self.maxnum = num

    def stack_is_over(self):
        return len(self.stack) < self.maxnum

    def stack_is_empty(self):
        return len(self.stack)

    def add_plate(self, name='Тарелка') -> bool:
        if self.stack_is_over():
            self.stack.append(f'{name} {self.stack_is_empty()}')
            return True
        return False

    def pop_plate(self) -> str:
        if not self.stack_is_empty():
            return False
        return self.stack.pop()


class ShelfOfStacks1(StackOfPlates):
    '''
    Оргазизуем список со стеком стопок, каждая стопка свой стек.
    Реализована часть интерфейса: положить/извлечь значение
    '''

    def __init__(self, num=10):
        super().__init__()
        self.stack = [[]]
        self.maxnum = num
        self.cnt = 0

    def stack_is_over(self):
        return len(self.stack[len(self.stack) - 1]) < self.maxnum

    def stack_is_empty(self):
        # print (len(self.stack[len(self.stack)-1]))
        return len(self.stack[len(self.stack) - 1])

    def shelf_is_empty(self):
        return self.stack == []

    def plate_count(self):
        self.cnt += 1
        return self.cnt

    def add_plate(self, name='Тарелка') -> bool:
        if self.stack_is_over():
            self.stack[len(self.stack) - 1].append(f'{name} {self.plate_count()}')
        else:
            self.stack.append([f'{name} {self.plate_count()}'])
        return True

    def pop_plate(self) -> str:
        if self.stack[len(self.stack) - 1] == []:
            self.stack.pop()
        if len(self.stack):
            return self.stack[len(self.stack) - 1].pop()
        return False


class ShelfOfStacks2(StackOfPlates):
    '''
    В основе положим список объектов типа StackOfPlates
    Методы частично наследуем.
    Без реализвации, слишком много ушло времени на первый релиз
    '''
    pass


print(str.center('ПЕРВЫЙ ОБЪЕКТ', 40, '*'))
st = StackOfPlates()
while st.add_plate():
    print(st.stack_is_empty(), end=' ')
print('\nСтек в начале', st.stack)
while st.stack_is_empty():
    print(st.pop_plate(), end=' ')
print('\nСтек в конце', st.stack)


print(str.center('ВТОРОЙ ОБЪЕКТ', 40, '*'))
shelf1 = ShelfOfStacks1(num=3)  # разбираем в стопочки по 3 штучки
for i in range(7):
    shelf1.add_plate()
print(shelf1.stack)

while True:
    print(shelf1.pop_plate(), end=' ')  # достаем тарелочки из шкафа в обратном порядке
    if shelf1.shelf_is_empty():
        break

# последним печатается False, ну и фиг с ним - оставим на доработки.
