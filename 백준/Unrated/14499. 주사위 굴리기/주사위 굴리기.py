from sys import stdin

def update_pos(x,y,dir):
    if dir == 1: # E
        nx, ny = (x, y+1)
    elif dir == 2: # W
        nx, ny = (x, y-1)
    elif dir == 3: # N
        nx, ny = (x-1, y)
    else: # S
        nx, ny = (x+1, y)

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        return (x, y)
    else:
        return (nx, ny)

def rotate_dice(dice, dir):
    B, N, E, W, S, T = dice
    if dir == 1: # E
        return [E, N, T, B, S, W]
    elif dir == 2: # W
        return [W, N, B, T, S, E]
    elif dir == 3: # N
        return [N, T, E, W, B, S]
    else: # S
        return [S, B, E, W, T, N]

N, M, x, y, K = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
command = list(map(int, stdin.readline().split()))

dice = [0, 0, 0, 0, 0, 0] # [BOT, N, E, W, S, TOP]
for d in command:
    nx, ny = update_pos(x,y,d)
    if nx == x and ny == y:
        continue
    
    x, y = nx, ny
    dice = rotate_dice(dice, d)
    if board[x][y] == 0:
        board[x][y] = dice[0]
    else:
        dice[0] = board[x][y]
        board[x][y] = 0
    print(dice[-1])