from sys import stdin
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(color, sx, sy):
    queue = deque([(sx,sy)])
    q_acc = [(sx, sy)]
    visit[sx][sy] = True
    acc = 0

    while queue:
        x, y = queue.popleft()
        acc += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue
            if not visit[nx][ny] and board[nx][ny] == color:
                queue.append((nx,ny))
                q_acc.append((nx,ny))
                visit[nx][ny] = True

    if acc >= 4:
        global pop_list
        pop_list += q_acc


def drop():
    for j in range(6):
        line = ["."] * 12
        idx = 11
        for i in range(11, -1, -1):
            if board[i][j] != '.':
                line[idx] = board[i][j]
                idx -= 1
        for i in range(11, -1, -1):
            board[i][j] = line[i]


board = [list(stdin.readline().rstrip()) for _ in range(12)]
ans = 0

while True:
    pop_list = []
    visit = [[False] * 6 for i in range(12)]

    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                bfs(board[i][j], i, j)
    
    if len(pop_list) == 0:
        break

    for (x, y) in pop_list:
        board[x][y] = '.'
    drop()
    
    ans += 1

print(ans)