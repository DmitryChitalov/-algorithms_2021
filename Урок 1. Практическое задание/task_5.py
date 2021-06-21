class PlateClass:
    def __init__(self, size):
        self.elems = []
        self.size = size

    def __str__(self):
        return str(self.elems)

    def inputplates(self, el):
      if len(self.elems) == 0:
         self.elems.append([])
      if len(self.elems[-1]) < self.size:
         self.elems[-1].append(el)
      else:
         self.elems.append([])
         self.elems[-1].append(el)

    def removeplate(self):
      newplates = self.elems[-1].pop()
      if len(self.elems[-1])==0:
          self.elems.pop()
      return newplates

    def steckcount(self):
        return len(self.elems)
    
    def platecount(self):
        if len(self.elems) == 0:
            return 'Ups, you have no plates.'
        result = self.size * (len(self.elems)-1) + len(self.elems[-1])
        return result

plates = PlateClass(5)

print (plates.platecount())
plates.inputplates('Plate1')
plates.inputplates('plate2')
plates.inputplates('plate3')
plates.inputplates('plate4')
plates.inputplates('plate5') 
plates.inputplates('plate6')
plates.inputplates('plate7')
print (plates.steckcount())
print (plates.platecount())
print(plates)

print (plates.removeplate())
print (plates.removeplate())
print (plates)
print (plates.steckcount())
print (plates.platecount())
