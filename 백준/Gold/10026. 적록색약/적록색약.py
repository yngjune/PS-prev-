from collections import deque
from sys import stdin

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(map, visit, N, start, crit):
    queue = deque()
    visit[start[0]][start[1]] = True
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]
            if x >= 0 and x < N and y >= 0 and y < N \
                and crit(map[cur[0]][cur[1]], map[x][y]) \
                and not visit[x][y]:
                visit[x][y] = True
                queue.append((x,y))


def crit_weak(cur, next):
    if cur == 'R' or cur == 'G':
        return next == 'R' or next == 'G'
    else: 
        return cur == next

def crit(cur, next):
    return cur == next


N = int(input())
graph = [list(stdin.readline()[:-1]) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]
visit_weak = [[False for _ in range(N)] for _ in range(N)]

cnt = 0
cnt_weak = 0

for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            BFS(graph, visit, N, (i,j), crit)
            cnt += 1
        
        if not visit_weak[i][j]:
            BFS(graph, visit_weak, N, (i,j), crit_weak)
            cnt_weak += 1
        
print(cnt, cnt_weak)