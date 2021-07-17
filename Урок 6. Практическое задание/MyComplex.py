class ComplexValue:
    def __init__(self,re,im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexValue(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexValue(self.re * other.re - self.im * other.im, self.re * other.im + self.im*other.re)

    def __str__(self):
        return f"(Real:{self.re}, Imagine:{self.im})"

class ComplexValueSlot:
    __slots__ = ['re','im']
    def __init__(self,re,im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexValue(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexValue(self.re * other.re - self.im * other.im, self.re * other.im + self.im*other.re)

    def __str__(self):
        return f"(Real:{self.re}, Imagine:{self.im})"

