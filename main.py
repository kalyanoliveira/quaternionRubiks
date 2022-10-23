from model import *

moves = [str(x) for x in input().split(" ")]

r = Rubiks()

for i in moves:
  r.rotate(i)

r.current()

print("\n\n\n")

moves2 = [str(x) for x in input().split(" ")]

for i in moves2:
  r.rotate(i)

r.current()
