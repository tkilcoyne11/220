"""
Name: Tucker Kilcoyne
lab10.py
"""


def build():
    return list(range(1, 10))


def display(board):
    for i in range(3):
        n = i * 3
        print(board[n], "|", board[n+1], "|", board[n+2])
        print(10 * "-")


def place(board, pos, piece):
    if piece == "X" or piece == "O":
        board[pos - 1] = piece
    else:
        print("That is not a valid piece.")


def legal(board, pos):
    if 1 <= pos <= 9 and board[pos - 1] == pos:
        return True
    return False


def isWon(board, piece):
    for i in range(3):
        n = i * 3
        if board[n] != piece:
            continue
        if board[n+1] != piece:
            continue
        if board[n+2] != piece:
            continue
        return True
    for i in range(3):
        if board[i] != piece:
            continue
        if board[i+3] != piece:
            continue
        if board[i+6] != piece:
            continue
        return True
    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True
    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True
    return False


def over(board):
    if isWon(board, "X"):
        return True
    elif isWon(board, "O"):
        return True
    else:
        for i in range(9):
            if board[i] == i + 1:
                return False
        return True


def play():
    board = build()
    while True:
        display(board)
        player1 = eval(input("Player 1 - Enter a position (1, 9): "))
        if legal(board, player1):
            place(board, player1, "X")
        if over(board):
            if isWon(board, "X"):
                display(board)
                print("X won!")
                break
            else:
                display(board)
                print("It's a tie!")
                break
        display(board)
        player2 = eval(input("Player 2 - Enter a position (1,9): "))
        if legal(board, player2):
            place(board, player2, "O")
        if over(board):
            if isWon(board, "O"):
                display(board)
                print("O won!")
                break


def main():
    play()
    pass


main()
