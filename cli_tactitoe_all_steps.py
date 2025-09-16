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

Step.22   --->  valid range, draw once, until correct move

idea -> limit valid range   --->   0 < p < 10
idea -> limit to draw once  --->   board[r][c] not in ["X", "O"]
idea -> until correct move  --->   while loop


def player_one():
    while True:
        p = int(input("Enter player one move ( X ) : "))
        r = (p - 1) // 3
        c = (p - 1) % 3
        if 0 < p < 10 and board[r][c] not in ["X", "O"]:
            board[r][c] = "X"
            break
        else:
            print("Invalid move. Try again.\n")


################################################


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
    while True:
        p = int(input("Enter player one move ( X ) : "))
        r = (p - 1) // 3
        c = (p - 1) % 3
        if 0 < p < 10 and board[r][c] not in ["X", "O"]:
            board[r][c] = "X"
            break
        else:
            print("Invalid move. Try again!")
            

def player_two():
    while True:
        p = int(input("Enter player two move ( O ) : "))
        r = (p - 1) // 3
        c = (p - 1) % 3
        if 0 < p < 10 and board[r][c] not in ["X", "O"]:
            board[r][c] = "O"
            break
        else:
            print("Invalid move. Try again!")


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


def tie():
    print()
    n = 0
    for l in board:
        for b in l: 
            if b in ["X", "O"]:
                n += 1
    if n == 9:
        return True


board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]

draw()

while True:
    player_one()
    draw()
    if win():
        print("Player one win.")
        break

    if tie():
        print("Tie!")
        break

    player_two()
    draw()
    if win():
        print("Player two win.")
        break

    if tie():
        print("Tie!")
        break


################################################

Step.23   --->   computer


from random import *


def computer():
    while True:
        p = randrange(1, 10)
        r = (p - 1) // 3
        c = (p - 1) % 3
        if 0 < p < 10 and board[r][c] not in ["X", "O"]:
            board[r][c] = "O"
            break
        else:
            print("Invalid move. Try again.\n")
            
            
################################################            


from random import randrange


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
    while True:
        p = int(input("Enter player one move ( X ) : "))
        r = (p - 1) // 3
        c = (p - 1) % 3
        if 0 < p < 10 and board[r][c] not in ["X", "O"]:
            board[r][c] = "X"
            break
        else:
            print("Invalid move. Try again!")


def computer():
    while True:
        p = randrange(1, 10)
        r = (p - 1) // 3
        c = (p - 1) % 3
        if 0 < p < 10 and board[r][c] not in ["X", "O"]:
            board[r][c] = "O"
            break


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


def tie():
    print()
    n = 0
    for l in board:
        for b in l:
            if b in ["X", "O"]:
                n += 1
    if n == 9:
        return True


board = [
         [1,2,3],
         [4,5,6],
         [7,8,9]
]

draw()

while True:
    player_one()
    draw()
    if win():
        print("Player one win.")
        break

    if tie():
        print("Tie!")
        break

    computer()
    draw()
    if win():
        print("Player two win.")
        break

    if tie():
        print("Tie!")
        break

   
################################################################################################


GUI of Tac Ti Toe

################################################

Step.1   --->   root
        
from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

x.mainloop() 

################################################

Step.2   --->   button

from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B1').grid(row=0, column=0)
x.mainloop()

################################################

Step.3   --->   label

from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B1')
b1.grid(row=0, column=0)

x.mainloop()

################################################

Step.4   --->   three button

from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B1')
b1.grid(row=0, column=0)
b2 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B2')
b2.grid(row=0, column=1)
b3 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B3')
b3.grid(row=0, column=2)

x.mainloop()

################################################

from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

b1 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B1')
b2 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B2')
b3 = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text='B3')

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

x.mainloop()

################################################

Step.5   --->   9 button

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

################################################

Step.6   --->   nested loop

for row in range(3):
    for column in range(3):
        print(row, column)

0  0 
0  1
0  2

1  0
1  1
1  2

2  0
2  1
2  2

################################################

# loop
from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

for row in range(3):
    for column in range(3):
        Button(x, width=16, height=8, font=('Arial', 30, 'bold'), text='B1').grid(row=row, column=column)

x.mainloop()


################################################

Step.7   --->   empty text

from tkinter import *


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3):
    for column in range(3):
        n += 1
        Button(x, width=16, height=8, font=('Arial', 30, 'bold'), text='').grid(row=row, column=column)

x.mainloop()

################################################

Step.8   --->   if click, show X

# event -> all data from click position
# event.widget -> botton of event position


from tkinter import *


def click(event):
    b = event.widget
    b['text'] = 'X'


x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3):
    for column in range(3):
        n += 1
        b = Button(x, width=8, height=4, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=column)
        b.bind("<Button-1>", click)

x.mainloop()

################################################

Step.9   --->   switch_player

current_player = "X"


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
        
        
################################################        

from tkinter import *


current_player = "X"


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
        
        
def click(event):
    b = event.widget
    b['text'] = current_player
    switch_player()
    

x = Tk()
x.title("Tac Ti Toe")

n = 0
for row in range(3):
    for column in range(3):
        n += 1
        b = Button(x, width=4, height=1, font=('Arial', 30, 'bold'), text=f'B{n}')
        b.grid(row=row, column=column)
        b.bind("<Button-1>", click)

x.mainloop()

################################################

Step.10   --->   control to write once

idea -> if somthing value, stop function and do nothing
code -> if b['text']: return


def click(event):
    b = event.widget
    if b['text']:
        return
    b['text'] = current_player
    switch_player()
    

################################################

from tkinter import *


current_player = "X"


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
       
        
def click(event):
    b = event.widget
    if b['text']:
        return
    b['text'] = current_player
    switch_player()
    

x = Tk()
x.title("Tac Ti Toe")

for row in range(3):
    for column in range(3):
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=column)
        b.bind("<Button-1>", click)

x.mainloop()

################################################

Step.11   --->   board, winner(), show_winner()  from CLI Tac Ti Toe

################################################

from tkinter import *
from tkinter import messagebox


current_player = "O"
board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
]


def winner():
    for i in range(3):
        row = board[i][0]['text'] == current_player and  board[i][1]['text'] == current_player and board[i][2]['text'] == current_player
        if row:
            return True
    for i in range(3):
        col= board[0][i]['text'] == current_player and  board[1][i]['text'] == current_player and board[2][i]['text'] == current_player
        if col:
            return True
    for a,b,c in ((0,1,2), (2,1,0)):
        diagonal = board[0][a]['text'] == current_player and  board[1][b]['text'] == current_player and board[2][c]['text'] == current_player
        if diagonal:
            return True


def show_winner():
    m = f"Player {current_player} win!"
    messagebox.showinfo("Game Over", m)


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
        

def click(event):
    b = event.widget
    if b['text']:
        return None
    b['text'] = current_player
    b.update_idletasks()
    if winner():
        show_winner()
        return 
    switch_player()


x = Tk()
x.title("Tac Ti Toe")

for row in range(3):
    for column in range(3):
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=column)
        b.bind("<Button-1>", click)
        board[row][column] = b

x.mainloop()

################################################

Step.12   --->   restart 


def restart():
    for r in range(3):
        for c in range(3):
            board[r][c]["text"] = ""


def restart():
    for l in board:
        for b in l:
            b["text"] = ""
            

################################################

from tkinter import *
from tkinter import messagebox


current_player = "O"

board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
]


def winner():
    for i in range(3):
        row = board[i][0]['text'] == current_player and  board[i][1]['text'] == current_player and board[i][2]['text'] == current_player
        if row:
            return True
    for i in range(3):
        col= board[0][i]['text'] == current_player and  board[1][i]['text'] == current_player and board[2][i]['text'] == current_player
        if col:
            return True
    for a,b,c in ((0,1,2), (2,1,0)):
        diagonal = board[0][a]['text'] == current_player and  board[1][b]['text'] == current_player and board[2][c]['text'] == current_player
        if diagonal:
            return True


def restart():
    for r in range(3):
        for c in range(3):
            board[r][c]["text"] = ""


def show_winner():
    m = f"Player {current_player} win!"
    messagebox.showinfo("Game Over", m)
    restart()


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
        

def click(event):
    b = event.widget
    if b['text']:
        return None
    b['text'] = current_player
    b.update_idletasks() 
    if winner():
        show_winner()
        return 
    switch_player()


x = Tk()
x.title("Tac Ti Toe")

for row in range(3):
    for column in range(3):
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=column)
        b.bind("<Button-1>", click)
        board[row][column] = b

x.mainloop()

################################################

Step.13   --->   tie(), show_tie()


# CLI
def tie():
    n = 0
    for l in board: 
        for b in l:
            if b in ["X", "O"]:
                n += 1
    if n == 9:
        return True
        

# button
def tie():
    n = 0
    for l in board:
        for b in l:
            if b["text"]:
                n += 1
    if n == 9:
        return True
        

# code quality       
def tie():
    for l in board:
        for b in l:
            if not b["text"]:
                return False
    return True
    

def show_tie():
    m = f"No one win!"
    messagebox.showinfo("Game Over", m)
    restart()
    
    
################################################    
    
from tkinter import *
from tkinter import messagebox

current_player = "O"

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


def winner():
    for i in range(3):
        row = board[i][0]['text'] == current_player and board[i][1]['text'] == current_player and board[i][2][
            'text'] == current_player
        if row:
            return True
    for i in range(3):
        col = board[0][i]['text'] == current_player and board[1][i]['text'] == current_player and board[2][i][
            'text'] == current_player
        if col:
            return True
    for a, b, c in ((0, 1, 2), (2, 1, 0)):
        diagonal = board[0][a]['text'] == current_player and board[1][b]['text'] == current_player and board[2][c][
            'text'] == current_player
        if diagonal:
            return True


def restart():
    n = 0
    for l in board:
        for b in l:
            b["text"] = ""


def tie():
    n = 0
    for l in board:
        for b in l:
            if b["text"]:
                n += 1
    if n == 9:
        return True


def show_tie():
    m = f"No one win. Tie!"
    messagebox.showinfo("Game Over", m)
    restart()


def show_winner():
    m = f"Player {current_player} win!"
    messagebox.showinfo("Game Over", m)
    restart()


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def click(event):
    b = event.widget
    if b['text']:
        return None
    b['text'] = current_player
    b.update_idletasks() 
    if winner():
        show_winner()
        return

    if tie():
        show_tie()

    switch_player()


x = Tk()
x.title("Tac Ti Toe")

for row in range(3):
    for column in range(3):
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=column)
        b.bind("<Button-1>", click)
        board[row][column] = b

x.mainloop()
 
################################################

Step.14   --->   Scrolls ( Add and show scrolls after Game Over. ) 

# Marks
x_scroll = 0
y_scroll = 0
l1 = Label(x, text="X scroll = 0", font=('Arial', 25, 'bold'))
l1.grid(row=3, columnspan=3) # columnspan -> column count

l2 = Label(x, text="O scroll = ", font=('Arial', 25, 'bold'))
l2.grid(row=4, columnspan=3)


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
        l2['text'] = f"Y scroll = {y_scroll}"
    restart()
    

################################################

from tkinter import *
from tkinter import messagebox

current_player = "O"
x_scroll = 0
y_scroll = 0

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


def winner():
    for i in range(3):
        row = board[i][0]['text'] == current_player and board[i][1]['text'] == current_player and board[i][2][
            'text'] == current_player
        if row:
            return True
    for i in range(3):
        col = board[0][i]['text'] == current_player and board[1][i]['text'] == current_player and board[2][i][
            'text'] == current_player
        if col:
            return True
    for a, b, c in ((0, 1, 2), (2, 1, 0)):
        diagonal = board[0][a]['text'] == current_player and board[1][b]['text'] == current_player and board[2][c][
            'text'] == current_player
        if diagonal:
            return True


def restart():
    n = 0
    for l in board:
        for b in l:
            b["text"] = ""


def tie():
    for l in board:
        for b in l:
            if not b["text"]:
                return False
    return True


def show_tie():
    m = f"No one win!"
    messagebox.showinfo("Game Over", m)
    restart()


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
        l2['text'] = f"O scroll = {y_scroll}"
    restart()


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def click(event):
    b = event.widget
    if b['text']:
        return None
    b['text'] = current_player
    b.update_idletasks() 
    if winner():
        show_winner()
        return

    if tie():
        show_tie()

    switch_player()


x = Tk()
x.title("Tac Ti Toe")

for row in range(3):
    for column in range(3):
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=column)
        b.bind("<Button-1>", click)
        board[row][column] = b

l1 = Label(x, text="X scroll = 0", font=('Arial', 25, 'bold'))
l1.grid(row=3, columnspan=3) # columnspan -> column count

l2 = Label(x, text="O scroll = 0", font=('Arial', 25, 'bold'))
l2.grid(row=4, columnspan=3)

x.mainloop()


################################################

Step.15   --->   add color

# click()

if current_player == 'X':
    b["fg"] = "purple"
else:
    b["fg"] = "blue"
    
    
def click(event):
    b = event.widget
    if b['text']:
        return None

    if current_player == 'X':
        b["fg"] = "purple"
    else:
        b["fg"] = "blue"
    b['text'] = current_player
    b.update_idletasks() 
    if winner():
        show_winner()
        return

    if tie():
        show_tie()

    switch_player()


################################################

from tkinter import *
from tkinter import messagebox

current_player = "O"
x_scroll = 0
y_scroll = 0

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


def winner():
    for i in range(3):
        row = board[i][0]['text'] == current_player and board[i][1]['text'] == current_player and board[i][2][
            'text'] == current_player
        if row:
            return True
    for i in range(3):
        col = board[0][i]['text'] == current_player and board[1][i]['text'] == current_player and board[2][i][
            'text'] == current_player
        if col:
            return True
    for a, b, c in ((0, 1, 2), (2, 1, 0)):
        diagonal = board[0][a]['text'] == current_player and board[1][b]['text'] == current_player and board[2][c][
            'text'] == current_player
        if diagonal:
            return True


def restart():
    n = 0
    for l in board:
        for b in l:
            b["text"] = ""


def tie():
    for l in board:
        for b in l:
            if not b["text"]:
                return False
    return True


def show_tie():
    m = f"No one win!"
    messagebox.showinfo("Game Over", m)
    restart()


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
        l2['text'] = f"Y scroll = {y_scroll}"
    restart()


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def click(event):
    b = event.widget
    
    if b['text']:
        return None

    b['text'] = current_player
    b.update_idletasks()

    if current_player == 'X':
        b["fg"] = "purple"
    else:
        b["fg"] = "blue"

    if winner():
        show_winner()
        return

    if tie():
        show_tie()
        return

    switch_player()


x = Tk()
x.title("Tac Ti Toe")

for row in range(3):
    for column in range(3):
        b = Button(x, width=4, height=2, font=('Arial', 30, 'bold'), text='')
        b.grid(row=row, column=column)
        b.bind("<Button-1>", click)
        board[row][column] = b

l1 = Label(x, text="X scroll = 0", font=('Arial', 25, 'bold'))
l1.grid(row=3, columnspan=3) # columnspan -> column count

l2 = Label(x, text="O scroll = 0", font=('Arial', 25, 'bold'))
l2.grid(row=4, columnspan=3)

x.mainloop()

################################################

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

################################################################################################

Tac Ti Toe 

CLI 23 steps + GUI 16 steps 

total steps = 39 steps


################################################################################################

   

"""

