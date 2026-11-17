class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
class Rectangle:
    def __init__(self, p, q):
        assert isinstance(p, Point) and isinstance(q, Point), "Bad input!"
        assert p.x <= q.x and p.y <= q.y, "Bad input!"
        self.p = p
        self.q = q
    def __str__(self):
        return f"(p=({self.p.x},{self.p.y}), q=({self.q.x},{self.q.y}))."
    def get_width(self):
        return self.q.x - self.p.x
    def get_height(self):
        return self.q.y - self.q.y
    def perimeter(self):
        return 2*(self.p.x+self.q.x)
    def area(self):
        return self.get_height * self.get_width
    def contains(self, pt):
        self.pt= pt
        if self.p.x <= self.pt.x <= self.q.x and self.p.y <= self.pt.y <= self.q.y:
            return True
        else:
            return False
p1= Point(1,2)
p2= Point(3.2,4)
R= Rectangle(p1,p2)
print(R)
print(R.get_width())
print(R.get_height())
print(R.area)
print(R.perimeter())
print(R.contains(Point(1.5, 3)))
print ( R.contains ( Point (10.5 , 3) ) )
print ( R.contains ( Point (1 , 2) ) )
print ( R.contains ( Point (3.2 , 4) ) )