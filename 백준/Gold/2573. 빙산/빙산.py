from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(sx,sy):
    queue = deque()
    queue.append((sx,sy))

    sea_count = [[0] * M for _ in range(N)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if ice[nx][ny] == 0:
                sea_count[x][y] += 1
            elif not visit[nx][ny]:
                queue.append((nx, ny))
                visit[nx][ny] = True

    # update height
    for i in range(N):
        for j in range(M):
            if ice[i][j]:
                ice[i][j] = max(0, ice[i][j] - sea_count[i][j])

    return 1


N, M = map(int, input().split())
ice = [list(map(int, stdin.readline().split())) for _ in range(N)]

year = 1
divided = False
while True:
    visit = [[False] * M for _ in range(N)]
    lands = 0

    for i in range(N):
        for j in range(M):
            if ice[i][j] and not visit[i][j]:
                visit[i][j] = True
                lands += BFS(i,j)

    if lands > 1:
        print(year - 1)
        divided = True
        break

    if ice == [[0] * M for _ in range(N)]:
        break

    year += 1

if not divided: print(0)