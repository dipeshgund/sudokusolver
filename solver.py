def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=" ")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def valid(board, num, pos):
    # check row
    for i in range(len(board)):
        if board[pos[0]][i] == num:
            return False

    # check column
    for i in range(len(board)):
        if board[i][pos[1]] == num:
            return False
    # check in grid
    x = pos[0] // 3
    y = pos[1] // 3
    for i in range(x * 3, (x * 3) + 3):
        for j in range(y * 3, (y * 3) + 3):
            if board[i][j] == num:
                return False

    return True


def solve(board):
    empty = find_empty(board)
    if empty is None:
        return True
    for i in range(1, 10):
        if valid(board, i, empty):
            board[empty[0]][empty[1]] = i

            if solve(board):
                return True
            else:
                board[empty[0]][empty[1]] = 0

    return False


board = [
    [0, 0, 0, 0, 5, 0, 0, 4, 0],
    [0, 0, 6, 7, 4, 1, 2, 8, 5],
    [4, 8, 0, 9, 0, 0, 0, 0, 6],
    [2, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 9, 8, 1, 0, 2, 5, 6, 0],
    [0, 0, 0, 0, 9, 0, 0, 0, 7],
    [3, 0, 0, 0, 0, 9, 0, 1, 2],
    [8, 7, 2, 3, 1, 6, 4, 0, 0],
    [0, 1, 0, 0, 7, 0, 0, 0, 0]
]

print_board(board)

print("________________________")
solve(board)
print_board(board)
