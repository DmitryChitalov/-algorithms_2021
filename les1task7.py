class DequeClass:
    def __init__(self):
        self.elements = []

    def size(self):
        return len(self.elements)

    def add1(self, elem):
        self.elements.append(elem)

    def add2(self, elem):
        self.elements.insert(0, elem)


    def pop1(self):
        return self.elements.pop()

    def pop2(self):
        return self.elements.pop(0)


def is_palindrome(s):
    obj = DequeClass()
    new_s = s.replace(' ', '')
    for i in new_s:
        obj.add2(i)

    equal = True

    while obj.size() > 1 and equal:
        first = obj.pop1()
        last = obj.pop2()
        if first != last:
            equal = False

    return equal

new_string = input("Введите сторчку для проверки на палиндром: ")
print(is_palindrome(new_string))