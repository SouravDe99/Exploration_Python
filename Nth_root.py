import math


def power(x, k):
    if k == 0:
        return 1
    else:
        if k % 2 == 0:
            t = power(x, k // 2)
            return t*t
        if k % 2 == 1:
            t = power(x, (k - 1) // 2)
            return x * t * t


g = 1
a = int(input("Enter a number :- "))
n = int(input("Enter value of n :- "))
if n < 0:
    a = 1 / a
    n = n * (-1)
print(n, "th root of", a, "=", math.pow(a, 1 / n), "(Python)")
for i in range(100000):
    g = ((n - 1) * g + a / power(g, n - 1)) / n
print(n, "th root of", a, "=", g, "(Me)")
