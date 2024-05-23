class Polygon:
  def __init__(self, coords):
      self.coordinates = coords

  def move(self, x, y):
      for i in self.coordinates:
          i[0] += x
          i[1] += y

  def area(self):
      raise NotImplementedError("Subclasses should implement this method")

  @staticmethod
  def compare(t1, t2):
      return t1.area() == t2.area()

  @staticmethod
  def is_intersect(t1, t2):
      def do_intersect(p1, q1, p2, q2):
          def on_segment(p, q, r):
              if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                      q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
                  return True
              return False

          def orientation(p, q, r):
              val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
              if val == 0:
                  return 0
              elif val > 0:
                  return 1
              else:
                  return 2

          o1 = orientation(p1, q1, p2)
          o2 = orientation(p1, q1, q2)
          o3 = orientation(p2, q2, p1)
          o4 = orientation(p2, q2, q1)

          if o1 != o2 and o3 != o4:
              return True

          if o1 == 0 and on_segment(p1, p2, q1):
              return True
          if o2 == 0 and on_segment(p1, q2, q1):
              return True
          if o3 == 0 and on_segment(p2, p1, q2):
              return True
          if o4 == 0 and on_segment(p2, q1, q2):
              return True

          return False

      def check_intersect(coords1, coords2):
          n1 = len(coords1)
          n2 = len(coords2)
          for i in range(n1):
              for j in range(n2):
                  if do_intersect(coords1[i], coords1[(i + 1) % n1], coords2[j], coords2[(j + 1) % n2]):
                      return True
          return False

      return check_intersect(t1.coordinates, t2.coordinates)

  @staticmethod
  def is_include(t1, t2):
      def is_point_inside_polygon(polygon, point):
          x, y = point
          n = len(polygon)
          inside = False

          p1x, p1y = polygon[0]
          for i in range(n + 1):
              p2x, p2y = polygon[i % n]
              if y > min(p1y, p2y):
                  if y <= max(p1y, p2y):
                      if x <= max(p1x, p2x):
                          if p1y != p2y:
                              xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                          if p1x == p2x or x <= xinters:
                              inside = not inside
              p1x, p1y = p2x, p2y

          return inside

      for point in t2.coordinates:
          if not is_point_inside_polygon(t1.coordinates, point):
              return False
      return True

class Triangle(Polygon):
    def __init__(self, coords=None):
        default_coords = [[1, 0], [-1, 0], [1, 1]]
        if coords and isinstance(coords, list) and len(coords) == 3 and all(isinstance(coord, list) for coord in coords):
            super().__init__(coords)
        else:
            print("Failed to save coordinates. Standard coordinates will be used")
            super().__init__(default_coords)
    
    def area(self):
        x1, y1 = self.coordinates[0]
        x2, y2 = self.coordinates[1]
        x3, y3 = self.coordinates[2]
        return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

class Tetragon(Polygon):
    def __init__(self, coords=None):
        default_coords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        if coords and isinstance(coords, list) and len(coords) == 4 and all(isinstance(coord, list) for coord in coords):
            super().__init__(coords)
        else:
            print("Failed to save coordinates. Standard coordinates will be used")
            super().__init__(default_coords)
    
    def area(self):
        def triangle_area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

        return triangle_area(self.coordinates[0], self.coordinates[1], self.coordinates[2]) + \
               triangle_area(self.coordinates[0], self.coordinates[2], self.coordinates[3])

# class Tetragon:
#     coordinates = [[0, 0], [1, 0], [1, 1], [0, 1]]

#     def __init__(self, coords=None):
#         if coords and isinstance(coords, list) and len(coords) == 4 and all(isinstance(coord, list) for coord in coords):
#             self.coordinates = coords
#         else:
#             print("Failed to save coordinates. Standard coordinates will be used")
    
#     def area(self):  # Площадь четырехугольника
#         def triangle_area(p1, p2, p3):
#             x1, y1 = p1
#             x2, y2 = p2
#             x3, y3 = p3
#             return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

#         # Разбиваем четырехугольник на два треугольника и суммируем их площади
#         return triangle_area(self.coordinates[0], self.coordinates[1], self.coordinates[2]) + \
#                triangle_area(self.coordinates[0], self.coordinates[2], self.coordinates[3])

#     def move(self, x, y):
#         for i in self.coordinates:
#             i[0] += x
#             i[1] += y

# class Triangle(Polygon):
#   coordinates = [[1,0], [-1,0], [1,1]]

#   def __init__(self, coords = None):
#     if coords != None and type(coords) == list and len(coords) == 3 and type(coords[0]) == list:
#       coordinates = coords
#     else:
#       print("Failed to save coordinates. Standart coordinates will be used")
    
#   def area(self): # Площадь треугольника
#     x1 = self.coordinates[0][0]
#     y1 = self.coordinates[0][1]

#     x2 = self.coordinates[1][0]
#     y2 = self.coordinates[1][1]

#     x3 = self.coordinates[2][0]
#     y3 = self.coordinates[2][1]
    
#     return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))    
  
#   def move(self, x, y):
#     for i in self.coordinates:
#       i[0] += x
#       i[1] += y



# Примеры использования
triangle = Triangle([[0, 0], [4, 0], [2, 3]])
tetragon = Tetragon([[0, 0], [4, 0], [4, 3], [0, 3]])

print("Area of triangle:", triangle.area())
print("Area of tetragon:", tetragon.area())

triangle.move(1, 1)
print("Moved triangle coordinates:", triangle.coordinates)

tetragon.move(2, 2)
print("Moved tetragon coordinates:", tetragon.coordinates)

print("Areas are equal:", Polygon.compare(triangle, tetragon))
print("Objects intersect:", Polygon.is_intersect(triangle, tetragon))
print("Triangle includes tetragon:", Polygon.is_include(triangle, tetragon))
print("Tetragon includes triangle:", Polygon.is_include(tetragon, triangle))
