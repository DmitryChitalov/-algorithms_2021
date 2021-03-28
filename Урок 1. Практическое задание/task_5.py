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


class PlateStack:
	def __init__(self, limit):
		self.limit = limit
		self.__stacks = []

	def add(self, number_of_plates = 1):
		for i in range(number_of_plates):
			if len(self.__stacks) == 0 or len(self.__stacks[-1]) == self.limit:
				self.__stacks.append(Stack())
			self.__stacks[-1].add('Тарелка')

	def remove(self, number_of_plates = 1):
		for i in range(number_of_plates):
			if len(self.__stacks) == 0:
				return
			self.__stacks[-1].pop()
			if len(self.__stacks[-1]) == 0:
				self.__stacks.pop()

	def __str__(self):
		s = ' '.join([str(len(stack)) for stack in self.__stacks])
		return 'Количество стопок: ' + str(len(self.__stacks)) + '\nСостояние стопок: ' + s + '\n'


class Stack:
	def __init__(self):
		self.__lst = []

	def add(self, element):
		self.__lst.append(element)

	def pop(self):
		return self.__lst.pop()

	def __len__(self):
		return len(self.__lst)


# Задаем количество тарелок в стопке
print("В одной стопке 4 тарелки\n")
plate_stack = PlateStack(4)

print("Добавялем 5 тарелок в стопку")
plate_stack.add(5)
print(plate_stack)

print("Добавялем 13 тарелки в стопки")
plate_stack.add(13)
print(plate_stack)

print("Удаляем 11 тарелок из стопки")
plate_stack.remove(7)
print(plate_stack)
