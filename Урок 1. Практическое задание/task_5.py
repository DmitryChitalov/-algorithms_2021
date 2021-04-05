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


class Stack:

    def __init__(self):
        self.elems = []

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        return self.elems.pop()

    def get_last_elem(self):
        return self.elems[len(self.elems) - 1]

    def get_size(self):
        return len(self.elems)

    def is_empty(self):
        return self.elems == []


class StackOfPlates(Stack):
    max_size_of_plates_stack = 0

    def __init__(self):
        print('Создание новой стопки тарелок')
        super().__init__()
        self.current_size = 0

    def push(self, plate):
        if self.current_size == self.max_size_of_plates_stack:
            # print('Стопка уже полная!')
            return False

        Stack.push(self, plate)
        self.current_size += 1
        return True


def count_of_stacks(max_size_of_plates_stack, total_count_of_plates):
    StackOfPlates.max_size_of_plates_stack = max_size_of_plates_stack

    if total_count_of_plates % max_size_of_plates_stack == 0:
        return int(total_count_of_plates / max_size_of_plates_stack)

    return total_count_of_plates // max_size_of_plates_stack + 1


def forming_stack_of_plates(max_size_of_plates_stack, total_count_of_plates):
    stacks_count = count_of_stacks(max_size_of_plates_stack, total_count_of_plates)

    stack_of_plates_storage = []
    for i in range(stacks_count):
        stack_of_plates_storage.append(StackOfPlates())

        if i == stacks_count - 1:
            for j in range(16 - i * max_size_of_plates_stack):
                stack_of_plates_storage[i].push(f'plate{j + 1}')
                print(f'Кладем тарелки в стопку {i + 1}')
            break
        else:
            for j in range(StackOfPlates.max_size_of_plates_stack):
                while stack_of_plates_storage[i].push(f'plate{j + 1}'):
                    print(f'Кладем тарелки в стопку {i + 1}')
                else:
                    print(f'Стопка {i + 1} заполнилась! Небходимо сформировать новую..')
                    break

    return stack_of_plates_storage


storage = forming_stack_of_plates(5, 16)

print(f'\nКоличество стопок тарелок: {len(storage)}')
for i in range(len(storage)):
    print(f'Количество тарелок в стопке с номером {i + 1}: {storage[i].get_size()}')
print('\n')

storage = forming_stack_of_plates(5, 15)
print(f'\nКоличество стопок тарелок: {len(storage)}')
for i in range(len(storage)):
    print(f'Количество тарелок в стопке с номером {i + 1}: {storage[i].get_size()}')
