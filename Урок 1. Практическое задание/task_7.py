"""
Задание 7.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)

Примечание:
Вам не нужно писать код с нуля. Вам нужно доработать пример с урока.
"""

class DequeClass:
    def __init__(self):
        self.elems = []
      
    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)

    def myprint(self):
        print(self.elems)
      
    
poli = 'молоко делили ледоколом'
new_str = DequeClass()

for el in poli:
  if el == ' ':
    continue
  else:
     new_str.add_to_rear(el)

new_str.myprint()
still_equal = True

while new_str.size() > 1 and still_equal:
  first = new_str.remove_from_front()
  last = new_str.remove_from_rear()
  if first != last:
      still_equal = False

print (still_equal)
