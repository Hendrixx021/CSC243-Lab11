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
      return self.__bar - amount
  def __str__(self):
    return f"Tank {self.label}: {self.__bar} bar"

t = scubaTank("A",80)
print(t)
t.fill(40)
print(t.get_bar())
t.set_bar(250)
print(t)
t.set_bar(400)
print(t.get_bar())
t.release (0)
t.release (300)
t.release (50)
print ( t )