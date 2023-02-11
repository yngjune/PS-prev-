from sys import stdin
from collections import deque

M, N, H = map(int, input().split())
# [h][n][m]
graph = [[
    list(map(int, stdin.readline().split())) for _ in range(N)
] for _ in range(H)]

queue = deque()
avail = True
dy = [-1, 1, 0, 0]
dz = [0, 0, 1, -1]
dx = [1, -1]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i,j,k,0))

while queue:
    cur = queue.popleft()
    for i in range(4):
        x = cur[0]
        y = cur[1] + dy[i]
        z = cur[2] + dz[i]

        if x >= 0 and x < H and y >= 0 and y < N and z >= 0 and z < M \
            and graph[x][y][z] == 0:
            graph[x][y][z] = 1
            queue.append((x,y,z,cur[3]+1))
    
    for i in range(2):
        x = cur[0] + dx[i]
        y = cur[1]
        z = cur[2]

        if x >= 0 and x < H and y >= 0 and y < N and z >= 0 and z < M \
            and graph[x][y][z] == 0:
            graph[x][y][z] = 1
            queue.append((x,y,z,cur[3]+1))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                avail = False
                break

print(cur[3] if avail else -1)