
"""

Tkinter (Tk + interface)

Tk = ToolKit for Tcl (Tool Command Language)

ToolKit
- multi-platform widgets (wi + dget = window gadget)

################################################

widgets (19)
- button widget
- label widget
- entry widget
-

################################################

CLI (command line interface)

GUI (graphical user interface)

################################################

GUI programming

1. What?    =>   show        =>   widgets 19
2. Where?   =>   position    =>   geometry management (pack, grid, place)
3. What?    =>   procedure   =>   Python function

################################################

1. Root       =>   Tk(), mainloop()

2. Frame()

3. Button()   =>   pack()   --->   middle

4. Entry()

5. StringVar() -> set(), get()

################################################

s.set("1")  # s = '1'
s.get()     # "1"

################################################

Button click

"1"
"+"
"2"

s.set("1") # s = '1'
s.set("+") # s = '+'
s.set("2") # s = '2'

"" + "1" + "+" + "2" --->  "1+2"

s.set(s.get() + '1') # s = '1'
s.set(s.get() + '+') # s = '1' + '+' = '1+'
s.set(s.get() + '2') # s = '1+' + '2' = '1+2'

################################################

Ans

s = "1+2"    =>   "3"

s.set(str(eval(s.get())))

################################################

del

s = "110%"
s[:-1]   =>   "110"

s.set(s.get()[:-1])

################################################

clr

s = ""
s.set("")

################################################

from tkinter import *


def f():
    s.set(s.get() + "1")

    
def f2():
    s.set(s.get() + "+")


def f3():
    s.set(s.get() + "2")


def f4():
    s.set(str(eval(s.get())))


def f5():
    s.set(s.get()[:-1])


def f6():
    s.set("")
    

x = Tk()
s = StringVar(x)
e = Entry(x, textvariable=s)

f1 = Frame(x)
f2 = Frame(x)

Button(f1, text="1", command=f).pack(side=LEFT)
Button(f1, text="+", command=f2).pack(side=LEFT)
Button(f1, text="2", command=f3).pack(side=LEFT)

Button(f2, text="Ans", command=f4).pack(side=LEFT)
Button(f2, text="del", command=f5).pack(side=LEFT)
Button(f2, text="clr", command=f6).pack(side=LEFT)

e.pack()
f1.pack()
f2.pack()

x.mainloop()

################################################################################################

"""

