class Triangle:
  coordinates = [[1,0], [-1,0], [1,1]]

  def __init__(self, coords = None):
    if coords != None and type(coords) == list and len(coords) == 3 and type(coords[0]) == list:
      coordinates = coords
    else:
      print("Failed to save coordinates. Standart coordinates will be used")
    
  def area(self): # Площадь треугольника
    x1 = self.coordinates[0][0]
    y1 = self.coordinates[0][1]

    x2 = self.coordinates[1][0]
    y2 = self.coordinates[1][1]

    x3 = self.coordinates[2][0]
    y3 = self.coordinates[2][1]
    
    return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))    
  
  def move(self, x, y):
    for i in self.coordinates:
      i[0] += x
      i[1] += y


tr = Triangle()
print(tr.area())
tr.move(2, 3)
print(tr.area())
for i in tr.coordinates:
  print(i)