from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    global ans
    queue = deque()
    visit = [[False] * 5 for _ in range(5)]
    princess = [[False] * 5 for _ in range(5)]
    for k in seq:
        i = k // 5
        j = k % 5
        if not queue:
            visit[i][j] = True
            queue.append((i,j))
        princess[i][j] = True
    
    acc = 0
    dasom = 0
    while queue:
        x, y = queue.popleft()
        acc += 1
        if graph[x][y] == 'S': dasom += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 5 or nx < 0 or ny >= 5 or ny < 0:
                continue
            if not princess[nx][ny] or visit[nx][ny]:
                continue
            queue.append((nx,ny))
            visit[nx][ny] = True

    if acc >= 7 and dasom >= 4:
        ans += 1

def combination(depth, N, start):
    if depth == 7:
        bfs()
        return
    
    for i in range(start, N):
        seq[depth] = i
        combination(depth+1, N, i+1)


graph = [input() for _ in range(5)]
seq = [0] * 7
ans = 0
combination(0, 25, 0)

print(ans)