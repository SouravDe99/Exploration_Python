def prime(p):
    c = 0
    for k in range(1, p+1):
        if p % k == 0:
            c = c + 1
    if c == 2:
        return True
    else:
        return False


n = int(input("Enter an even number greater than 2 :- "))
if n % 2 == 0 and n > 2:
    r = 0
    for i in range(1, n//2 + 1):
        if prime(i) and prime(n - i):
            print(n, "=", i, "+", n - i)
            r = r + 1
    print("Number of prime representations of", n, "is", r)
else:
    print("Wrong input")
