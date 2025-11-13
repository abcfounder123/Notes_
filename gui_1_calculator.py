
"""
kinter (Tk + interface)

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

3. Button()   =>   pack()   --->   middle, t to b

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

geometry management

789/
456*
123-
0.+%

clr Ans

################################################

from tkinter import *


x = Tk()

s = StringVar(x)
e = Entry(textvariable=s)

f1 = Frame(x)
f2 = Frame(x)
f3 = Frame(x)
f4 = Frame(x)
f5 = Frame(x)

e.pack()
f1.pack()
f2.pack()
f3.pack()
f4.pack()
f5.pack()

Button(f1, text='7', command=lambda :s.set(s.get() + '7')).pack(side=LEFT)
Button(f1, text='8', command=lambda :s.set(s.get() + '8')).pack(side=LEFT)
Button(f1, text='9', command=lambda :s.set(s.get() + '9')).pack(side=LEFT)
Button(f1, text='/', command=lambda :s.set(s.get() + '/')).pack(side=LEFT)

Button(f2, text='4', command=lambda :s.set(s.get() + '4')).pack(side=LEFT)
Button(f2, text='5', command=lambda :s.set(s.get() + '5')).pack(side=LEFT)
Button(f2, text='6', command=lambda :s.set(s.get() + '6')).pack(side=LEFT)
Button(f2, text='*', command=lambda :s.set(s.get() + '*')).pack(side=LEFT)


Button(f3, text='1', command=lambda :s.set(s.get() + '1')).pack(side=LEFT)
Button(f3, text='2', command=lambda :s.set(s.get() + '2')).pack(side=LEFT)
Button(f3, text='3', command=lambda :s.set(s.get() + '3')).pack(side=LEFT)
Button(f3, text='-', command=lambda :s.set(s.get() + '-')).pack(side=LEFT)

Button(f4, text='0', command=lambda :s.set(s.get() + '0')).pack(side=LEFT)
Button(f4, text='.', command=lambda :s.set(s.get() + '.')).pack(side=LEFT)
Button(f4, text='+', command=lambda :s.set(s.get() + '+')).pack(side=LEFT)
Button(f4, text='%', command=lambda :s.set(s.get() + '%')).pack(side=LEFT)

Button(f5, text='clr', command=lambda :s.set("")).pack(side=LEFT)
Button(f5, text='Ans', command=lambda :s.set(str(eval(s.get())))).pack(side=LEFT)
Button(f5, text='del', command=lambda :s.set(s.get()[:-1])).pack(side=LEFT)

x.mainloop()

################################################

from tkinter import *


x = Tk()

s = StringVar(x)
e = Entry(textvariable=s)
e.pack()

keymap = ['789/', '456*', '123-', '0.+%']

for keys in keymap:
    f = Frame(x)
    f.pack()
    for key in keys:
        Button(f, text=key, command=lambda i=key: s.set(s.get() + i + " ")).pack(side=LEFT)

f5 = Frame()
f5.pack()

Button(f5, text='clr', command=lambda :s.set("")).pack(side=LEFT)
Button(f5, text='Ans', command=lambda :s.set(str(eval(s.get())) + " ")).pack(side=LEFT)
Button(f5, text='del', command=lambda :s.set(s.get()[:-1])).pack(side=LEFT)

x.mainloop()

################################################################################################

"""
