import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def display(self):
        print(f"Điểm tâm: ({self.x}, {self.y})")
class Elip(Point):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b
    def area(self):
        return math.pi * self.a * self.b
    def display(self):
        super().display()
        print(f"Elip với a = {self.a}, b = {self.b}")
        print(f"Diện tích elip = {self.area():.2f}")
class Circle(Elip):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r)
        self.r = r
    def circumference(self):
        return 2 * math.pi * self.r
    def area(self):
        return math.pi * self.r * self.r
    def display(self):
        print("Hình tròn:")
        super(Point, self).display()
        print(f"Bán kính r = {self.r}")
        print(f"Chu vi = {self.circumference():.2f}")
        print(f"Diện tích = {self.area():.2f}")
print("=== Elip ===")
e = Elip(0, 0, 5, 3)
e.display()
print("\n=== Đường tròn ===")
c = Circle(1, 2, 4)
c.display()
