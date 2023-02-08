from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
depth = 0
valid = True

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i,j,depth))

while queue:
    cur = queue.popleft()
    for i in range(4):
        x = cur[0] + dx[i]
        y = cur[1] + dy[i]

        if x >= 0 and x < N and y >= 0 and y < M and graph[x][y] == 0:
            graph[x][y] = 1
            queue.append((x,y,cur[2]+1))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            valid = False

print(cur[2] if valid else -1)