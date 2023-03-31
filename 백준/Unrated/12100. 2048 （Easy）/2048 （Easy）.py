def shift_left(board):
    shifted_board = []
    for i in range(N):
        shifted_row = [0] * N
        idx = 0
        for j in range(N):
            if board[i][j] == 0:
                continue
            if shifted_row[idx] == 0:
                shifted_row[idx] = board[i][j]
            elif shifted_row[idx] == board[i][j]:
                shifted_row[idx] *= 2
                idx += 1
            else:
                idx += 1
                shifted_row[idx] = board[i][j]
        shifted_board.append(shifted_row)
    return shifted_board


def rotate(board):
    rotated_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated_board[i][j] = board[j][N-1-i]

    return rotated_board


def clone(board):
    cloned = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cloned[i][j] = board[i][j]
    return cloned


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for t in range(1024):
    board_tmp = clone(board)
    tmp = t
    for _ in range(5):
        k = tmp % 4
        tmp //= 4
        for _ in range(k):
            board_tmp = rotate(board_tmp)
        board_tmp = shift_left(board_tmp)
    
    for i in range(N):
        for j in range(N):
            ans = max(board_tmp[i][j], ans)

print(ans)
