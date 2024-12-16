from tkinter import *

root = Tk()
root.title("Calculator")

display = Entry(root, width=40, borderwidth=10, bg="WHITE", justify=RIGHT)

button_1 = Button(root, text="1", padx=30, pady=12, bg="WHITE", command=lambda: button_click("1"))
button_2 = Button(root, text="2", padx=30, pady=12, bg="WHITE", command=lambda: button_click("2"))
button_3 = Button(root, text="3", padx=30, pady=12, bg="WHITE", command=lambda: button_click("3"))
button_4 = Button(root, text="4", padx=30, pady=12, bg="WHITE", command=lambda: button_click("4"))
button_5 = Button(root, text="5", padx=30, pady=12, bg="WHITE", command=lambda: button_click("5"))
button_6 = Button(root, text="6", padx=30, pady=12, bg="WHITE", command=lambda: button_click("6"))
button_7 = Button(root, text="7", padx=30, pady=12, bg="WHITE", command=lambda: button_click("7"))
button_8 = Button(root, text="8", padx=30, pady=12, bg="WHITE", command=lambda: button_click("8"))
button_9 = Button(root, text="9", padx=30, pady=12, bg="WHITE", command=lambda: button_click("9"))
button_0 = Button(root, text="0", padx=30, pady=12, bg="WHITE", command=lambda: button_click("0"))
button_dot = Button(root, text=" .", padx=30, pady=12, bg="WHITE", command=lambda: button_click("."))
button_sign = Button(root, text="+/-", padx=24, pady=12, bg="WHITE", command=lambda: button_negate())

button_add = Button(root, text=" +", padx=28, pady=12, bg="WHITE", command=lambda: button_click(" + "))
button_subtract = Button(root, text="-", padx=31, pady=12, bg="WHITE", command=lambda: button_click(" - "))
button_multiply = Button(root, text="*", padx=31, pady=12, bg="WHITE", command=lambda: button_click(" * "))
button_divide = Button(root, text="/", padx=31, pady=12, bg="WHITE", command=lambda: button_click(" / "))
button_equal = Button(root, text=" =", padx=28, pady=12, bg="WHITE", command=lambda: button_evaluate())

button_ce = Button(root, text="CE", padx=26, pady=12, bg="WHITE", command=lambda: button_clear_entry())
button_c = Button(root, text="C", padx=29, pady=12, bg="WHITE", command=lambda: button_clear())
button_del = Button(root, text="<--", padx=24, pady=12, bg="WHITE", command=lambda: button_delete())


def button_click(new):
    prev = display.get()
    display.delete(0, END)
    display.insert(0, prev + new)


def button_negate():
    prev = display.get()
    new = ""
    prev = " " + prev
    for i in range(len(prev) - 1, -1, -1):
        if not prev[i:i + 1].isdigit():
            new = prev[1:i + 1] + "-" + prev[i + 1:]
            break
    display.delete(0, END)
    display.insert(0, new)


def button_evaluate():
    prev = display.get()
    try:
        result = eval(prev)
        new = str(result)
    except (SyntaxError, NameError, ValueError, TypeError, ArithmeticError):
        new = "Error"
    display.delete(0, END)
    display.insert(0, new)


def button_clear_entry():
    prev = display.get()
    new = ""
    prev = " " + prev
    for i in range(len(prev) - 1, -1, -1):
        if not prev[i:i + 1].isdigit():
            new = prev[1:i + 1]
            break
    display.delete(0, END)
    display.insert(0, new)


def button_clear():
    display.delete(0, END)


def button_delete():
    prev = display.get()
    new = prev[:-1]
    display.delete(0, END)
    display.insert(0, new)


display.grid(row=0, column=0, columnspan=4, pady=15)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=1)
button_dot.grid(row=5, column=2)
button_sign.grid(row=5, column=0)

button_add.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)
button_equal.grid(row=5, column=3)

button_ce.grid(row=1, column=0)
button_c.grid(row=1, column=1)
button_del.grid(row=1, column=2)

root.mainloop()
