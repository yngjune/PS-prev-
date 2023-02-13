from sys import stdin
from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

T = int(input())
for _ in range(T):
    N = int(stdin.readline())
    sx, sy = map(int, stdin.readline().split())
    tx, ty = map(int, stdin.readline().split())

    queue = deque()
    graph = [[0] * N for _ in range(N)]

    queue.append((sx, sy))
    while queue:
        cur = queue.popleft()
        if cur == (tx, ty):
            print(graph[cur[0]][cur[1]])
            break
            
        for i in range(8):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]
            if x >= 0 and x < N and y >= 0 and y < N \
                and graph[x][y] == 0:
                queue.append((x,y))
                graph[x][y] = graph[cur[0]][cur[1]] + 1
    