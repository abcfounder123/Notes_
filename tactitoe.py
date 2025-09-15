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