"""

CLI for Tac Ti Toe game

lesson.1 ( လူနှစ်ယောက်ဆော့ရန် ရေးသားခြင်း )

################################################

Step.1   --->   နေရာချခြင်း

print("+-------" * 3 + "+")
print("|       " * 3 + "|")
print("|   7   " * 3 + "|")
print("|       " * 3 + "|")
print("+-------" * 3 + "+")

################################################

Step.2   --->   variable number

n = 1
print("+-------" * 3 + "+")
print("|       " * 3 + "|")
print(f"|   {n}   " * 3 + "|")
print("|       " * 3 + "|")
print("+-------" * 3 + "+")

################################################

Step.3   --->   loop

n = 5

# 1
print(f"|   {n}   " * 3 + "|")

# 2
print(f"|   {n}   ", end="")
print(f"|   {n}   ", end="")
print(f"|   {n}   ", end="")
print("|")

# 3
for i in range(0, 3, 1):
    print(f"|   {i}   ", end="")

print("|")    

################################################

Step.4   --->   step.2 + step.3

print("+-------" * 3 + "+")
print("|       " * 3 + "|")

for i in range(0, 3, 1):
    print(f"|   {i}   ", end="")

print("|")

print("|       " * 3 + "|")
print("+-------" * 3 + "+")

################################################

Step.5   --->   n တန်ဖိုး‌ကို တည်နေရာ နဲ့ထုတ်မယ်။

n = [1, 2, 3]

print("+-------" * 3 + "+")
print("|       " * 3 + "|")

for i in range(0, 3, 1):
    print(f"|   {n[i]}   ", end="")

print("|")

print("|       " * 3 + "|")
print("+-------" * 3 + "+")

################################################

Step.6   --->   သုံးကြိမ်လုပ်ခိုင်းမယ်။ ( nested loop )

n = [1,2,3]

print("+-------" * 3,"+",sep="")

for i in range(3):
    print("|       " * 3 + "|")

    for i in range(0, 3, 1):
        print(f"|   {n[i]}   ", end="")

    print("|")

    print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

################################################

Step.7   --->   2D ပုံစံနဲ့ n တန်ဖိုးကို ထုတ်မယ်။  [list.1, list.2, list.3]

# n[0]    => [1,2,3]
# n[0][0] => 1
# n[0][1] => 2
# n[0][2] => 3

n = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print("+-------" * 3,"+",sep="")

for r in range(3): # range(3), range(0, 3, 1) => 0, 1, 2
    print("|       " * 3 + "|")

    for c in range(3): # 0 1 2
        print(f"|   {n[r][c]}   ", end="")

    print("|")

    print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

################################################

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
[Program finished]

################################################

Step.8   --->   function အဖြစ် ပြောင်းမယ်။

board = [[1,2,3],
        [4,5,6],
        [7,8,9]]


def draw():
    print("+-------" * 3, "+", sep="")

    for r in range(3):  # range(0, 3, 1) => 0, 1, 2
        print("|       " * 3 + "|")

        for c in range(3):  # 0 1 2
            print(f"|   {board[r][c]}   ", end="")

        print("|")

        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")

draw()

################################################

# n တန်ဖိုးပြောင်းတာကို ကြည့်ပါ။

board = [[1,2,3],
        [4,5,6],
        [7,8,9]]


def draw():
    print("+-------" * 3, "+", sep="")

    for r in range(3):  # range(3), range(0, 3, 1) => 0, 1, 2
        print("|       " * 3 + "|")

        for c in range(3):  # 0 1 2
            print(f"|   {board[r][c]}   ", end="")

        print("|")

        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")



draw()

x = "X"
board = [[x,2,3],
        [4,x,6],
        [7,8,x]]

draw()

################################################

Step.9   --->   X ကို တည်နေရာနဲ့ ထည့်ခြင်း

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]


def draw():
    print("+-------" * 3, "+", sep="")

    for r in range(3):  # range(3), range(0, 3, 1) => 0, 1, 2
        print("|       " * 3 + "|")

        for c in range(3):  # 0 1 2
            print(f"|   {board[r][c]}   ", end="")

        print("|")

        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


draw()

# board တန်ဖိုးကို တည်နေရာနဲ့ ပြောင်းပါမယ်။
board[0][0] = "X"
board[1][1] = "X"
board[2][2] = "X"
board[2][0] = "O"
draw()

################################################

Step.10   --->   ပုံသေနည်းထုတ်ခြင်း

# n[2][2] = "X"  
# တည်နေရာ  2  , 2 ဟာ no.9 တန်ဖိုးရဲ့နေရာပါ။ 
# 9 ထည့်ရင် 2, 2 ထွက်ဖို့ အောက်က ပုံသေနည်းနဲ့ တွက်နိုင်ပါတယ်။
p = 9
r = (p-1) // 3        # 2
c = (p-1) % 3         # 2
n[r][c] = "X"
draw(n)

################################################

Step.11   --->   ပုံသေနည်းစမ်းသပ်ခြင်း

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]


def draw():
    print("+-------" * 3, "+", sep="")

    for r in range(3):  # range(3), range(0, 3, 1) => 0, 1, 2
        print("|       " * 3 + "|")

        for c in range(3):  # 0 1 2
            print(f"|   {board[r][c]}   ", end="")

        print("|")

        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


draw()

p = int(input("Enter your move : "))
r = (p-1) // 3
c = (p-1) % 3
board[r][c] = "X"

draw()

################################################

Step.12   --->  move function အဖြစ် ပြောင်းပါတယ်။

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]


def draw():
    print("+-------" * 3, "+", sep="")

    for r in range(3):  # range(3), range(0, 3, 1) => 0, 1, 2
        print("|       " * 3 + "|")

        for c in range(3):  # 0 1 2
            print(f"|   {board[r][c]}   ", end="")

        print("|")

        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def move():
    p = int(input("Enter your move : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "X"


draw()

move()
draw()

move()
draw()

move()
draw()

################################################################################################

Step.13   --->   အနိုင်အရှုံး စစ်ဆေးခြင်း

#စမ်းပါ။

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]
print(board[0])
print(board[0][0])
print(board[0][1])
print(board[0][2])

board[0][0] = "X"
board[0][1] = "O"
board[0][2] = "X"

print(board[0][0] == "X")
print(board[0][1] == "X")
print(board[0][2] == "X")

################################################

Step.13.1   --->   row တစ်ခုစီမှာ X တန်ဖိုးပါလား စစ်ပါမယ်။


board = [
         ["X","X","X"],
         [4,5,6],
         [7,8,9]
]
# win = True and True and True  # assignment 1 (14), logical AND 2  (11), left-sided bind

# row 0 ကိုစစ်ပါမယ်။
row_0 = board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X"
print(row_0)

# row 1 ကိုစစ်ပါမယ်။
row_1 = board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X"
print(row_1)

# row 2 ကိုစစ်ပါမယ်။
row_2 = board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X"
print(row_2)

################################################

Step.13.2   --->   Column တစ်ခုစီမှာ X တန်ဖိုးပါလား စစ်ပါမယ်။

board = [
         [1, 2, "X"],
         [4, 5, "X"],
         [7, 8, "X"]
]
print(board[0]) # [1, 2, 3]
print(board[0][0]) # 1

print(board[1]) # [4, 5, 6]
print(board[1][0]) # 4

print(board[2]) # [7, 8, 9]
print(board[2][0]) # 7

# column 0 ကိုစစ်ပါမယ်။
col_0 = board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X"
print(col_0)

# column 1 ကိုစစ်ပါမယ်။
col_1 = board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X"
print(col_1)

# column 2 ကိုစစ်ပါမယ်။
col_2 = board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"
print(col_2)

################################################
#############################################

Step.13.3   --->   ထောင့်ဖြတ်များ X ဟုတ်/မဟုတ် စစ်ပါမယ်။

board = [
         [1, 2, "X"],
         [4, "X", 6],
         ["X", 8, 9]
]

print(board[0])
print(board[0][0])
print(board[1])
print(board[1][1])
print(board[2])
print(board[2][2])

diagonal_1 = board[0][0] == "X" and  board[1][1] == "X" and board[2][2] == "X"
print(diagonal_1)

diagonal_2 = board[0][2] == "X" and  board[1][1] == "X" and board[2][0] == "X"
print(diagonal_2)

################################################

Step.13   --->   အနိုင်အရှုံးစစ်ဆေးခြင်း 

# row သုံးခုကို စစ်ခြင်း
row_0 = board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X"
row_1 = board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X"
row_2 = board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X"

# column သုံးခုကို စစ်ခြင်း
col_0 = board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X"
col_1 = board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X"
col_2 = board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"

#ထောင့်ဖြတ်နှစ်ခုကို စစ်ခြင်း
diagonal_1 = board[0][0] == "X" and  board[1][1] == "X" and board[2][2] == "X"
diagonal_2 = board[0][2] == "X" and  board[1][1] == "X" and board[2][0] == "X"

################################################

Step.14   --->   Step.12 + Step.13

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]


def draw():
    print("+-------" * 3, "+", sep="")

    for r in range(3):  # range(3), range(0, 3, 1) => 0, 1, 2
        print("|       " * 3 + "|")

        for c in range(3):  # 0 1 2
            print(f"|   {board[r][c]}   ", end="")

        print("|")

        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def player_one():
    p = int(input("Enter your move : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "X"


def player_two():
    p = int(input("Enter your move : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "O"


draw()

player_one()
draw()

player_one()
draw()

player_one()
draw()

# row သုံးခုကို စစ်ခြင်း
row_0 = board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X"
row_1 = board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X"
row_2 = board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X"

# column သုံးခုကို စစ်ခြင်း
col_0 = board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X"
col_1 = board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X"
col_2 = board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"

#ထောင့်ဖြတ်နှစ်ခုကို စစ်ခြင်း
diagonal_1 = board[0][0] == "X" and  board[1][1] == "X" and board[2][2] == "X"
diagonal_2 = board[0][2] == "X" and  board[1][1] == "X" and board[2][0] == "X"

print(row_0, row_1, row_2)
print(col_1, col_2, col_0)
print(diagonal_1, diagonal_2)

################################################

Step.15   --->   program မှာ တူနေတာတွေကို ချုံ့ပါမယ်။

Step.15.1   --->   row 3 ခုအတွက် for loop နဲ့ သုံးကြိမ်ပတ်ပါမယ်။

# row သုံးခုကို စစ်ခြင်း
row_0 = board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X"
row_1 = board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X"
row_2 = board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X"

# ချုံ့ထားသော program
for r in range(3): # 0 1 2
    row = board[r][0] == "X" and  board[r][1] == "X" and board[r][2] == "X"
    print(row)

################################################

Step.15.2   --->   column ကို ချုံ့ခြင်း

col_0 = board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X"
col_1 = board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X"
col_2 = board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"

for c in range(3):  # 0 1 2
    col = board[0][c] == "X" and board[1][c] == "X" and board[2][c] == "X"
    print(col

################################################

Step.15.3   --->   ထောင့်ဖြတ်ကို ချုံ့ခြင်း

diagonal_1 = n[0][0] == "X" and  n[1][1] == "X" and n[2][2] == "X"
print(diagonal_1)
diagonal_2 = n[0][2] == "X" and  n[1][1] == "X" and n[2][0] == "X"
print(diagonal_2)

for a, b, c in [(0, 1, 2), (2, 1, 0)]:  # [(), ()] => (0,1,2)
    diagonal = board[0][a] == "X" and board[1][b] == "X" and board[2][c] == "X"
    print(diagonal)

################################################

Step.16   --->   function အဖြစ်‌ပြောင်းခြင်း

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]


def draw():
    print("+-------" * 3, "+", sep="")

    for r in range(3):  # range(3), range(0, 3, 1) => 0, 1, 2
        print("|       " * 3 + "|")

        for c in range(3):  # 0 1 2
            print(f"|   {board[r][c]}   ", end="")

        print("|")

        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def player_one():
    p = int(input("Enter your move : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "X"


def player_two():
    p = int(input("Enter your move : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "O"


def win():
    # row သုံးခုကို စစ်ခြင်း
    for r in range(3): # 0 1 2
        row = board[r][0] == "X" and  board[r][1] == "X" and board[r][2] == "X"
        print(row)

    # column သုံးခုကို စစ်ခြင်း
    for c in range(3):  # 0 1 2
        col = board[0][c] == "X" and board[1][c] == "X" and board[2][c] == "X"
        print(col)

    # diagonals 2 
    for a, b, c in [(0, 1, 2), (2, 1, 0)]:  # [(), ()] => (0,1,2)
        diagonal = board[0][a] == "X" and board[1][b] == "X" and board[2][c] == "X"
        print(diagonal)


draw()

player_one()
draw()

player_one()
draw()

player_one()
draw()

win()

################################################
  
input အဖြစ် 
1
2
3
ထည့်စမ်းပါ။

################################################

Step.17   --->   X သုံးခုတန်းရင် True / False return ပြန်ခိုင်းပါမယ်။

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]


def draw():
    print("+-------" * 3, "+", sep="")

    for r in range(3):  # range(3), range(0, 3, 1) => 0, 1, 2
        print("|       " * 3 + "|")

        for c in range(3):  # 0 1 2
            print(f"|   {board[r][c]}   ", end="")

        print("|")

        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def player_one():
    p = int(input("Enter your move : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "X"


def player_two():
    p = int(input("Enter your move : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "O"


def win():
    # row သုံးခုကို စစ်ခြင်း
    for r in range(3): # 0 1 2
        row = board[r][0] == "X" and  board[r][1] == "X" and board[r][2] == "X"
        print(f"row{r} = {row}")
        if row:
            return True

    # column သုံးခုကို စစ်ခြင်း
    for c in range(3):  # 0 1 2
        col = board[0][c] == "X" and board[1][c] == "X" and board[2][c] == "X"
        print(f"column {c} = {col}")
        if col:
            return True

    # diagonals 2 
    for a, b, c in [(0, 1, 2), (2, 1, 0)]:  # [(), ()] => (0,1,2)
        diagonal = board[0][a] == "X" and board[1][b] == "X" and board[2][c] == "X"
        print(f"diagonal = {diagonal}")
        if diagonal:
            return True

draw()

player_one()
draw()

player_one()
draw()

player_one()
draw()

result = win()
print(result)

################################################

input အဖြစ် 
3
5
9
ထည့်စမ်းပါ။

################################################

Step.18   --->   player one ကို ထည့်ခိုင်းပါမယ်။ X သုံးခုတန်းရင် ရပ်ပါမယ်။

while True:
    player_one()
    draw()
    if win():
        break

################################################

# လက်တွေ့စမ်းပါမယ်။

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]


def draw():
    print("+-------" * 3, "+", sep="")

    for r in range(3):  # range(3), range(0, 3, 1) => 0, 1, 2
        print("|       " * 3 + "|")

        for c in range(3):  # 0 1 2
            print(f"|   {board[r][c]}   ", end="")

        print("|")

        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def player_one():
    p = int(input("Enter your move : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "X"


def player_two():
    p = int(input("Enter your move : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "O"


def win():
    # row သုံးခုကို စစ်ခြင်း
    for r in range(3): # 0 1 2
        row = board[r][0] == "X" and  board[r][1] == "X" and board[r][2] == "X"
        print(f"row{r} = {row}")
        if row:
            return True

    # column သုံးခုကို စစ်ခြင်း
    for c in range(3):  # 0 1 2
        col = board[0][c] == "X" and board[1][c] == "X" and board[2][c] == "X"
        print(f"column {c} = {col}")
        if col:
            return True

    # diagonals 2
    for a, b, c in [(0, 1, 2), (2, 1, 0)]:  # [(), ()] => (0,1,2)
        diagonal = board[0][a] == "X" and board[1][b] == "X" and board[2][c] == "X"
        print(f"diagonal = {diagonal}")
        if diagonal:
            return True

draw()

while True:
    player_one()
    draw()
    if win():
        break

################################################
        
Step.19   --->   player one + player two

while True:
    player_one()
    draw()
    if win():
        break

    player_two()
    draw()
    if win():
        break

################################################

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]


def draw():
    print("+-------" * 3, "+", sep="")

    for r in range(3):  # range(3), range(0, 3, 1) => 0, 1, 2
        print("|       " * 3 + "|")

        for c in range(3):  # 0 1 2
            print(f"|   {board[r][c]}   ", end="")

        print("|")

        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def player_one():
    p = int(input("Enter player one move ( X ) : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "X"


def player_two():
    p = int(input("Enter player two move ( O ) : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "O"


def win():
    # row သုံးခုကို စစ်ခြင်း
    for r in range(3): # 0 1 2
        row = board[r][0] == "X" and  board[r][1] == "X" and board[r][2] == "X"
        if row:
            return True

    # column သုံးခုကို စစ်ခြင်း
    for c in range(3):  # 0 1 2
        col = board[0][c] == "X" and board[1][c] == "X" and board[2][c] == "X"
        if col:
            return True

    # diagonals 2
    for a, b, c in [(0, 1, 2), (2, 1, 0)]:  # [(), ()] => (0,1,2)
        diagonal = board[0][a] == "X" and board[1][b] == "X" and board[2][c] == "X"
        if diagonal:
            return True


draw()

while True:
    player_one()
    draw()
    if win():
        break

    player_two()
    draw()
    if win():
        break

################################################

Step.20   --->   win message before program break  

while True:
    player_one()
    draw()
    if win():
        print("Player one win.")
        break

    player_two()
    draw()
    if win():
        print("Player two win.")
        break

################################################   

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]


def draw():
    print("+-------" * 3, "+", sep="")

    for r in range(3):  # range(3), range(0, 3, 1) => 0, 1, 2
        print("|       " * 3 + "|")

        for c in range(3):  # 0 1 2
            print(f"|   {board[r][c]}   ", end="")

        print("|")

        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def player_one():
    p = int(input("Enter player one move ( X ) : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "X"


def player_two():
    p = int(input("Enter player two move ( O ) : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "O"


def win():
    # row သုံးခုကို စစ်ခြင်း
    for r in range(3): # 0 1 2
        row = board[r][0] == "X" and  board[r][1] == "X" and board[r][2] == "X"
        if row:
            return True

    # column သုံးခုကို စစ်ခြင်း
    for c in range(3):  # 0 1 2
        col = board[0][c] == "X" and board[1][c] == "X" and board[2][c] == "X"
        if col:
            return True

    # diagonals 2
    for a, b, c in [(0, 1, 2), (2, 1, 0)]:  # [(), ()] => (0,1,2)
        diagonal = board[0][a] == "X" and board[1][b] == "X" and board[2][c] == "X"
        if diagonal:
            return True


draw()

while True:
    player_one()
    draw()
    if win():
        print("Player one win.")
        break

    player_two()
    draw()
    if win():
        print("Player two win.")
        break

################################################

Step.21   --->   သရေကျ / မကျ စစ်ဆေးခြင်းနှင့် အရောင်များထည့်ခြင်း

def tie():
    print()
    n = 0
    for l in board: #  [1,2,3]
        for b in l: # 1 2 3
            if b in ["\033[1:35:40m" + "X" + "\033[m", "\033[1:34:40m" + "O" + "\033[m"]:
                n += 1
    if n == 9:
        return True

################################################

board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]


def tie():
    print()
    n = 0
    for l in board: #  [1,2,3]
        for b in l: # 1 2 3
            if b in ["\033[1:35:40m" + "X" + "\033[m", "\033[1:34:40m" + "O" + "\033[m"]:
                n += 1
    if n == 9:
        return True


def draw():
    print("+-------" * 3, "+", sep="")

    for r in range(3):  # range(3), range(0, 3, 1) => 0, 1, 2
        print("|       " * 3 + "|")

        for c in range(3):  # 0 1 2
            print(f"|   {board[r][c]}   ", end="")

        print("|")

        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def player_one():
    p = int(input("Enter player one move ( X ) : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "\033[1:35:40m" + "X" + "\033[m"


def player_two():
    p = int(input("Enter player two move ( O ) : "))
    r = (p - 1) // 3
    c = (p - 1) % 3
    board[r][c] = "\033[1:34:40m" + "O" + "\033[m"


def win(symbol):
    # row သုံးခုကို စစ်ခြင်း
    for r in range(3): # 0 1 2
        row = board[r][0] == symbol and  board[r][1] == symbol and board[r][2] == symbol
        if row:
            return True

    # column သုံးခုကို စစ်ခြင်း
    for c in range(3):  # 0 1 2
        col = board[0][c] == symbol and board[1][c] == symbol and board[2][c] == symbol
        if col:
            return True

    # diagonals 2
    for a, b, c in [(0, 1, 2), (2, 1, 0)]:  # [(), ()] => (0,1,2)
        diagonal = board[0][a] == symbol and board[1][b] == symbol and board[2][c] == symbol
        if diagonal:
            return True

draw()

while True:
    player_one()
    draw()
    if win("\033[1:35:40m" + "X" + "\033[m"):
        print("\033[1:35:40m" + "Player one win." + "\033[m")    # "\033[1:35:40m" + "X" + "\033[m"
        break

    if tie():
        print("Tie!")
        break

    player_two()
    draw()
    if win("\033[1:34:40m" + "O" + "\033[m"):
        print("\033[1:34:40m" + "Player two win." + "\033[m")
        break

    if tie():
        print("\033[1:31:40m" + "Tie!")
        break

################################################################################################
      

"""

