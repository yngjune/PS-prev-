from itertools import combinations
from collections import deque

GREEN = 3
RED = 4
FLOWER = 5

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(sel_r, sel_g):
    ans = 0
    board = [[[0, 0] for _ in range(M)] for _ in range(N)] # time, color
    queue = deque()

    for idx in sel_r:
        cx, cy = candidate[idx]
        board[cx][cy][1] = RED
        queue.append((cx,cy))

    for idx in sel_g:
        cx, cy = candidate[idx]
        board[cx][cy][1] = GREEN
        queue.append((cx,cy))

    while queue:
        x, y = queue.popleft()
        time, color = board[x][y]
        
        if color == FLOWER: continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if garden[nx][ny] == 0:
                continue
            if board[nx][ny][1] == 0:
                board[nx][ny][0], board[nx][ny][1] = time+1, color
                queue.append((nx,ny))
            elif board[nx][ny][1] == RED and color == GREEN and board[nx][ny][0] == board[x][y][0]+1:
                board[nx][ny][1] = FLOWER
                ans += 1
            elif board[nx][ny][1] == GREEN and color == RED and board[nx][ny][0] == board[x][y][0]+1:
                board[nx][ny][1] = FLOWER
                ans += 1

    
    return ans


N, M, g, r = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]

candidate = []
for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            candidate.append((i,j))

ans = 0

for c1 in combinations(range(len(candidate)), r+g):
    for c2 in combinations(c1, r):
        sel_r = list(c2)
        sel_g = [x for x in c1 if x not in c2]

        ans = max(ans, BFS(sel_r, sel_g))

print(ans)