print("Hello World")


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("Move disk from", a, "to", c)
        hanoi(n - 1, b, a, c)


print("This program prints instructions to solve Tower of Hanoi")
x = int(input("Enter number of disks:- "))
hanoi(x, "A", "B", "C")
# print("Finished")
