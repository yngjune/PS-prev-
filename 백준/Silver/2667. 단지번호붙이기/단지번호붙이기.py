from sys import stdin

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def DFS(i, j):
    stk = [(i, j)]
    cnt = 0
    while stk:
        x, y = stk.pop()
        if visit[x][y]: continue

        visit[x][y] = True
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny]:
                stk.append((nx,ny))

    return cnt

N = int(input())
graph = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
count = []

for i in range(N):
    for j in range(N):
        if graph[i][j] and not visit[i][j]:
            count.append(DFS(i,j))

print(len(count),*sorted(count), sep='\n')