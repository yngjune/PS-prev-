from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
tomato = [list(map(int, stdin.readline().split())) for _ in range(n)]
depth = [[-1 for _ in range(m)] for _ in range(n)]

queue = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i,j))
            depth[i][j] = 0

while queue:
    cx, cy = queue.popleft()

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if tomato[nx][ny] == 0 and depth[nx][ny] == -1:
            tomato[nx][ny] = 1
            ans = depth[cx][cy] + 1
            depth[nx][ny] = ans
            queue.append((nx, ny))

done = True
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            done = False
if done:
    print(ans)
else:
    print(-1)