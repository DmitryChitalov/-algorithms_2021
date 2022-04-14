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


class PlateStack:

    def __init__(self, maxplates):
        '''
        Создаем объект класса
        '''
        self.stack = [[]]
        self.amount = 0
        self.maxplates = maxplates


    def add(self, amt=1):
        '''
        Добавляем amt тарелок
        '''
        for i in range(amt):
            if len(self.stack[len(self.stack) - 1]) < self.maxplates:
                self.stack[len(self.stack) - 1].append('\uFE3A')
            else:
                self.stack.append([])
                self.stack[len(self.stack) - 1].append('\uFE3A')
            self.amount += 1
        self.show()


    def remove(self, amt=1):
        '''
        Отнимаем amt тарелок
        '''
        for i in range(amt):
            if self.stack == [[]]:
                print('No plates here!')
                return None
            self.stack[len(self.stack) - 1].pop()
            if len(self.stack[len(self.stack) - 1]) == 0:
                self.stack.pop()
            self.amount -= 1
            if len(self.stack) == 0:
                self.stack = [[]]
        self.show()


    def rearrange(self, newmaxplates):
        '''
        Перераспределяем по новому количеству в стопке
        '''
        if 0 < newmaxplates < 100:
            self.maxplates = newmaxplates
        self.stack = [[]]
        amount = self.amount
        self.amount = 0
        self.add(amount)


    def show(self):
        '''
        Показываем красиво и наглядно
        '''
        if self.stack == [[]]:
            print('No plates here ¯\_(ツ)_/¯', end='\n\n')
            return None
        print(f'Here are your {self.amount} plates, {self.maxplates} in row, washed and shiny:')
        for i in range(len(self.stack[0])):
            for j in range(len(self.stack)):
                if len(self.stack[j]) >= self.maxplates - i or len(self.stack[j]) == len(self.stack[0]):
                    print('\uFE3A', end='')
            print('', end='\n')

        print('\n')


st = PlateStack(5)
st.show()
st.add(1)
st.add(13)
st.show()
st.add(21)
st.add()
st.rearrange(2)
st.rearrange(7)
st.rearrange(8)
st.remove(25)
st.rearrange(1)
st.remove(11)
st.remove()