from collections import deque
from sys import stdin



hdx = [1, 2, 2, 1, -1, -2, -2, -1]
hdy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(graph, dist):
    queue = deque()
    queue.append((0,0,0))
    dist[0][0][0] = 0

    while queue:
        x, y, h = queue.popleft()
        if x == H-1 and y == W-1:
            return dist[x][y][h]
        
        if h != K:
            for i in range(8):
                nx = x + hdx[i]
                ny = y + hdy[i]

                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    continue
                if graph[nx][ny] == 0 and dist[nx][ny][h+1] == -1:
                    queue.append((nx,ny,h+1))
                    dist[nx][ny][h+1] = dist[x][y][h] + 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if graph[nx][ny] == 0 and dist[nx][ny][h] == -1:
                queue.append((nx,ny,h))
                dist[nx][ny][h] = dist[x][y][h] + 1
    
    return -1

            

K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(H)]
dist = [[[-1] * 31 for _ in range(W)] for _ in range(H)]

print(BFS(graph, dist))