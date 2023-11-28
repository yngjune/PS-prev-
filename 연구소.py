from collections import deque
from itertools import combinations
from copy import deepcopy
from sys import stdin

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, stdin.readline().split())
lab = [list(map(int, stdin.readline().split())) for _ in range(n)]

candi = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            candi.append((i,j))

ans = 0

for c in combinations(candi, 3):
    newlab = deepcopy(lab)

    for x, y in c:
        newlab[x][y] = 1
    
    queue = deque()
    for i in range(n):
        for j in range(m):
            if newlab[i][j] == 2:
                queue.append((i,j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m and newlab[nx][ny] == 0:
                newlab[nx][ny] = 2
                queue.append((nx,ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if newlab[i][j] == 0:
                cnt += 1

    if cnt > ans:
        ans = cnt

print(ans)