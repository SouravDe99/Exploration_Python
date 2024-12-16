import math
g = 1
a = int(input("Enter a number :- "))
print("square root of", a, "=", math.sqrt(a), "(Python)")
for i in range(100):
    g = (g + a / g) / 2
print("square root of", a, "=", g, "(Me)")
