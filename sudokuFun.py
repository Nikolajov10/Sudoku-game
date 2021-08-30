limit = 9

def check_row(matrix, i, j, value):
    for k in range(0, limit):
        if k == j:
            continue
        if abs(matrix[i][k]) == value:
            return 0
    return 1

def check_column(matrix, i, j, value):
    for k in range(0, limit):
        if k == i:
            continue
        if abs(matrix[k][j]) == value:
            return 0
    return 1

def check_square(matrix, i, j, value):
    # 0 3 2
    if j <= 2:
        cr = 0
    elif j <= 5:
        cr = 3
    else:
        cr = 6
    if i<=2:
        rr=0
    elif i<=5:
        rr=3
    else:
        rr=6
    for k in range(rr,rr+3):
        for r in range(cr,cr+3):
            if k == i and r == j:
                continue
            if abs(matrix[k][r]) == value:
                return 0
    return 1

def find_empty(board):
    for i in range(0, limit):
        for j in range(0, limit):
            if board[i][j] == 0:
                return i, j
    return -1, -1

def find_back(board, startrow, startcolumn):
    k = 0
    for i in range(startrow, -1, -1):
        k += 1
        if k == 2:
            startcolumn = 9
        for j in range(startcolumn - 1, -1, -1):
            if board[i][j] < 0:
                return i, j
    return -1, -1

def solve(board):
    row, column = find_empty(board)
    ind = 0
    while row>=0 and column>=0:
        start = abs(board[row][column]) + 1
        for i in range(start, limit + 1):
            if (check_column(board, row, column, i) + check_row(board, row, column, i) + check_square(board, row,column, i)) == 3:
                board[row][column] = (-1) * i
                ind = 1
                break
        if ind == 0:
            if board[row][column] != 0:
                board[row][column] = 0
            row, column = find_back(board, row, column)
        else:
            row, column = find_empty(board)
            ind=0

def finish_table(board):
    for i in range(limit):
        for j in range(limit):
            if board[i][j]<0:
                board[i][j]=abs(board[i][j])