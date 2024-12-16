def prime(p):
    c = 0
    for k in range(1, p+1):
        if p % k == 0:
            c = c + 1
    if c == 2:
        return True
    else:
        return False


n = int(input("Enter an odd number greater than 5 :- "))
if n % 2 == 1 and n > 5:
    r = 0
    for i in range(1, n//2 + 1):
        for j in range(i, (n - i) // 2 + 1):
            if prime(i) and prime(j) and prime(n - i - j):
                print(n, "=", i, "+", j, "+", n - i - j)
                r = r + 1
    print("Number of prime representations of", n, "is", r)
else:
    print("Wrong input")
