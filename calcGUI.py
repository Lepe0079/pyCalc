from tkinter import *

root = Tk()
root.title("PyCalc 0.1")

ent = Entry(root, width=10, borderwidth=20, font=('Verdana', 20))
ent.pack(side=TOP)

def bPress(val):
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0,str(current) + str(val))

def bClear():
    ent.delete(0,END)

def bOperation(code):
    global firstNum
    firstNum = int(ent.get())
    global opCode 
    opCode = code
    bClear()
    return

def bEqual():
    secondNum = int(ent.get())
    bClear()
    if opCode == "+":
        ent.insert(0, firstNum+secondNum)
        return
    if opCode == "-":
        ent.insert(0, str(firstNum-secondNum))
        return
    if opCode == "*":
        ent.insert(0, str(firstNum*secondNum))
        return
    if opCode == "/":
        if (secondNum == 0 or firstNum == 0):
            ent.insert(0, "Division by Zero")
            return
        else:
            ent.insert(0, str(firstNum/secondNum))
            return
    return

#buttons go here, packed into frames. numbers on the left, operations on the right
bFrame = Frame(root)
bFrame.pack(side=BOTTOM)
Button(bFrame, text=(1), command=lambda: bPress(1), pady=20, padx=20).grid(row=0, column=0)
Button(bFrame, text=(2), command=lambda: bPress(2), pady=20, padx=20).grid(row=0, column=1)
Button(bFrame, text=(3), command=lambda: bPress(3), pady=20, padx=20).grid(row=0, column=2)
Button(bFrame, text=(4), command=lambda: bPress(4), pady=20, padx=20).grid(row=1, column=0)
Button(bFrame, text=(5), command=lambda: bPress(5), pady=20, padx=20).grid(row=1, column=1)
Button(bFrame, text=(6), command=lambda: bPress(6), pady=20, padx=20).grid(row=1, column=2)
Button(bFrame, text=(7), command=lambda: bPress(7), pady=20, padx=20).grid(row=2, column=0)
Button(bFrame, text=(8), command=lambda: bPress(8), pady=20, padx=20).grid(row=2, column=1)
Button(bFrame, text=(9), command=lambda: bPress(9), pady=20, padx=20).grid(row=2, column=2)
Button(bFrame, text=(0), command=lambda: bPress(0), pady=20, padx=20).grid(row=3, column=0)

Button(bFrame, text=("+"), command=lambda: bOperation("+"), pady=20, padx=20).grid(row=0, column=4)
Button(bFrame, text=("-"), command=lambda: bOperation("-"), pady=20, padx=20).grid(row=1, column=4)
Button(bFrame, text=("*"), command=lambda: bOperation("*"), pady=20, padx=20).grid(row=2, column=4)
Button(bFrame, text=("/"), command=lambda: bOperation("/"), pady=20, padx=20).grid(row=3, column=4)
Button(bFrame, text=("="), command=lambda: bEqual(), pady=20, padx=20).grid(row=3, column=2)
Button(bFrame, text=("C"), command=lambda: bClear(), pady=20, padx=20).grid(row=3, column=1)


root.mainloop()