def a(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return a(m - 1, 1)
    else:
        return a(m - 1, a(m, n - 1))


x = int(input("Enter the value of m :- "))
y = int(input("Enter the value of n :- "))
z = a(x, y)
print("A(", x, ",", y, ")=", z)

"""for i in range(4):
    for j in range(10):
        z = a(i, j)
        print("A(", i, ",", j, ")=", z)"""
