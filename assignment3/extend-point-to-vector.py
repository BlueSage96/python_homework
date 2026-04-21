import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
         return self.x == other.x and self.y == other.y
      
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def distance(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx * dx + dy * dy)
    
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        
        return Vector(new_x, new_y)

p1 = Point(0,6)
p2 = Point(5,7)

v1 = Vector(1,3)
v2 = Vector(9,2)

print(f"Point: {p1}")

print(f"Vector: {v1}")

print(f"Equality: {p1.__eq__(p2)}")

print(f"Distance: {p1.distance(p2)}")

print(f"Adding vectors: {v1.__add__(v2)}")