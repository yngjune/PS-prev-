from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

region = 0
max_area = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] and not visit[i][j]:
            region += 1
            area = 0

            queue = deque()
            queue.append((i,j))
            visit[i][j] = True
            while queue:
                cur = queue.popleft()
                x, y = cur[0], cur[1]
                area += 1
                
                for k in range(4):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if xx >= 0 and xx < N and yy >= 0 and yy < M \
                        and graph[xx][yy] and not visit[xx][yy]:
                        queue.append((xx, yy))
                        visit[xx][yy] = True
                        
            max_area = max(max_area, area)

print(region)
print(max_area)