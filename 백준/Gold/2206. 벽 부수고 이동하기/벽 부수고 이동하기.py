from sys import stdin
from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, stdin.readline()[:-1])) for _ in range(N)]
depth = [[[0] * 2 for _ in range(M)]for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0,0,0))
depth[0][0][0] = 1
ans = -1

while queue:
    x, y, broken = queue.popleft()
    if x == N-1 and y == M-1:
        ans = depth[x][y][broken]
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if graph[nx][ny] == 0 and depth[nx][ny][broken] == 0:
            queue.append((nx,ny,broken))
            depth[nx][ny][broken] = depth[x][y][broken] + 1

        elif graph[nx][ny] == 1 and broken == 0:
            queue.append((nx,ny,1))
            depth[nx][ny][1] = depth[x][y][0] + 1

print(ans)