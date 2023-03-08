from sys import stdin

N, M = map(int, input().split())
graph = [list(stdin.readline().rstrip()) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
ans = 0

for i in range(N):
    if graph[i][0] == '1':
        dp[i][0] = 1
        ans = 1
    else:
        dp[i][0] = 0

for i in range(M):
    if graph[0][i] == '1':
        dp[0][i] = 1
        ans = 1
    else:
        dp[0][i] = 0

for i in range(1,N):
    for j in range(1,M):
        if graph[i][j] == '0':
            continue
        dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        if dp[i][j] > ans: ans = dp[i][j]

print(ans * ans)