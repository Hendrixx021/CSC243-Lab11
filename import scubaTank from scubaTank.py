from scubaTank import scubaTank

def transfer_air(source, target, amount):
  if amount< source.get_bar() and amount > 0:
    source.release(amount)
    target.fill(amount)

  elif amount<=0:
    print("Invalid amount")
  elif amount > source.get_bar():
    print("Not enough air")

src = scubaTank("A", 150)
dst = scubaTank("B", 20)
transfer_air(src, dst, 50)
print(src)
print(dst)

transfer_air (src, dst, 120)
print(src.get_bar())
print (dst.get_bar())