
"""

Step.1  -->  Create root


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

x.mainloop()

#########################################

Step.2  --> button, grid


          C0     C1     C2                C9

row 0     B1     B2     B3
row 1     B4     B5     B6
row 2     B7     B8     B9

B1 = row 0, C0
B2 = row 0, C1
B5 = row 1, C1
B9 = row 2, C2



from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

Button(x, width=8, height=4, text="B1", font=('Arial', 30, 'bold')).grid(row=0, column=0)

x.mainloop()

#########################################

Step.3  -->   label


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=8, height=4, text="B1", font=('Arial', 30, 'bold'))
b1.grid(row=0, column=0)

x.mainloop()

#########################################

Step.4  -->  button 3, 9


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=8, height=4, text="B1", font=('Arial', 30, 'bold'))
b2 = Button(x, width=8, height=4, text="B2", font=('Arial', 30, 'bold'))
b3 = Button(x, width=8, height=4, text="B3", font=('Arial', 30, 'bold'))

b4 = Button(x, width=8, height=4, text="B4", font=('Arial', 30, 'bold'))
b5 = Button(x, width=8, height=4, text="B5", font=('Arial', 30, 'bold'))
b6 = Button(x, width=8, height=4, text="B6", font=('Arial', 30, 'bold'))

b7 = Button(x, width=8, height=4, text="B7", font=('Arial', 30, 'bold'))
b8 = Button(x, width=8, height=4, text="B8", font=('Arial', 30, 'bold'))
b9 = Button(x, width=8, height=4, text="B9", font=('Arial', 30, 'bold'))


b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

x.mainloop()

#########################################

Step.5  -->  nested loop

for row in range(3): # 0
    for col in range(3): # 0 1 2
        print(row, col) # 0 0, 0 1, 0 2

0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2

#########################################

Step.6    -->   B1, B2, B3, ..., B9

from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

n = 1
for row in range(3):
    for col in range(3):
        Button(x, width=8, height=4, text=f"B{n}", font=('Arial', 30, 'bold')).grid(row=row, column=col)
        n += 1

x.mainloop()

#########################################

Step.7    -->  empty_text = ''


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

for row in range(3):
    for col in range(3):
        Button(x, width=8, height=4, text='', font=('Arial', 30, 'bold')).grid(row=row, column=col)

x.mainloop()

##################################################################################

Step.8  -->  if click b1, show X

=> command=f


def f():
    b1["text"] = 'X'

##################################################################################

Step.9  -->  Switch player   ( X and O )


s = "X"


def f2():
    global s
    if s == "X":
        s = "O"
    else:
        s = "X"


##################################################################################

Step.8 + Step.9


from tkinter import *


s = "X"


def f2():
    global s
    if s == "X":
        s = "O"
    else:
        s = "X"


def f():
    b1["text"] = s
    f2()                # X => O => X


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f)
b1.grid(row=0, column=0)

x.mainloop()

##################################################################################

Step.10  -->  Control to draw once

If text value is somthing, do nothing.
Else, Draw s and Switch player.

def f():
    if b1['text']:
        pass
    else:
        b1["text"] = s
        switch_player()

#########################################

If text value is not somthing, Draw s and Switch player.

def f():
    if not b1['text']:
        b1["text"] = s
        switch_player()

#########################################

If text value is somthing, do nothing and stop function.
If not stop, continue following program.

def f():
    if b1['text']:
        return
    b1["text"] = s
    switch_player()

#########################################


from tkinter import *


s = "X"


def switch_player():
    global s
    if s == "X":
        s = "O"
    else:
        s = "X"


def f():
    if b1['text']:
        pass
    else:
        b1["text"] = s
        switch_player()


def f2():
    if not b2['text']:
        b2["text"] = s
        switch_player()


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f)
b1.grid(row=0, column=0)

b2 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f2)
b2.grid(row=0, column=1)

x.mainloop()

##################################################################################

Step.11  -->  Functions for each data and Function for every data

Functions for each data

d1 = {'text': ''}
d2 = {'text': ''}
d3 = {'text': ''}


def f1():
    d1["text"] = 'apple'

def f2():
    d2["text"] = 'banana'

def f3():
    d3["text"] = 'orange'


f3()

print(d1)
print(d2)
print(d3)

#########################################

Function for every data

d1 = {'text': ''}
d2 = {'text': ''}
d3 = {'text': ''}


def f(x):
    x['text'] = 'apple'


f(d3)

print(d1)
print(d2)
print(d3)

#########################################

Functions for each button

def f1():
    b1["text"] = 'X'

def f2():
    b2["text"] = 'X'

def f3():
    b3["text"] = 'X'


Function for every buttons
def f(e):
    e.widget["text"] = 'X'

#########################################


def f(e):
    print(e.widget)  # .!button,  .!button2  .!button3


#########################################


def f1():
    if not b1['text']:
        b1["text"] = s
        switch_player()


def f2():
    if not b2['text']:
        b2["text"] = s
        switch_player()


def f(e):
    b = e.widget
    if not b['text']:
        b["text"] = s
        switch_player()

#########################################

Functions for each button


from tkinter import *


s = "X"


def switch_player():
    global s
    if s == "X":
        s = "O"
    else:
        s = "X"


def f1():
    if not b1['text']:
        b1["text"] = s
        switch_player()


def f2():
    if not b2['text']:
        b2["text"] = s
        switch_player()


def f3():
    if not b3['text']:
        b3["text"] = s
        switch_player()


def f4():
    if not b4['text']:
        b4["text"] = s
        switch_player()


def f5():
    if not b5['text']:
        b5["text"] = s
        switch_player()


def f6():
    if not b6['text']:
        b6["text"] = s
        switch_player()


def f7():
    if not b7['text']:
        b7["text"] = s
        switch_player()


def f8():
    if not b8['text']:
        b8["text"] = s
        switch_player()


def f9():
    if not b9['text']:
        b9["text"] = s
        switch_player()

x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f1)
b1.grid(row=0, column=0)
b2 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f2)
b2.grid(row=0, column=1)
b3 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f3)
b3.grid(row=0, column=2)

b4 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f4)
b4.grid(row=1, column=0)
b5 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f5)
b5.grid(row=1, column=1)
b6 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f6)
b6.grid(row=1, column=2)

b7 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f7)
b7.grid(row=2, column=0)
b8 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f8)
b8.grid(row=2, column=1)
b9 = Button(x, width=8, height=4, text="", font=('Arial', 30, 'bold'), command=f9)
b9.grid(row=2, column=2)

x.mainloop()

#########################################

Function for every buttons


from tkinter import *


s = "X"


def switch_player():
    global s
    if s == "X":
        s = "O"
    else:
        s = "X"


def f(e):
    b = e.widget
    if not b['text']:
        b["text"] = s
        switch_player()


x = Tk()
x.title("Tac Ti Toe")

for row in range(3):
    for col in range(3):
        b = Button(x, width=8, height=4, text='', font=('Arial', 30, 'bold'))
        b.grid(row=row, column=col)
        b.bind("<Button-1>", f)

x.mainloop()

##################################################################################

Step.12  -->  1D, 2D, 3D

Step.12.1  --> Creating 1D data

board = []
n1 = 1
n2 = 2
n3 = 3

board.append(n1)
board.append(n2)
board.append(n3)

print(board)

#########################################

Step.12.2  --> Creating 1D data with loop

board = []

for n in range(1, 10): # 1 2 
    board.append(n)

print(board)

#########################################

Step.12.3  --> Creating 2D data

d1 = {'text': ''}
d2 = {'text': ''}
d3 = {'text': ''}

board = [d1, d2, d3]   # [{'text': ''}, {'text': ''}, {'text': ''}]

#########################################

Step.12.4  --> Assign value to 2D data

board[0]['text'] = "apple"
print(board)

board[2]['text'] = "X"
print(board)

board[1]['text'] = "O"
print(board)

#########################################

Step.12.5  --> Creating 3D data   (row + column + text)

[   
    [{'text': ''}, {'text': ''}, {'text': ''}], 
    [{'text': ''}, {'text': ''}, {'text': ''}], 
    [{'text': ''}, {'text': ''}, {'text': ''}]
    
]

[   
    [d1, d2, d3], 
    [d4, d5, d6], 
    [d7, d8, d9]
    
]


board[0] => [{'text': ''}, {'text': ''}, {'text': ''}]      <-- r0
board[0][0] =>  {'text': ''}                                <-- d1
board[0][1]                                                 <-- d2
board[0][2]                                                 <-- d3

board[1]                                                    <-- r1
board[1][0]                                                 <-- d4
board[1][1]                                                 <-- d5
board[1][2]                                                 <-- d5

board[2]                                                    <-- r2
board[2][0]                                                 <-- d7
board[2][1]                                                 <-- d8
board[2][2]                                                 <-- d9

#########################################

Step.12.6  -->  2D (row, col)

          C0     C1     C2                C9

row 0     B1     B2     B3
row 1     B4     B5     B6
row 2     B7     B8     B9

B1 = row 0, C0
B2 = row 0, C1
B5 = row 1, C1
B9 = row 2, C2

[   
    [d1, d2, d3], 
    [d4, d5, d6], 
    [d7, d8, d9]
    
]

#########################################

Step.12.7  -->  3D (row, col, text)

[   
    [{'text': 'X'}, {'text': 'apple'}, {'text': ''}], 
    [{'text': ''}, {'text': ''}, {'text': ''}], 
    [{'text': ''}, {'text': ''}, {'text': 'X'}]
    
]

#########################################

Step.12.8  --> Assign value to 3D data

d1 = {'text': ''}  # 1D
d2 = {'text': ''}
d3 = {'text': ''}

d4 = {'text': ''}
d5 = {'text': ''}
d6 = {'text': ''}

d7 = {'text': ''}
d8 = {'text': ''}
d9 = {'text': ''}

r0 = [d1, d2, d3]  # 2D
r1 = [d4, d5, d6]
r2 = [d7, d8, d9]

board = [r0, r1, r2]  # 3D

board[0][0]['text'] = 'X'
board[2][2]['text'] = 'X'

print(board[0][1]['text'])

#########################################

Step.12.9  --> Access value from 3D data


board = [
    [{'text': ''}, {'text': 'apple'}, {'text': ''}],
    [{'text': ''}, {'text': 'banana'}, {'text': ''}],
    [{'text': ''}, {'text': ''}, {'text': ''}]

]

print(board[0][1]['text'])
print(board[1][1]['text'])

#########################################

Step.13  --> Creating 2D data (empty board)

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],

]

#########################################

Step.14  --> Creating 3D data (2D + 1D data)

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]

b1 = {'text': ''}
b9 = {'text': ''}

board[0][0] = b1     # 2D + 1D
board[2][2] = b9

print(board)

#########################################

board = [
          [{'text': ''}, None, None], 
          [None, None, None], 
          [None, None, {'text': ''}]
]

#########################################

Step.15.1  -->  Assign buttons to empty board

board[0][0] = b1
board[0][1] = b2
board[0][2] = b3

board[1][0] = b4
board[1][1] = b5
board[1][2] = b6

board[2][0] = b7
board[2][1] = b8
board[2][2] = b9

#########################################

Step.15.2  -->  Access text data from button

board = [
    
    [<tkinter.Button object .!button> , <tkinter.Button object .!button2>, <tkinter.Button object .!button3>],
    [<tkinter.Button object .!button4>, <tkinter.Button object .!button5>, <tkinter.Button object .!button6>], 
    [<tkinter.Button object .!button7>, <tkinter.Button object .!button8>, <tkinter.Button object .!button9>]
    
]


print(board)
print(board[0][0])  # b1
print(board[0][0]['text']) # "" <--- empty text

##################################################################################

Step.16  -->  Checking winner (X player) (3 rows)

          C0     C1     C2                C9

row 0     B1     B2     B3
row 1     B4     B5     B6
row 2     B7     B8     B9

row o   =>  B1, B2, B3
row 1   =>  B4, B5, B7
row 2   =>  B7, B8, B9

row o   =>  B1, B2, B3
board[0][0]['text'] == 'X' and board[0][1]['text'] == 'X' and board[0][2]['text'] == 'X'

row 1   =>  B4, B5, B7
board[1][0]['text'] == 'X' and board[1][1]['text'] == 'X' and board[1][2]['text'] == 'X'

row 2   =>  B7, B8, B9
board[2][0]['text'] == 'X' and board[2][1]['text'] == 'X' and board[2][2]['text'] == 'X'


r0 or r1 or r2

#########################################

def check_win_x():
    row0 = board[0][0]['text'] == 'X' and board[0][1]['text'] == 'X' and board[0][2]['text'] == 'X'
    row1 = board[1][0]['text'] == 'X' and board[1][1]['text'] == 'X' and board[1][2]['text'] == 'X'
    row2 = board[2][0]['text'] == 'X' and board[2][1]['text'] == 'X' and board[2][2]['text'] == 'X'
    return row0 or row1 or row2


#########################################

Step.17  -->  show_winner


def show_winner():
    print("X player win.")


def show_winner():
    m = "X player win."
    messagebox.showinfo("Game Over", m)


#########################################

Step.18  -->  update new data to button

b.update_idletasks()

#########################################

Step.19  -->  Checking winner for all player


def check_win():
    row0 = board[0][0]['text'] == current_player and board[0][1]['text'] == current_player and board[0][2]['text'] == current_player
    row1 = board[1][0]['text'] == current_player and board[1][1]['text'] == current_player and board[1][2]['text'] == current_player
    row2 = board[2][0]['text'] == current_player and board[2][1]['text'] == current_player and board[2][2]['text'] == current_player
    return row0 or row1 or row2


def show_winner():
    m = f"{current_player} player win."
    messagebox.showinfo("Game Over", m)


#########################################

Step.20  -->  Checking winner (3 columns + 2 diagonals)

          C0     C1     C2                C9

row 0     B1     B2     B3
row 1     B4     B5     B6
row 2     B7     B8     B9

col 0   =>  1, 4, 7
col 1   =>  2, 5, 8
col 2   =>  3, 6, 9

col0 = board[0][0]['text'] == current_player and board[1][0]['text'] == current_player and board[2][0]['text'] == current_player
col1 = board[0][1]['text'] == current_player and board[1][1]['text'] == current_player and board[2][1]['text'] == current_player
col2 = board[0][2]['text'] == current_player and board[1][2]['text'] == current_player and board[2][2]['text'] == current_player

diagonal1 =>  1, 5, 9
diagonal1 = board[0][0]['text'] == current_player and board[1][1]['text'] == current_player and board[2][2]['text'] == current_player

diagonal2 =>  3, 5, 7
diagonal2 = board[0][2]['text'] == current_player and board[1][1]['text'] == current_player and board[2][0]['text'] == current_player

#########################################

def check_win():
    row0 = board[0][0]['text'] == current_player and board[0][1]['text'] == current_player and board[0][2]['text'] == current_player
    row1 = board[1][0]['text'] == current_player and board[1][1]['text'] == current_player and board[1][2]['text'] == current_player
    row2 = board[2][0]['text'] == current_player and board[2][1]['text'] == current_player and board[2][2]['text'] == current_player

    col0 = board[0][0]['text'] == current_player and board[1][0]['text'] == current_player and board[2][0]['text'] == current_player
    col1 = board[0][1]['text'] == current_player and board[1][1]['text'] == current_player and board[2][1]['text'] == current_player
    col2 = board[0][2]['text'] == current_player and board[1][2]['text'] == current_player and board[2][2]['text'] == current_player

    diagonal1 = board[0][0]['text'] == current_player and board[1][1]['text'] == current_player and board[2][2]['text'] == current_player
    diagonal2 = board[0][2]['text'] == current_player and board[1][1]['text'] == current_player and board[2][0]['text'] == current_player

    return row0 or row1 or row2 or col0 or col1 or col2 or diagonal1 or diagonal2

#########################################

Step.21  -->  Game restart


def restart():
    board[0][0]['text'] = ''
    board[0][1]['text'] = ''
    board[0][2]['text'] = ''

    board[1][0]['text'] = ''
    board[1][1]['text'] = ''
    board[1][2]['text'] = ''

    board[2][0]['text'] = ''
    board[2][1]['text'] = ''
    board[2][2]['text'] = ''


def restart():
    for row in range(3):
        for col in range(3):
            board[row][col]['text'] = ''

#########################################

from tkinter import *
from tkinter import messagebox


current_player = "X"
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],

]


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def f(e):
    b = e.widget
    if b['text']:
        return
    b["text"] = current_player
    b.update_idletasks()
    if check_win():
        show_winner()
        restart()
    switch_player()


def show_winner():
    m = f"{current_player} player win."
    messagebox.showinfo("Game Over", m)


def check_win():
    row0 = board[0][0]['text'] == current_player and board[0][1]['text'] == current_player and board[0][2]['text'] == current_player
    row1 = board[1][0]['text'] == current_player and board[1][1]['text'] == current_player and board[1][2]['text'] == current_player
    row2 = board[2][0]['text'] == current_player and board[2][1]['text'] == current_player and board[2][2]['text'] == current_player

    col0 = board[0][0]['text'] == current_player and board[1][0]['text'] == current_player and board[2][0]['text'] == current_player
    col1 = board[0][1]['text'] == current_player and board[1][1]['text'] == current_player and board[2][1]['text'] == current_player
    col2 = board[0][2]['text'] == current_player and board[1][2]['text'] == current_player and board[2][2]['text'] == current_player

    diagonal1 = board[0][0]['text'] == current_player and board[1][1]['text'] == current_player and board[2][2]['text'] == current_player
    diagonal2 = board[0][2]['text'] == current_player and board[1][1]['text'] == current_player and board[2][0]['text'] == current_player

    return row0 or row1 or row2 or col0 or col1 or col2 or diagonal1 or diagonal2


def restart():
    board[0][0]['text'] = ''
    board[0][1]['text'] = ''
    board[0][2]['text'] = ''

    board[1][0]['text'] = ''
    board[1][1]['text'] = ''
    board[1][2]['text'] = ''

    board[2][0]['text'] = ''
    board[2][1]['text'] = ''
    board[2][2]['text'] = ''


x = Tk()
x.title("Tac Ti Toe")

for row in range(3):
    for col in range(3):
        b = Button(x, width=8, height=4, text='', font=('Arial', 30, 'bold'))
        b.grid(row=row, column=col)
        b.bind("<Button-1>", f)
        board[row][col] = b


x.mainloop()

##################################################################################




"""

