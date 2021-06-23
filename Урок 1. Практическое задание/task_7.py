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

    def my_print(self):
        print(self.elems)


phrase = 'молоко делили ледоколом'
new_str = DequeClass()

for el in phrase:
    if el == ' ':
        continue
    else:
        new_str.add_to_rear(el)

new_str.my_print()
still_equal = True

while new_str.size() > 1 and still_equal:
    first = new_str.remove_from_front()
    last = new_str.remove_from_rear()
    if first != last:
        still_equal = False

print(still_equal)
