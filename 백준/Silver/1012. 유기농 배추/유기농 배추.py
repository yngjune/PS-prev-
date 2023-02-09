from sys import stdin

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for _ in range(T):
    N, M, K = map(int, stdin.readline().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        i, j = map(int, stdin.readline().split())
        graph[i][j] = 1
    
    count = 0
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] and not visit[i][j]:
                count += 1
                # DFS
                stack = [(i,j)]
                while stack:
                    cur = stack.pop()
                    if not visit[cur[0]][cur[1]]:
                        visit[cur[0]][cur[1]] = 1
                        for k in range(4):
                            x = cur[0] + dx[k]
                            y = cur[1] + dy[k]
                            if x >= 0 and x < N and y >= 0 and y < M and graph[x][y]:
                                stack.append((x,y))

    print(count)