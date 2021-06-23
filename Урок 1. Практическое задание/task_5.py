class PlateClass:
    def __init__(self, size):
        self.elems = []
        self.size = size

    def __str__(self):
        return str(self.elems)

    def input_plates(self, el):
        if len(self.elems) == 0:
            self.elems.append([])
        if len(self.elems[-1]) < self.size:
            self.elems[-1].append(el)
        else:
            self.elems.append([])
            self.elems[-1].append(el)

    def remove_plate(self):
        new_plates = self.elems[-1].pop()
        if len(self.elems[-1]) == 0:
            self.elems.pop()
        return new_plates

    def stack_count(self):
        return len(self.elems)

    def plate_count(self):
        if len(self.elems) == 0:
            return 'Ups, you have no plates.'
        result = self.size * (len(self.elems) - 1) + len(self.elems[-1])
        return result


plates = PlateClass(5)

print(plates.plate_count())
plates.input_plates('Plate1')
plates.input_plates('plate2')
plates.input_plates('plate3')
plates.input_plates('plate4')
plates.input_plates('plate5')
plates.input_plates('plate6')
plates.input_plates('plate7')
print(plates.stack_count())
print(plates.plate_count())
print(plates)
print(plates.remove_plate())
print(plates.remove_plate())
print(plates)
print(plates.stack_count())
print(plates.plate_count())
