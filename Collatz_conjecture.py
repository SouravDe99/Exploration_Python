n = int(input("Enter a number :- "))
c = 0
print(n)
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    c = c + 1
    print(n)
print("Number of steps =", c)
