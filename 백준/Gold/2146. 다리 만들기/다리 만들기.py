from collections import deque
from sys import stdin

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def BFS_number(sx, sy, land):
    queue = deque()
    queue.append((sx,sy))
    visit[sx][sy] = True
    graph[sx][sy] = land

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1 and not visit[nx][ny]:
                queue.append((nx,ny))
                visit[nx][ny] = True
                graph[nx][ny] = land


def BFS_bridge(land):
    queue = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j] == land:
                queue.append((i,j))
                depth[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] != 0 and graph[nx][ny] != land:
                return depth[x][y]

            if graph[nx][ny] == 0 and depth[nx][ny] == -1:
                queue.append((nx,ny))
                depth[nx][ny] = depth[x][y] + 1

    return N


N = int(input())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]

# label islands
land = 1
visit = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visit[i][j]:
            BFS_number(i,j,land)
            land += 1

# miminum length bridge
min_len = N * 2
for l in range(1, land):
    depth = [[-1] * N for _ in range(N)]
    min_len = min(BFS_bridge(l), min_len)

print(min_len)