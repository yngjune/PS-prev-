from sys import stdin
from collections import deque

R, C = map(int, input().split())
graph = [list(stdin.readline()[:-1]) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
escape = False

queue = deque()
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            queue.append((i,j,0,0)) # (posX, posY, J/F, depth)
        elif graph[i][j] == 'F':
            queue.appendleft((i,j,1,0))

while queue:
    cur = queue.popleft()
    if cur[2] == 0: # Jihun
        if cur[0] == R - 1 or cur[1] == C - 1 \
            or cur[0] == 0 or cur[1] == 0:
            escape = True
            break
        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]
            if x >= 0 and x < R and y >= 0 and y < C \
                and graph[x][y] == '.':
                graph[x][y] = 'J'
                queue.append((x,y,0,cur[3]+1))
        
    else: # Fire
        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]
            if x >= 0 and x < R and y >= 0 and y < C \
                and (graph[x][y] == '.' or graph[x][y] == 'J'):
                graph[x][y] = 'F'
                queue.append((x,y,1,cur[3]+1))

print(cur[3]+1 if escape else 'IMPOSSIBLE')