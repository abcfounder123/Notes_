
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

#########################################


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B1').grid(row=0, column=0)

x.mainloop()

#########################################

Step.3  -->   label


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B1')

b1.grid(row=0, column=0)

x.mainloop()

#########################################

Step.4, 5  -->  button 3, 9


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B1')
b2 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B2')
b3 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B3')

b4 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B4')
b5 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B5')
b6 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B6')

b7 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B7')
b8 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B8')
b9 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B9')

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

Step.6  -->  nested loop

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


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

for row in range(3): # 0
    for col in range(3): # 0 1 2
        Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='B1').grid(row=row, column=col)


x.mainloop()

#########################################

Step.7.1    -->   B1, B2, B3, ..., B9
           

from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text=f'B{n}').grid(row=row, column=col)

x.mainloop()

#########################################

Step.7.2   -->   empty text   =>   text=''


from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='').grid(row=row, column=col)

x.mainloop()

#########################################

Step.8  -->  if left click 1, show X

b.bind("<Button-1>", click)


def click(event):
    b = event.widget
    b['text'] = "X"
    

#########################################


from tkinter import *


def click(event):
    b = event.widget
    b['text'] = "X"


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=col)
        b.bind("<Button-1>", click)

x.mainloop()

#########################################

Step.9 -->  switch player ( X, O )

def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
        
#########################################


from tkinter import *


current_player = "X"


def click(event):
    b = event.widget
    b['text'] = current_player
    switch_player()


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=col)
        b.bind("<Button-1>", click)

x.mainloop()

#########################################

Step.10 --> control to draw once

idea -> if somthing value, stop function and do nothing
code -> if b['text']: return

''     False
"X"    True
"O"    True

#########################################


from tkinter import *


current_player = "X"


def click(event):
    b = event.widget
    if b['text']:
        return
    b['text'] = current_player
    switch_player()


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=col)
        b.bind("<Button-1>", click)

x.mainloop()

#########################################

Step.11 -->  board and winner()


 c0     c1    c2

  .     .     .           r0   X     X     X

  .     .     .           r1

  .     .     .           r2


row       3
column    3
diagonal  2

r0   (1, 2, 3) (and)
board[0][0]['text'] == 'X'
board[0][1]['text'] == 'X'
board[0][2]['text'] == 'X'

r1   (4, 5, 6)
board[1][0]['text'] == 'X'
board[1][1]['text'] == 'X'
board[1][2]['text'] == 'X'

r2   (7, 8, 9)
board[2][0]['text'] == 'X'
board[2][1]['text'] == 'X'
board[2][2]['text'] == 'X'

c0   (1, 4, 7)
board[0][0]['text'] == 'X'
board[1][0]['text'] == 'X'
board[2][0]['text'] == 'X'

c1   (2, 5, 8)
board[0][1]['text'] == 'X'
board[1][1]['text'] == 'X'
board[2][1]['text'] == 'X'

c2   (3, 6, 9)
board[0][2]['text'] == 'X'
board[1][2]['text'] == 'X'
board[2][2]['text'] == 'X'


d1   (1, 5, 9)
board[0][0]['text'] == 'X'
board[1][1]['text'] == 'X'
board[2][2]['text'] == 'X'

d2   (3, 5, 7)
board[0][2]['text'] == 'X'
board[1][1]['text'] == 'X'
board[2][0]['text'] == 'X'

or

#########################################

Step.11.1   -->   create empty board and added buttons

board (2D)

  .     .     .

  .     .     .

  .     .     .

#########################################

1D data

r0 = ["b1", "b2", "b3"]

r0[0]
r0[1]
r0[2]

r1 = ["b4", "b5", "b6"]

r1[0]
r1[1]
r1[2]

r2 = ["b7", "b8", "b9"]

r2[0]
r2[1]
r2[2]

#########################################

2D data

board = [r0, r1, r2]



  .     .     .

  .     .     .

  .     .     .


board = [
         ["b1", "b2", "b3"],
         ["b4", "b5", "b6"],
         ["b7", "b8", "b9"]

         ]

board[0]
board[1]
board[2]

"b1"
board[0][0]

"b5"
board[1][1]

"b9"
board[2][2]

#########################################

Empty board

board = [
         [None, None, None],
         [None, None, None],
         [None, None, None]

         ]

#########################################

Sample of adding buttons


board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]

]


board[0][0] = "b1"
print(board)

board[1][1] = "b5"
print(board)

board[2][2] = "b9"
print(board)


#########################################

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]

]

board[row][col] = b

#########################################


from tkinter import *


current_player = "X"

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]

]


def click(event):
    b = event.widget
    if b['text']:
        return
    b['text'] = current_player
    switch_player()


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


x = Tk()
x.title("Tac Ti Toe")

print(board)

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=col)
        b.bind("<Button-1>", click)
        board[row][col] = b

print(board)

x.mainloop()

#########################################

Step.11.2   -->  Check for player X
  

def winX():
    # r0   (1, 2, 3)
    if board[0][0]['text'] == 'X' and board[0][1]['text'] == 'X' and board[0][2]['text'] == 'X':
        return True
    # r1   (4, 5, 6)
    if board[1][0]['text'] == 'X' and board[1][1]['text'] == 'X' and board[1][2]['text'] == 'X':
        return True
    # r2   (7, 8, 9)
    if board[2][0]['text'] == 'X' and board[2][1]['text'] == 'X' and board[2][2]['text'] == 'X':
        return True

    # c0(1, 4, 7)
    if board[0][0]['text'] == 'X' and board[1][0]['text'] == 'X' and board[2][0]['text'] == 'X':
        return True

    # c1(2, 5, 8)
    if board[0][1]['text'] == 'X' and board[1][1]['text'] == 'X' and board[2][1]['text'] == 'X':
        return True

    # c2(3, 6, 9)
    if board[0][2]['text'] == 'X' and board[1][2]['text'] == 'X' and board[2][2]['text'] == 'X':
        return True

    # d1(1, 5, 9)
    if board[0][0]['text'] == 'X' and board[1][1]['text'] == 'X' and board[2][2]['text'] == 'X':
        return True

    # d2(3, 5, 7)
    if board[0][2]['text'] == 'X' and board[1][1]['text'] == 'X' and board[2][0]['text'] == 'X':
        return True


#########################################

Step.11.3   -->  Check for current player 


def winner():
    # r0   (1, 2, 3)
    if board[0][0]['text'] == current_player and board[0][1]['text'] == current_player and board[0][2]['text'] == current_player:
        return True
    # r1   (4, 5, 6)
    if board[1][0]['text'] == current_player and board[1][1]['text'] == current_player and board[1][2]['text'] == current_player:
        return True
    # r2   (7, 8, 9)
    if board[2][0]['text'] == current_player and board[2][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # c0(1, 4, 7)
    if board[0][0]['text'] == current_player and board[1][0]['text'] == current_player and board[2][0]['text'] == current_player:
        return True

    # c1(2, 5, 8)
    if board[0][1]['text'] == current_player and board[1][1]['text'] == current_player and board[2][1]['text'] == current_player:
        return True

    # c2(3, 6, 9)
    if board[0][2]['text'] == current_player and board[1][2]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d1(1, 5, 9)
    if board[0][0]['text'] == current_player and board[1][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d2(3, 5, 7)
    if board[0][2]['text'] == current_player and board[1][1]['text'] == current_player and board[2][0]['text'] == current_player:
        return True

#########################################


from tkinter import *
from tkinter import messagebox


current_player = "X"
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]

]


def click(event):
    b = event.widget
    if b['text']:
        return
    b['text'] = current_player
    if winner():
        show_winner()

    switch_player()


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def winner():
    # r0   (1, 2, 3)
    if board[0][0]['text'] == current_player and board[0][1]['text'] == current_player and board[0][2]['text'] == current_player:
        return True
    # r1   (4, 5, 6)
    if board[1][0]['text'] == current_player and board[1][1]['text'] == current_player and board[1][2]['text'] == current_player:
        return True
    # r2   (7, 8, 9)
    if board[2][0]['text'] == current_player and board[2][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # c0(1, 4, 7)
    if board[0][0]['text'] == current_player and board[1][0]['text'] == current_player and board[2][0]['text'] == current_player:
        return True

    # c1(2, 5, 8)
    if board[0][1]['text'] == current_player and board[1][1]['text'] == current_player and board[2][1]['text'] == current_player:
        return True

    # c2(3, 6, 9)
    if board[0][2]['text'] == current_player and board[1][2]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d1(1, 5, 9)
    if board[0][0]['text'] == current_player and board[1][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d2(3, 5, 7)
    if board[0][2]['text'] == current_player and board[1][1]['text'] == current_player and board[2][0]['text'] == current_player:
        return True


def show_winner():
    m = f"Player {current_player} win!"
    messagebox.showinfo("Game Over", m)


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=col)
        b.bind("<Button-1>", click)
        board[row][col] = b

x.mainloop()

#########################################

Step.12 -->  restart  (empty text)


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

#########################################

from tkinter import *
from tkinter import messagebox


current_player = "X"
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]

]


def click(event):
    b = event.widget
    if b['text']:
        return
    b['text'] = current_player

    if winner():
        show_winner()
        restart()

    switch_player()


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def winner():
    # r0   (1, 2, 3)
    if board[0][0]['text'] == current_player and board[0][1]['text'] == current_player and board[0][2]['text'] == current_player:
        return True
    # r1   (4, 5, 6)
    if board[1][0]['text'] == current_player and board[1][1]['text'] == current_player and board[1][2]['text'] == current_player:
        return True
    # r2   (7, 8, 9)
    if board[2][0]['text'] == current_player and board[2][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # c0(1, 4, 7)
    if board[0][0]['text'] == current_player and board[1][0]['text'] == current_player and board[2][0]['text'] == current_player:
        return True

    # c1(2, 5, 8)
    if board[0][1]['text'] == current_player and board[1][1]['text'] == current_player and board[2][1]['text'] == current_player:
        return True

    # c2(3, 6, 9)
    if board[0][2]['text'] == current_player and board[1][2]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d1(1, 5, 9)
    if board[0][0]['text'] == current_player and board[1][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d2(3, 5, 7)
    if board[0][2]['text'] == current_player and board[1][1]['text'] == current_player and board[2][0]['text'] == current_player:
        return True


def show_winner():
    m = f"Player {current_player} win!"
    messagebox.showinfo("Game Over", m)


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

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=col)
        b.bind("<Button-1>", click)
        board[row][col] = b

x.mainloop()

#########################################

Step.13 -->  tie()


def tie():
    if board[0][0]['text'] and board[0][1]['text'] and board[0][2]['text'] and board[1][0]['text'] and board[1][1]['text'] and board[1][2]['text'] and board[2][0]['text'] and board[2][1]['text'] and board[2][2]['text']:
        return True

    
def show_tie():
    m = f"Draw!"
    messagebox.showinfo("Game Over", m)


def click():

    if tie():
        show_tie()
        restart()
        

#########################################


from tkinter import *
from tkinter import messagebox


current_player = "X"
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]

]


def click(event):
    b = event.widget
    if b['text']:
        return
    b['text'] = current_player

    if winner():
        show_winner()
        restart()

    if tie():
        show_tie()
        restart()

    switch_player()


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def winner():
    # r0   (1, 2, 3)
    if board[0][0]['text'] == current_player and board[0][1]['text'] == current_player and board[0][2]['text'] == current_player:
        return True
    # r1   (4, 5, 6)
    if board[1][0]['text'] == current_player and board[1][1]['text'] == current_player and board[1][2]['text'] == current_player:
        return True
    # r2   (7, 8, 9)
    if board[2][0]['text'] == current_player and board[2][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # c0(1, 4, 7)
    if board[0][0]['text'] == current_player and board[1][0]['text'] == current_player and board[2][0]['text'] == current_player:
        return True

    # c1(2, 5, 8)
    if board[0][1]['text'] == current_player and board[1][1]['text'] == current_player and board[2][1]['text'] == current_player:
        return True

    # c2(3, 6, 9)
    if board[0][2]['text'] == current_player and board[1][2]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d1(1, 5, 9)
    if board[0][0]['text'] == current_player and board[1][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d2(3, 5, 7)
    if board[0][2]['text'] == current_player and board[1][1]['text'] == current_player and board[2][0]['text'] == current_player:
        return True


def show_winner():
    m = f"Player {current_player} win!"
    messagebox.showinfo("Game Over", m)


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


def tie():
    if board[0][0]['text'] and board[0][1]['text'] and board[0][2]['text'] and board[1][0]['text'] and board[1][1]['text'] and board[1][2]['text'] and board[2][0]['text'] and board[2][1]['text'] and board[2][2]['text']:
        return True


def show_tie():
    m = f"Draw!"
    messagebox.showinfo("Game Over", m)


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=col)
        b.bind("<Button-1>", click)
        board[row][col] = b

x.mainloop()

##################################################################################

day. 2

Step.14 -->  Scrolls ( Add and show scrolls after game over. )

  .     .     .

  .     .     .

  .     .     .

  X scroll = 0

  O scroll = 0

x_scroll = 0
y_scroll = 0

l1 = Label(x, text="X scroll = 0", font=('Arial', 30, 'bold'))
l1.grid(row=3, columnspan=3)

l2 = Label(x, text="O scroll = 0", font=('Arial', 30, 'bold'))
l1.grid(row=4, columnspan=3)


def show_winner():
    m = f"Player {current_player} win!"
    messagebox.showinfo("Game Over", m)
    if current_player == 'X':
        global x_scroll
        x_scroll += 1
        l1['text'] = f"X scroll = {x_scroll}"
    else:
        global y_scroll
        y_scroll += 1
        l2['text'] = f"O scroll = {x_scroll}"

#########################################

from tkinter import *
from tkinter import messagebox


current_player = "X"
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]

]
x_scroll = 0
y_scroll = 0


def click(event):
    b = event.widget
    if b['text']:
        return
    b['text'] = current_player

    if winner():
        show_winner()
        restart()

    if tie():
        show_tie()
        restart()

    switch_player()


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def winner():
    # r0   (1, 2, 3)
    if board[0][0]['text'] == current_player and board[0][1]['text'] == current_player and board[0][2]['text'] == current_player:
        return True
    # r1   (4, 5, 6)
    if board[1][0]['text'] == current_player and board[1][1]['text'] == current_player and board[1][2]['text'] == current_player:
        return True
    # r2   (7, 8, 9)
    if board[2][0]['text'] == current_player and board[2][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # c0(1, 4, 7)
    if board[0][0]['text'] == current_player and board[1][0]['text'] == current_player and board[2][0]['text'] == current_player:
        return True

    # c1(2, 5, 8)
    if board[0][1]['text'] == current_player and board[1][1]['text'] == current_player and board[2][1]['text'] == current_player:
        return True

    # c2(3, 6, 9)
    if board[0][2]['text'] == current_player and board[1][2]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d1(1, 5, 9)
    if board[0][0]['text'] == current_player and board[1][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d2(3, 5, 7)
    if board[0][2]['text'] == current_player and board[1][1]['text'] == current_player and board[2][0]['text'] == current_player:
        return True


def show_winner():
    m = f"Player {current_player} win!"
    messagebox.showinfo("Game Over", m)
    if current_player == 'X':
        global x_scroll
        x_scroll += 1
        l1['text'] = f"X scroll = {x_scroll}"
    else:
        global y_scroll
        y_scroll += 1
        l2['text'] = f"O scroll = {x_scroll}"


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


def tie():
    if board[0][0]['text'] and board[0][1]['text'] and board[0][2]['text'] and board[1][0]['text'] and board[1][1]['text'] and board[1][2]['text'] and board[2][0]['text'] and board[2][1]['text'] and board[2][2]['text']:
        return True


def show_tie():
    m = f"Draw!"
    messagebox.showinfo("Game Over", m)


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=col)
        b.bind("<Button-1>", click)
        board[row][col] = b

l1 = Label(x, text="X scroll = 0", font=('Arial', 30, 'bold'))
l1.grid(row=3, columnspan=3)

l2 = Label(x, text="O scroll = 0", font=('Arial', 30, 'bold'))
l2.grid(row=4, columnspan=3)

x.mainloop()

#########################################

Step.15 -->  fg color

X    purple
O    blue

if current_player == 'X':
    b['fg'] = 'purple'
else:
    b['fg'] = 'blue'


def click(event):
    b = event.widget

    if b['text']:
        return

    if current_player == 'X':
        b['fg'] = 'purple'
    else:
        b['fg'] = 'blue'

    b['text'] = current_player

    if winner():
        show_winner()
        restart()

    if tie():
        show_tie()
        restart()

    switch_player()


#########################################


from tkinter import *
from tkinter import messagebox


current_player = "X"
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]

]
x_scroll = 0
y_scroll = 0


def click(event):
    b = event.widget

    if b['text']:
        return

    if current_player == 'X':
        b['fg'] = 'purple'
    else:
        b['fg'] = 'blue'

    b['text'] = current_player

    if winner():
        show_winner()
        restart()

    if tie():
        show_tie()
        restart()

    switch_player()


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def winner():
    # r0   (1, 2, 3)
    if board[0][0]['text'] == current_player and board[0][1]['text'] == current_player and board[0][2]['text'] == current_player:
        return True
    # r1   (4, 5, 6)
    if board[1][0]['text'] == current_player and board[1][1]['text'] == current_player and board[1][2]['text'] == current_player:
        return True
    # r2   (7, 8, 9)
    if board[2][0]['text'] == current_player and board[2][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # c0(1, 4, 7)
    if board[0][0]['text'] == current_player and board[1][0]['text'] == current_player and board[2][0]['text'] == current_player:
        return True

    # c1(2, 5, 8)
    if board[0][1]['text'] == current_player and board[1][1]['text'] == current_player and board[2][1]['text'] == current_player:
        return True

    # c2(3, 6, 9)
    if board[0][2]['text'] == current_player and board[1][2]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d1(1, 5, 9)
    if board[0][0]['text'] == current_player and board[1][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d2(3, 5, 7)
    if board[0][2]['text'] == current_player and board[1][1]['text'] == current_player and board[2][0]['text'] == current_player:
        return True


def show_winner():
    m = f"Player {current_player} win!"
    messagebox.showinfo("Game Over", m)
    if current_player == 'X':
        global x_scroll
        x_scroll += 1
        l1['text'] = f"X scroll = {x_scroll}"
    else:
        global y_scroll
        y_scroll += 1
        l2['text'] = f"O scroll = {x_scroll}"


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


def tie():
    if board[0][0]['text'] and board[0][1]['text'] and board[0][2]['text'] and board[1][0]['text'] and board[1][1]['text'] and board[1][2]['text'] and board[2][0]['text'] and board[2][1]['text'] and board[2][2]['text']:
        return True


def show_tie():
    m = f"Draw!"
    messagebox.showinfo("Game Over", m)


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=col)
        b.bind("<Button-1>", click)
        board[row][col] = b

l1 = Label(x, text="X scroll = 0", font=('Arial', 30, 'bold'))
l1.grid(row=3, columnspan=3)

l2 = Label(x, text="O scroll = 0", font=('Arial', 30, 'bold'))
l2.grid(row=4, columnspan=3)

x.mainloop()

#########################################

Step.16   --->   Making application

Window computer
1. pip3 install pyinstaller
3. python3 -m PyInstaller --onefile --windowed ttt.py

################################################

Macbook
1. bash
2. cd/Users/myothantzin/PycharmProjects/NewCourse2025
3. python3 -m PyInstaller --onefile --windowed ttt.py

Build complete! The results are available in: /Users/myothantzin/PycharmProjects/NewCourse2025/dist

right click => open => finder

################################################

from tkinter import *
from tkinter import messagebox


current_player = "X"
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]

]
x_scroll = 0
y_scroll = 0


def click(event):
    b = event.widget

    if b['text']:
        return

    if current_player == 'X':
        b['fg'] = 'purple'
    else:
        b['fg'] = 'blue'

    b['text'] = current_player

    if winner():
        show_winner()
        restart()

    if tie():
        show_tie()
        restart()

    switch_player()


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def winner():
    # r0   (1, 2, 3)
    if board[0][0]['text'] == current_player and board[0][1]['text'] == current_player and board[0][2]['text'] == current_player:
        return True
    # r1   (4, 5, 6)
    if board[1][0]['text'] == current_player and board[1][1]['text'] == current_player and board[1][2]['text'] == current_player:
        return True
    # r2   (7, 8, 9)
    if board[2][0]['text'] == current_player and board[2][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # c0(1, 4, 7)
    if board[0][0]['text'] == current_player and board[1][0]['text'] == current_player and board[2][0]['text'] == current_player:
        return True

    # c1(2, 5, 8)
    if board[0][1]['text'] == current_player and board[1][1]['text'] == current_player and board[2][1]['text'] == current_player:
        return True

    # c2(3, 6, 9)
    if board[0][2]['text'] == current_player and board[1][2]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d1(1, 5, 9)
    if board[0][0]['text'] == current_player and board[1][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d2(3, 5, 7)
    if board[0][2]['text'] == current_player and board[1][1]['text'] == current_player and board[2][0]['text'] == current_player:
        return True


def show_winner():
    m = f"Player {current_player} win!"
    messagebox.showinfo("Game Over", m)
    if current_player == 'X':
        global x_scroll
        x_scroll += 1
        l1['text'] = f"X scroll = {x_scroll}"
    else:
        global y_scroll
        y_scroll += 1
        l2['text'] = f"O scroll = {x_scroll}"


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


def tie():
    if board[0][0]['text'] and board[0][1]['text'] and board[0][2]['text'] and board[1][0]['text'] and board[1][1]['text'] and board[1][2]['text'] and board[2][0]['text'] and board[2][1]['text'] and board[2][2]['text']:
        return True


def show_tie():
    m = f"Draw!"
    messagebox.showinfo("Game Over", m)


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        b = Button(x, width=10, height=5, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=col)
        b.bind("<Button-1>", click)
        board[row][col] = b

l1 = Label(x, text="X scroll = 0", font=('Arial', 30, 'bold'))
l1.grid(row=3, columnspan=3)

l2 = Label(x, text="O scroll = 0", font=('Arial', 30, 'bold'))
l2.grid(row=4, columnspan=3)

x.mainloop()

################################################

Step.17   --->   computer (random)


def computer():
    while True:
        p = randrange(1, 10) # 1 to 9  => 5
        r = (p - 1) // 3  # 1
        c = (p - 1) % 3   # 1
        if not board[r][c]['text']:
            board[r][c]['text'] = current_player
            break
            
            
################################################            

from tkinter import *
from tkinter import messagebox
from random import randrange


current_player = "X"
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]

]
x_scroll = 0
y_scroll = 0


def click(event):
    b = event.widget

    if b['text']:
        return

    if current_player == 'X':
        b['fg'] = 'purple'
    else:
        b['fg'] = 'blue'

    b['text'] = current_player

    if winner():
        show_winner()
        restart()

    if tie():
        show_tie()
        restart()

    switch_player()

    computer()
    
    if winner():
        show_winner()
        restart()

    if tie():
        show_tie()
        restart()

    switch_player()


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def winner():
    # r0   (1, 2, 3)
    if board[0][0]['text'] == current_player and board[0][1]['text'] == current_player and board[0][2]['text'] == current_player:
        return True
    # r1   (4, 5, 6)
    if board[1][0]['text'] == current_player and board[1][1]['text'] == current_player and board[1][2]['text'] == current_player:
        return True
    # r2   (7, 8, 9)
    if board[2][0]['text'] == current_player and board[2][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # c0(1, 4, 7)
    if board[0][0]['text'] == current_player and board[1][0]['text'] == current_player and board[2][0]['text'] == current_player:
        return True

    # c1(2, 5, 8)
    if board[0][1]['text'] == current_player and board[1][1]['text'] == current_player and board[2][1]['text'] == current_player:
        return True

    # c2(3, 6, 9)
    if board[0][2]['text'] == current_player and board[1][2]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d1(1, 5, 9)
    if board[0][0]['text'] == current_player and board[1][1]['text'] == current_player and board[2][2]['text'] == current_player:
        return True

    # d2(3, 5, 7)
    if board[0][2]['text'] == current_player and board[1][1]['text'] == current_player and board[2][0]['text'] == current_player:
        return True


def show_winner():
    m = f"Player {current_player} win!"
    messagebox.showinfo("Game Over", m)
    if current_player == 'X':
        global x_scroll
        x_scroll += 1
        l1['text'] = f"X scroll = {x_scroll}"
    else:
        global y_scroll
        y_scroll += 1
        l2['text'] = f"O scroll = {x_scroll}"


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


def tie():
    if board[0][0]['text'] and board[0][1]['text'] and board[0][2]['text'] and board[1][0]['text'] and board[1][1]['text'] and board[1][2]['text'] and board[2][0]['text'] and board[2][1]['text'] and board[2][2]['text']:
        return True


def show_tie():
    m = f"Draw!"
    messagebox.showinfo("Game Over", m)


def computer():
    while True:
        p = randrange(1, 10) # 1 to 9  => 5
        r = (p - 1) // 3  # 1
        c = (p - 1) % 3   # 1
        if not board[r][c]['text']:
            board[r][c]['text'] = current_player
            break


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3): # 0
    for col in range(3): # 0 1 2
        n += 1
        b = Button(x, width=10, height=5, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=col)
        b.bind("<Button-1>", click)
        board[row][col] = b

l1 = Label(x, text="X scroll = 0", font=('Arial', 30, 'bold'))
l1.grid(row=3, columnspan=3)

l2 = Label(x, text="O scroll = 0", font=('Arial', 30, 'bold'))
l2.grid(row=4, columnspan=3)

x.mainloop()

################################################################################################



"""

