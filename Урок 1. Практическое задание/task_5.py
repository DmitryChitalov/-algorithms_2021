"""
Задание 5.

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков. Создание нового стека происходит
при достижении предыдущим стеком порогового значения. Реализуйте по аналогии с примером,
рассмотренным на уроке, необходимые методы, для реализации этой структуры, добавьте новые методы
(не рассмотренные в примере с урока) для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях.
"""


# Код написанный на уроке с дополнениями --------------------------------------
class StackClass:
    def __init__(self):
        self.elems = []
        self.stacks = []  # Добавлен список "стопок тарелок" - стеков
        self.counter = 1  # Добавлен счетчик "стопок тарелок" - стеков

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в начале списка"""
        self.elems.insert(0, el)

    def pop_out(self, number_stack):
        '''
        Метод класса удаляет первый элемент стека

        :param number_stack (int): номер стека
        :return (class arg).pop(): удаляет первый элемент указанного стека
        '''
        if number_stack <= len(self.stacks):
            return self.stacks[number_stack - 1].pop(0)
        else:
            return self.elems.pop(0)

    def get_val(self):
        return self.elems[0]

    def stack_size(self):
        return len(self.elems)

    def quantity_stack(self):
        '''
        Метод класса добавляет заполненный стек в список стеков

        :return (str): сообщение о наполнении стека
        '''
        self.stacks.append(self.elems)
        return f'{SC_OBJ.counter}-я cтопка наполнена, {SC_OBJ.stack_size()} тарел.'


if __name__ == '__main__':
    SC_OBJ = StackClass()
    while True:
        print('-' * 50)
        plate = input('Для выхода введите => q\n'
                      'Добавить тарелку   => 1\n'
                      'Убрать тарелку     => 0\n'
                      'Введиете значение: ')
        if plate == 'q':
            print(f'Наши стопки: {SC_OBJ.stacks} + {SC_OBJ.stack_size()} тарел.')
            break

        if plate == '1':
            SC_OBJ.push_in(plate)

            if SC_OBJ.stack_size() == 3:        # Количество тарелок в стопке (стеке)
                print(SC_OBJ.quantity_stack())
                SC_OBJ.counter += 1
                SC_OBJ.elems = []
                continue

            print(f'{SC_OBJ.counter}-я стопка: {SC_OBJ.stack_size()} тарел.')

        if plate == '0':
            number_stack = input('Введите номер стопки с тарелками: ')
            SC_OBJ.pop_out(int(number_stack))
            print(f'Наши стопки: {SC_OBJ.stacks} + {SC_OBJ.stack_size()} тарел.')


