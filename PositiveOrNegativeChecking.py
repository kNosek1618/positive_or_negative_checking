
from random import randint

x = randint(-100, 100)
print("x = " + str(x))
while x == 0:
    x = randint(-100, 100)

y = randint(-100, 100)
print("y = " + str(y))
while y == 0:
    y = randint(-100, 100)

if x > 0 and y > 0:
    print("both positive")
if x < 0 and y < 0:
    print("both negative")
if x > 0 and y < 0:
    print("x is positive and y is negative")
if x < 0 and y > 0:
    print("y is positive and x is negative")