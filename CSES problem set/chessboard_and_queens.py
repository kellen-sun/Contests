board=[]
board.append(list(input()))
board.append(list(input()))
board.append(list(input()))
board.append(list(input()))
board.append(list(input()))
board.append(list(input()))
board.append(list(input()))
board.append(list(input()))
def is_safe(board, row, col):
    if board[row][col] == '*':
        return False
    for i in range(row):
        if board[i][col] == 'q':
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'q':
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i >= 0 and j < 8:
        if board[i][j] == 'q':
            return False
        i -= 1
        j += 1
    return True
    

def place_queens(board, row):
    global k
    if  row == 8:
        k += 1
        return True
    res = False
    for c in range(8):
        
        if is_safe(board, row, c):
            board[row][c] = 'q'
            res = place_queens(board, row + 1) or res
            board[row][c] = '.'
    return res
                    
k = 0
b = board
place_queens(b, 0)
print(k)
