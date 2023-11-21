from sys import stdin
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, stdin.readline().split())
board = [stdin.readline().rstrip() for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]

queue = deque()
queue.append((0, 0))
dist[0][0] = 1

while queue:
    cx, cy = queue.popleft()
    if cx == n-1 and cy == m-1:
        print(dist[cx][cy])
        break

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
            continue
        if board[nx][ny] == "1" and dist[nx][ny] == 0:
            dist[nx][ny] = dist[cx][cy] + 1
            queue.append((nx, ny))