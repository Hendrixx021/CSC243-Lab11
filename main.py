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
        w= self.q.x - self.p.x
        return w
    def get_height(self):
        h=self.q.y - self.p.y
        return h
    def perimeter(self):
        return 2* (self.get_width() + self.get_height())
    def area(self):
        return self.get_width() * self.get_height()
    def contains(self, pt):
        self.pt= pt
        if self.p.x <= self.pt.x <= self.q.x and self.p.y <= self.pt.y <= self.q.y:
            return True
        else:
            return False

class scubaTank:
  def __init__(self, label, bar):
    self.__bar = bar
    self.label= label
  def get_bar(self):
    return self.__bar
  def set_bar(self, bar):
    if 0 > bar < 300:
      print("Invalid pressure")
    else:
      self.__bar = bar
  def fill(self, amount):
      if amount <= 0:
        print("Invalid amount")
      else:
        self.__bar += amount
  def release(self, amount):
    if amount <= 0:
      print("Invalid amount")
    elif amount > self.__bar:
      print("Not enough air")
    else:
      self.__bar-= amount
      return self.__bar
  def __str__(self):
    return f"Tank {self.label}: {self.__bar} bar"

def transfer_air(source, target, amount):
  if amount< source.get_bar() and amount > 0:
    source.release(amount)
    target.fill(amount)

  elif amount<=0:
    print("Invalid amount")
  elif amount > source.get_bar():
    print("Not enough air")
