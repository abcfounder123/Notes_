

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